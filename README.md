# What is this?

A repository containing a set of python scripts that I find pretty helpful/interesting.

> **NOTE**: There are not that many scripts present as of now, but there will be plenty added over time.

## Contents

- [**01_transcription**](scripts/01_transcription): Transcribes text from short video files
- [**02_audio_listener**](scripts/02_audio_listener): Writes recognized microphone audio into text file
- [**03_json_csv_converter**](scripts/03_json_csv_converter): Converts CSV/JSON files

## Requirements

- [conda](https://docs.conda.io/en/latest/)

> **NOTE**: If you are unsure whether to get Anaconda or Miniconda read through [this](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda).

After making sure conda is installed on your device navigate to this directory and run:
```
$ conda env create --file environment.yml
```
to create an environment with the required packages. Wait until they are installed and then run:
```
$ conda activate py-scripts
```
to activate the environment. In case you change something and want to export it, run:
```
$ conda env export | cut -f -2 -d "=" | grep -v "prefix" > environment.yml
```
to get your new environment file. Either way you are ready to go.

## Usage:

Check each individual [script](scripts) for more information/instructions. 

Thanks for reading and have fun!

___

_For any inquiries or questions contact me under: lungnguyenhung@gmail.com_
