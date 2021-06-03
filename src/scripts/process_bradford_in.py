# === Read the data
DATA = {}

DATA['accident'] = pd.read_csv(PATH['raw_accident'], dtype={
                               0: 'string', 31: 'string'}, encoding='utf-8-sig', index_col=False)

DATA['casual'] = pd.read_csv(PATH['raw_casual'], dtype={
                             0: 'string'}, encoding='utf-8-sig', index_col=False)

DATA['vehicles'] = pd.read_csv(PATH['raw_vehicles'], dtype={
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
DATA['brad_accident'].to_csv(PATH['accident'], index=False)
DATA['brad_casual'].to_csv(PATH['casual'], index=False)
DATA['brad_vehicles'].to_csv(PATH['vehicles'], index=False)
