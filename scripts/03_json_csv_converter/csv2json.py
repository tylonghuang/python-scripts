# Necessary imports
import csv
import json
import argparse

# Define command line argument(s)
parser = argparse.ArgumentParser(description="Convert a csv file to a json file")
parser.add_argument("-f", "--csv-file", type=str, metavar="", required=True, 
 help="name of the file (e.g. data.csv)")
args = parser.parse_args()

# Load csv file
with open(args.csv_file) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Write to json file
with open('output.json', 'w') as f:
    json.dump(rows, f)
