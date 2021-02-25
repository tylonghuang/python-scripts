# JSON/CSV file converter with Python

This repository contains two simple Python scripts that convert either CSV files to JSON files or vice versa. 

> **NOTE**: The script of your choice depends on if you want a more compact CSV file or a more versatile JSON file.

## Requirements

- [pandas](https://pypi.org/project/pandas/) to easily create CSV files from JSON data

> **NOTE**: Using pandas this way kind of only works from json2csv but not the other way around.

## Usage:

Command line arguments for csv2json:
```
$ python csv2json.py -h/--help
$ python csv2json.py -f/--csv-file <file_name> 
```
Command line arguments for json2csv:
```
$ python json2csv.py -h/--help
$ python json2csv.py -f/--json-file <file_name>
```

> **NOTE**: The file has to be in the same directory as the script. Provided sample files were randomly generated.

Have fun!
