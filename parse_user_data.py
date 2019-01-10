import os
import json
import pandas as pd

INPUT_DATA_DIR = 'user_data/'
OUTPUT_FILENAME = 'collected_data.csv'

# Collect all endpoints per user_id
entries = {}
for filename in sorted(os.listdir(INPUT_DATA_DIR)):
    data = json.loads(open(os.path.join(INPUT_DATA_DIR, filename)).read())
    user_id = data['user_id']
    if user_id not in entries:
        entries[user_id] = {}
    entries[user_id].update(data)


# Convert to a CSV file
data_rows = [i for i in entries.values()]
pd.DataFrame(data_rows).to_csv(OUTPUT_FILENAME)
