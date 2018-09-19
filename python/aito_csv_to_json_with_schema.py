import pandas as pd
import json
import os
import pprint
import json

print("Convert all csv file in a folder into json, returns aito schema accordingly")
# input_folder_path = input("Input Folder Path")
# output_folder_path = input("Output Folder Path")

input_folder_path = "CsvFiles"
output_folder_path = "JsonFiles"


var_type = ["string", "integer", "number", "boolean", "decimal"]
aito_var_type = ["String", "Int", "Decimal", "Boolean", "Decimal"]


all_tables = {}
all_tables_schema = {}
all_tables_data = {}

for file_name in os.listdir(input_folder_path):
    # print("File name", file_name)
    all_tables[file_name[:-4]] = pd.read_csv(input_folder_path + "/" + file_name)


print(all_tables.keys())

for key in all_tables.keys():
    table_df = all_tables[key]
    all_tables_schema[key] = pd.io.json.build_table_schema(table_df, index = False)['fields']
    all_tables_data[key] = table_df.to_json(orient = "records")


schema = ""
schema += "{\"tables\":["

keys = list(all_tables.keys())
for i in range(len(keys)):
    key = keys[i]
    # print(key)
    table_schema = all_tables_schema[key]

    table_schema_json_string = "["
    for j in range(len(table_schema)):
        table_schema_json_string += "{ \"column\":" + "\"" + table_schema[j]['name'] + "\"" + ","
        table_schema_json_string += "\"type\": " + "\"" + aito_var_type[var_type.index(table_schema[j]['type'])] + "\"" + "}"
        if j != len(table_schema) - 1:
            table_schema_json_string += ","
    table_schema_json_string += "]"
    # print(table_schema_json_string)

    ###
    # add table
    # add table name
    schema += "{ \"table\": " + "\"" + key + "\"" + ","
    # add columns schema
    schema += "\"columns\": "
    schema += table_schema_json_string
    schema += "}"
    if i != (len(keys) - 1):
        schema += ","
    # print(schema)
schema += "]}"


with open(output_folder_path + "/schema.json", 'w') as outfile:
    parsed = json.loads(schema)
    print(json.dumps(parsed, indent=4))
    json.dump(parsed, outfile)


for key in all_tables.keys():
    with open(output_folder_path + "/" + key + ".json", 'w') as outfile:
        parsed = json.loads(all_tables_data[key])
        json.dump(parsed, outfile)