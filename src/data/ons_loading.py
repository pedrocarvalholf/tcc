import pandas as pd

def filter_ons_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process a monthly csv file from ONS and return a dataframe containing only data from photovoltaic sources
    
    Parameters
    ----------
    df: .csv file
        A CSV file from ONS containing power generation for a complete month
    
    Returns
    -------
    df: pd.dataframe 
        A cleaned monthly dataframe file from ONS containing only data from PV
    
    
    """
    import os

    df = pd.read_csv(df, sep = ";")   
    df = df[df['nom_tipousina'] == 'FOTOVOLTAICA']

    return df


