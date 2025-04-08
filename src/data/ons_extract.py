import pandas as pd
from src.data.ons_transform import get_location_df

def get_active_usines(df: pd.DataFrame) -> pd.DataFrame:
    """
    Receives a dataframe - supposed to use the yearly dataframe - and returns the dataframe with location for each usine with disponible location
    
    --------
    Parameters
    df: pd.DataFrame
        A yearly dataframe from ONS containing only data from PV

    Returns
    ------- 
    df: pd.DataFrame
        A yearly dataframe from ONS containing PV only data, geolocated
    """
    location_df = get_location_df()


    mask = df['nom_usina'].isin(location_df['nom_usina'])
    df_one_entry = df[mask].copy()

    df_one_entry = pd.merge(df_one_entry, location_df, how="inner", on="nom_usina")
    return df_one_entry