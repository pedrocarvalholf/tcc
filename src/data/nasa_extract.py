import pandas as pd 
import os
import glob
from src.data.nasa_transform import filter_nasa_csv

def concatenate_nasa_csv_streamed(output_path: str = "data/processed/nasa_grid_data.parquet"):
    """
    Processes and streams each CSV file from NASA Power API into a Parquet file on disk.

    Parameters
    ----------
    output_path : str
        File path to save the concatenated DataFrame.

    Returns
    -------
    None
    """
    filepath = os.getcwd() + 'data/raw/output_brazil_grid/'
    all_files = glob.glob(f"{filepath}/*.csv")

    # Delete old output if exists
    if os.path.exists(output_path):
        os.remove(output_path)

    for i, file in enumerate(all_files):
        df_cleaned = filter_nasa_csv(file)
        
        df_cleaned.to_parquet(
            output_path, 
            engine="fastparquet",  # or "pyarrow"
            compression="snappy",
            index=False,
            append=(i != 0),  # Append after the first file
        )
        print(f"[{i+1}/{len(all_files)}] Written {file}")

    print("✅ All files streamed to", output_path)
