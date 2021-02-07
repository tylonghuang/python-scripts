# Necessary imports
import os
from time import sleep, localtime, strftime
from speech_recognition import Microphone, Recognizer ,UnknownValueError, RequestError

# Write/Append local timestamp and recognized text to a txt file
def write_to_file(res):
    time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    with open("output.txt", "a") as f:
        print("[" + time + "]: " + res, file=f)

# Function that is called from the background thread
def callback(recognizer, audio):
    try:
        # Make changes HERE if you want to use a different API (i.e. Google Cloud Speech)
        res = recognizer.recognize_google(audio)
        print("You said " + res)
        write_to_file(res)
        # Stopping recording when you say "stop"
        if("stop" in res):
            print("Stopping recording...")
            os._exit(1)
    except UnknownValueError:
        print("I did not catch that one!")
    except RequestError as e:
        print("Requests are not possible right now.; {0}".format(e))

# Function that gets the microphone audio
def listen():
    print("Say something!")
    r = Recognizer()
    m = Microphone()
    with m as src:
        # Deal with ambient noise since microphone output is rather unpredictable
        r.adjust_for_ambient_noise(src)
    # Start listening
    r.listen_in_background(m, callback)
    # Keep listening even though main thread is blocked
    while True: 
        sleep(1)

if __name__ == "__main__":
    listen()
