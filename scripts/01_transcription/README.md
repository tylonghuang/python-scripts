# Video Transcription with Python

This repository contains a simple Python command line script that transcribes text from short video files with MoviePy and SpeechRecognition.

> **NOTE**: The script uses the [Google Web Speech API](https://wicg.github.io/speech-api) because of the present default API key which is both convenient and free. Sadly it only supports smaller video files as of now. For bigger files or production use you might want to have a look at [Google Cloud Speech](https://cloud.google.com/speech-to-text). It has a payment model and requires registration which would defeat the purpose of this script.

## Requirements

- [MoviePy](https://pypi.org/project/moviepy) to convert the video files to audio data
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition) which functions as a wrapper for multiple recognition APIs

> **NOTE**: The requirements for this script were already included in the environment.yml.

## Usage:

Command line arguments for the script:

```
$ python transcription.py -h/--help
$ python transcription.py -v/--video-file <file_name>
```

> **NOTE**: The video has to be in the same directory as the script.

Have fun!
