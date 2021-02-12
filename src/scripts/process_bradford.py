# Imports
from pathlib import Path
import numpy as np


# Constants
raw_folder = Path('./data/raw/')

accident = raw_folder / "Road Safety Data - Accidents 2019.csv"
casual = raw_folder / "Road Safety Data - Casualties 2019.csv"
vehicles = raw_folder / "Road Safety Data - Vehicles 2019.csv"


# Process the data
data_acc = np.genfromtxt(accident, dtype=None,
                         delimiter=',', names=True, encoding='utf-8-sig')

data_cas = np.genfromtxt(casual, dtype=None,
                         delimiter=',', names=True, encoding='utf-8-sig')

data_veh = np.genfromtxt(vehicles, dtype=None,
                         delimiter=',', names=True, encoding='utf-8-sig')

brad_acc_mask = data_acc["Local_Authority_District"] == 200
brad_acc = data_acc[brad_acc_mask]

print(brad_acc)
