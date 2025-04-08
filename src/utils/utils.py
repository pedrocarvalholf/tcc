import pandas as pd
import numpy as np

def info_yearly_ons(df: pd.DataFrame):
    """
    Receives the yearly ONS dataframe and returns the description of it, and also #usines, #nulls and #NaN
    
    Parameters
    ----------
    df: pd.DataFrame
        A yearly dataframe from ONS containing only data from PV

    Returns
    ------- 
    """

    print(df.info())
    print(f"Quantidade de usinas fotovoltaicas no dataframe: {len(df['nom_usina'].unique())}" )
    print(f'Quantidade de valores nulos no DataFrame: {df.isnull().sum().sum()}')
    print(f'Quantidade de valores NaN no DataFrame: {df.isna().sum().sum()}')


def most_common_count(df) -> tuple:
    """
    Receives the yearly ONS dataframe and returns a tuple with the #entries for each usine and the maximum #entries in the dataset
    
    Parameters
    ----------
    df: pd.DataFrame
        A yearly dataframe from ONS containing only data from PV

    Returns
    ------- 
    tuple: (counts,most_common_count)
    """

    counts = df.groupby('nom_usina').size()
    most_common_count = counts.value_counts().idxmax()
    return counts,most_common_count

def identify_missing_data_usines(df: pd.DataFrame) -> pd.DataFrame:
    """
    Receives the yearly ONS dataframe and returns a dataframe containing the names and #of entries of usines without a complete year time series
    
    Parameters
    ----------
    df: pd.DataFrame
        A yearly dataframe from ONS containing only data from PV

    Returns
    ------- 
    df: pd.DataFrame
    """

    usine_counts, most_common_usine_count = most_common_count(df)
    usines_missing_data = usine_counts[usine_counts != most_common_usine_count].reset_index()

    return usines_missing_data

def identify_complete_data_usines(df: pd.DataFrame) -> pd.DataFrame:
    """
    Receives the yearly ONS dataframe and returns a dataframe containing the names and #of entries of usines with a complete year time series
    
    Parameters
    ----------
    df: pd.DataFrame
        A yearly dataframe from ONS containing only data from PV

    Returns
    ------- 
    df: pd.DataFrame
    """

    usine_counts, most_common_usine_count = most_common_count(df)
    usines_complete_data  = usine_counts[usine_counts == most_common_usine_count].reset_index()

    return usines_complete_data

def haversine(lat1, lon1, lat2, lon2):
    """
    Receives two locations - latitude and longitude and returns the haversine distance between these locations
    
    Parameters
    ----------
    any: lat1, lon1, lat2, lon2

    Returns:
    -------
    R: float 
    
    """
    R = 6371.0  # Earth radius in kilometers
    lat1_rad, lon1_rad = np.radians(lat1), np.radians(lon1)
    lat2_rad, lon2_rad = np.radians(lat2), np.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = np.sin(dlat/2.0)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c  # distance in kilometers

