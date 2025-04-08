import pandas as pd
from src.data.ons_loading import filter_ons_csv
from pathlib import Path

def concatenate_ons_csv() -> pd.DataFrame:
    """
    Process all monthly csv file from ONS and return a yearly dataframe with all months data
    
    Parameters
    ----------

    Returns
    -------
    df: pd.DataFrame
        A yearly dataframe from ONS containing only data from PV
    """
   
    import os
    import glob
    
    # Get the root path (3 levels up from this file)
    base_dir = Path(__file__).resolve().parents[3]  # codigos/

    # Build the full path to the datasets folder
    filepath = base_dir / "codigos" / "data" / "raw" / "datasets ons/" 

    processed_dfs = []

    for file in glob.glob(f"{filepath}/*.csv"): #initial solution
        df_cleaned = filter_ons_csv(file)
        processed_dfs.append(df_cleaned)

    #print("Resolved path:", filepath)
    #print("Is directory:", filepath.is_dir())
    #print("Files found:", list(filepath.glob("*.csv")))



    yearly_df = pd.concat(processed_dfs, ignore_index=True)
    yearly_df.sort_values(by=['din_instante'], inplace = True)

    yearly_df = yearly_df.reset_index(drop = True)

    return yearly_df


def get_location_df()-> pd.DataFrame:
    """
    Opens a dataframe with the name of active usines - with disponible location or without mmgd
    
    --------

    Returns
    ------- 
    df: pd.DataFrame
    """
    
    import os
    import glob
    
    # Get the root path (3 levels up from this file)
    base_dir = Path(__file__).resolve().parents[3]  # codigos/

    #filepath = os.getcwd() 
    filepath = base_dir / "codigos" / "data" / "raw" / "localizacao usinas.csv"

    #location_df = pd.read_csv(filepath +'raw/data/localizacao usinas.csv', sep = ";")
    location_df = pd.read_csv(filepath, sep =";")
    return location_df