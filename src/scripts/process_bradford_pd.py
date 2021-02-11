# Imports
from pathlib import Path
import pandas as pd


# Constants
raw_folder = Path('./data/raw/')
pross_folder = Path('./data/processed/')
pross_out = "bradford_all_inner.csv"

accident = raw_folder / "Road Safety Data - Accidents 2019.csv"
casual = raw_folder / "Road Safety Data - Casualties 2019.csv"
vehicles = raw_folder / "Road Safety Data - Vehicles 2019.csv"


# Process the data
data_acc = pd.read_csv(
    accident, dtype={0: 'string', 31: 'string'}, encoding='utf-8-sig')
data_cas = pd.read_csv(casual, dtype={0: 'string'}, encoding='utf-8-sig')
data_veh = pd.read_csv(vehicles, dtype={0: 'string'}, encoding='utf-8-sig')


# Merge data with inner join
brad_acc = data_acc[data_acc["Local_Authority_(District)"] == 200]

data_inner = pd.merge(brad_acc, data_cas, how="inner", on=[
                      "Accident_Index", "Accident_Index"])

data_inner = pd.merge(data_inner, data_veh, how="inner", on=[
                      "Accident_Index", "Accident_Index"])


# Save all the processed data
data_inner.to_csv(pross_folder / pross_out)
