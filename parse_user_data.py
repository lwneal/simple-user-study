import os
import json
import pandas as pd

INPUT_DATA_DIR = 'user_data/'
OUTPUT_FILENAME = 'collected_data.csv'

# Collect all the .json data files written by server.py:save_request
entries = {}
print('Reading user data from {}'.format(INPUT_DATA_DIR))

# Load each .json file and add it to entries, sorted by user_id
for filename in sorted(os.listdir(INPUT_DATA_DIR)):
    if not filename.endswith('.json'):
        continue
    text = open(os.path.join(INPUT_DATA_DIR, filename)).read()
    data = json.loads(text)
    user_id = data['user_id']
    if user_id not in entries:
        entries[user_id] = {}
    entries[user_id].update(data)

# Convert the dictionary to a Pandas dataframe
data_rows = [i for i in entries.values()]
df = pd.DataFrame(data_rows)

# Put user_id into the leftmost column so it looks nice
df = df[['user_id'] + df.columns.tolist()]

# Write the dataframe as a CSV file
print('Writing user data to CSV file: {}'.format(OUTPUT_FILENAME))
df.to_csv(OUTPUT_FILENAME)
