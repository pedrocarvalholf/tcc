from src.data.ons_extract import get_active_usines
from src.data.ons_transform import concatenate_ons_csv

#df_yearly_usines = concatenate_ons_csv()
#df_active_usines = get_active_usines(df_yearly_usines)
#df_active_usines.head()

#criar datetime como din_instante no dataframe da nasa
#atualizar csv loclaizcao usinas
#df_one_entry
#closest lat.long(nasa) no df_one_entry
#passar lat long do df one entru pro df active usines
#passar parametros NASA pro df active usines    

import pandas as pd
df_test = pd.read_parquet("nasa_grid_data.parquet", engine = 'pyarrow')