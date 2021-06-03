# === Imports
from pathlib import Path
import pandas as pd


# === Set Constants
PATH = {
    'raw': Path('./data/raw/'),
    'processed': Path('./data/processed/'),
    'interim': Path('./data/interim/'),
}

PATH['accident'] = PATH['raw'] / "Road Safety Data - Accidents 2019.csv"
PATH['casual'] = PATH['raw'] / "Road Safety Data - Casualties 2019.csv"
PATH['vehicles'] = PATH['raw'] / "Road Safety Data - Vehicles 2019.csv"


# === Read the data
DATA = {}

DATA['accident'] = pd.read_csv(PATH['accident'], dtype={
                               0: 'string', 31: 'string'}, encoding='utf-8-sig', index_col=False)

DATA['casual'] = pd.read_csv(PATH['casual'], dtype={
                             0: 'string'}, encoding='utf-8-sig', index_col=False)

DATA['vehicles'] = pd.read_csv(PATH['vehicles'], dtype={
                               0: 'string'}, encoding='utf-8-sig', index_col=False)


# === Process it
# Get all bradford accidents as we know they're in local district 200
DATA['brad_accident'] = DATA['accident'][DATA['accident']
                                         ['Local_Authority_(District)'] == 200]

# Get the accident indexes from brad_accident
accident_index = DATA['brad_accident']['Accident_Index']

# Use the index to find all matching rows in casualties and vehicles
brad_cass_mask = DATA['casual']['Accident_Index'].isin(accident_index)
brad_vehi_mask = DATA['vehicles']['Accident_Index'].isin(accident_index)

DATA['brad_casual'] = DATA['casual'][brad_cass_mask]
DATA['brad_vehicles'] = DATA['vehicles'][brad_vehi_mask]


# === Save it
# Don't let pandas add an index
DATA['brad_accident'].to_csv(PATH['interim'] / 'bradford_accidents.csv', index=False)
DATA['brad_casual'].to_csv(PATH['interim'] / 'bradford_casualties.csv', index=False)
DATA['brad_vehicles'].to_csv(PATH['interim'] / 'bradford_vehicles.csv', index=False)


# === Old code
# tmp_inner = pd.merge(DATA['acc_bradford'], DATA['casual'], how="inner", on=[
#     "Accident_Index", "Accident_Index"])

# tmp_inner = pd.merge(tmp_inner, DATA['vehicles'], how="inner", on=[
#     "Accident_Index", "Accident_Index"])
