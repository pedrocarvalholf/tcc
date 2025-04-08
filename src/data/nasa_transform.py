import pandas as pd

def filter_nasa_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process a yearly csv file from ONS for a given location and return a cleaned dataframe for this location
    
    Parameters
    ----------
    df: .csv file
        A CSV file from NASA Power API containing climate parameters
    
    Returns
    -------
    df: pd.dataframe 
        A cleaned dataframe file from NASA
    
    
    """
    import os
    import re

    filepath = os.getcwd() + '/output_brazil_grid/'
    filename = df

    df = pd.read_csv(df, skiprows = 12, sep = ",")
    df.columns = df.iloc[0]
    df = df[1:].reset_index()
    df.columns.name = None
    df = df.rename(columns={"level_0": "YEAR", "level_1": "MO", "level_2": "DY", "level_3": "HR", "level_4": "ALLSKY_SFC_SW_DWN", "level_5": "T2M", "level_6": " RH2M", "level_7": "WS10M"})

    match = re.search(r"location_([-+]?[0-9]*\.?[0-9]+)_([-+]?[0-9]*\.?[0-9]+)_\d{4}\.csv", filename)
    if match:
        lat = float(match.group(1))
        lon = float(match.group(2))

    df['latitude'] = lat
    df['longitude'] = lon
    #df['location'] = f"{lat},{lon}"

    return df