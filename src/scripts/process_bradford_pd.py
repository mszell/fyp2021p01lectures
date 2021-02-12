# Imports
from pathlib import Path
import pandas as pd


# Constants
PATH = {
    'raw': Path('./data/raw/'),
    'processed': Path('./data/processed/'),
}

PATH['bradford_out'] = PATH['processed'] / 'bradford_all_inner.csv'
PATH['accident'] = PATH['raw'] / "Road Safety Data - Accidents 2019.csv"
PATH['casual'] = PATH['raw'] / "Road Safety Data - Casualties 2019.csv"
PATH['vehicles'] = PATH['raw'] / "Road Safety Data - Vehicles 2019.csv"

# Process the data
DATA = {}

DATA['accident'] = pd.read_csv(PATH['accident'], dtype={
                               0: 'string', 31: 'string'}, encoding='utf-8-sig')

DATA['casual'] = pd.read_csv(PATH['casual'], dtype={
                             0: 'string'}, encoding='utf-8-sig')

DATA['vehicles'] = pd.read_csv(PATH['vehicles'], dtype={
                               0: 'string'}, encoding='utf-8-sig')


# Merge data with inner join
DATA['acc_bradford'] = DATA['accident'][DATA["accident"]
                                        ["Local_Authority_(District)"] == 200]

tmp_inner = pd.merge(DATA['acc_bradford'], DATA['casual'], how="inner", on=[
    "Accident_Index", "Accident_Index"])

tmp_inner = pd.merge(tmp_inner, DATA['vehicles'], how="inner", on=[
    "Accident_Index", "Accident_Index"])

# Save all the processed data
tmp_inner.to_csv(PATH['bradford_out'])
