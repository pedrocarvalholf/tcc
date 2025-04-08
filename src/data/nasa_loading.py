import requests
import os
import time
import concurrent.futures
import random
import numpy as np

# Define the output directory
output = r".data/raw/output_brazil_grid"
os.makedirs(output, exist_ok=True)

# Define the base URL for the API request (Hourly data for the year 2024)
base_url = r"https://power.larc.nasa.gov/api/temporal/hourly/point?parameters={parameters}&community=RE&longitude={longitude}&latitude={latitude}&start=20240101&end=20241231&format=CSV"

# List of renewable energy parameters available in the NASA POWER API
parameters = [
    "ALLSKY_SFC_SW_DWN",  # Surface Downward Shortwave Radiation (W/m²)
    "T2M",  # 2m Temperature (°C)
    "RH2M",  # 2m Relative Humidity (%)
    "WS10M",  # 10m Wind Speed (m/s)
    #"PRECTOT",  # Total Precipitation (mm)
    #"SH2O",  # Surface Humidity (g/m²)
    #"SRAD",  # Solar Radiation (W/m²)
    #"CLRSKY_SFC_SW_DWN",  # Clear Sky Surface Downward Shortwave Radiation (W/m²)
    "ALLSKY_KT" #,  # Surface Pressure (Pa)
    #"WSPD10M",  # Wind Speed at 10m (m/s)
]

# Define the grid of latitudes and longitudes (0.5 x 0.5 resolution for Brazil)
latitudes = list(np.arange(-34.0, 6.0, 0.5))      # From -34.0 to 6.0
longitudes = list(np.arange(-74.0, -34.0, 0.5))   # From -74.0 to -34.0

# Function to make API request and save the data for a given latitude and longitude
def fetch_data_for_location(latitude, longitude, param_list):
    # Construct the API request URL for the current grid point
    params = ','.join(param_list)
    api_request_url = base_url.format(longitude=longitude, latitude=latitude, parameters=params)

    retries = 1  # Number of retries in case of error
    backoff_factor = 2  # Exponential backoff factor

    for attempt in range(retries):
        try:
            # Make the API request with a timeout of 30 seconds
            response = requests.get(api_request_url, verify=True, timeout=30.0)
            
            # Check if the response status is OK (200)
            if response.status_code == 200:
                # Define the output CSV file path
                filename = f"location_{latitude}_{longitude}_2024.csv"
                filepath = os.path.join(output, filename)

                # Write the data to a CSV file
                with open(filepath, 'wb') as csvfile:
                    csvfile.write(response.content)  # Save the CSV content directly

                print(f"Data for location ({latitude}, {longitude}) saved to {filepath}")
                break  # Exit the loop if the request was successful
            else:
                print(f"Error {response.status_code}: Could not fetch data for location ({latitude}, {longitude})")
                time.sleep(10)  # Wait before retrying
        except requests.exceptions.RequestException as e:
            print(f"Request error for location ({latitude}, {longitude}): {e}")
            if attempt < retries - 1:
                time.sleep(backoff_factor ** attempt)  # Exponential backoff
            else:
                print(f"Failed after {retries} attempts for location ({latitude}, {longitude})")
                break

# Create a list of all latitude and longitude pairs
locations = [(lat, lon) for lat in latitudes for lon in longitudes]

# Function to handle batching of parameters (to stay within the limit of 10 parameters per call)
def chunk_parameters(parameter_list, chunk_size=10):
    for i in range(0, len(parameter_list), chunk_size):
        yield parameter_list[i:i + chunk_size]

# Using ThreadPoolExecutor to run the API calls in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Loop through all latitude and longitude locations
    future_to_location = {}
    for lat, lon in locations:
        for param_chunk in chunk_parameters(parameters):
            # Submit each API call in parallel
            future = executor.submit(fetch_data_for_location, lat, lon, param_chunk)
            future_to_location[future] = (lat, lon)

    # Wait for all futures to complete
    for future in concurrent.futures.as_completed(future_to_location):
        location = future_to_location[future]
        try:
            future.result()  # If any exception occurred, it will be raised here
        except Exception as e:
            print(f"Exception for {location}: {e}")

        # Delay to avoid hitting API rate limits
        time.sleep(2)  # sleep 1 second between requests to avoid overloading the server
