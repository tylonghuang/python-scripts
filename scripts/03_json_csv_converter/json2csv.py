# Necessary imports
import pandas as pd
import argparse

# Define command line argument(s)
parser = argparse.ArgumentParser(description="Convert a json file to a csv file")
parser.add_argument("-f", "--json-file", type=str, metavar="", required=True, 
 help="name of the file (e.g. data.json)")
args = parser.parse_args()

# Load json and write to csv with pandas
df = pd.read_json(r'' + args.json_file)
df.to_csv(r'output.csv')
