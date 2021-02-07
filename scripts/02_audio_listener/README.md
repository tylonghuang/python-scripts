# Microphone Audio Listener with Python

This repository contains a simple Python script that tries to recognize your microphone audio through the Google Web Speech API. The recognized audio will then be logged into a textfile with a timestamp. As of now there is very little logic included (e.g. quitting when you say "stop") but the possibilities are limitless so feel free to extend it yourself.

> **NOTE**: The script uses the [Google Web Speech API](https://wicg.github.io/speech-api) because of the present default API key which is both convenient and free but only suitable for smaller personal projects. For bigger projects or production use you might want to have a look at [Google Cloud Speech](https://cloud.google.com/speech-to-text). It has a payment model and requires registration which would defeat the purpose of this script.

## Requirements

- [PyAudio](https://pypi.org/project/PyAudio/) to access your microphone with SpeechRecognition
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition) which functions as a wrapper for multiple recognition APIs

> **NOTE**: The requirements for this script were already included in the environment.yml.

## Usage:

Command line input:
```
$ python audio_listener.py
```
Sample output:
```
Say something!
I did not catch that one!
You said hello
You said I like Google
You said stop
Stopping recording...
```
> **NOTE**: Check the output.txt for more.

Have fun!
___

_For any inquiries or questions contact me under: lungnguyenhung@gmail.com_

