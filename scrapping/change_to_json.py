import pandas as pd
import json

# Read the CSV file into a dataframe
df = pd.read_csv("180257R_new.csv")

bulk_json = []


for index, row in df.iterrows():
    # Create a JSON object with the desired format
    json_object = {}
    json_object.update(row.to_dict())
    bulk_json.append(json_object)

with open("data.json", "w") as f:
    json.dump(bulk_json, f)
