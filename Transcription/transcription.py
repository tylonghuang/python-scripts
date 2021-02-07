# Necessary imports
import moviepy.editor as mp
import speech_recognition as sr
import argparse

# Define command line argument(s)
parser = argparse.ArgumentParser(description="Transcribe text from a video file")
parser.add_argument("-v", "--video-file", type=str, metavar="", required=True,
 help="name of the video file e.g. video.mp4")
args = parser.parse_args()

# Convert video file to textual data
def video_to_text(file_name):
    video_input = mp.VideoFileClip(r""+file_name)
    stripped_filename = file_name.split(".", maxsplit=1)[0] + ".wav"
    audio_output = video_input.audio.write_audiofile(r""+stripped_filename)
    r = sr.Recognizer()
    audio_file = sr.AudioFile(stripped_filename)
    with audio_file as source:
        # Uncomment if there is a lot of background noise:
        # r.adjust_for_ambient_noise(source)
        # You might change the starting point and duration of the audio data:
        # audio_data = r.record(source, offset=x, duration=y)
        audio_data = r.record(source)
    try:
        # Make changes HERE if you want to use a different API (i.e. Google Cloud Speech)
        # Language codes: https://cloud.google.com/speech-to-text/docs/languages
        # Default value is English
        text_data = r.recognize_google(audio_data, language="en-US")
        return text_data
    except sr.UnknownValueError:
        print("Did not understand the audio. Please try again")
    except sr.RequestError as e:
        print("Requesting results from Google Speech Recognition is not possible atm; {0}"
        .format(e))
          
# Write textual data to a txt file
def write_to_file(text):
    with open("transcription.txt", "w") as f:
        f.write("Text from the video: " + text)
    return f

if __name__ == "__main__":
    text = video_to_text(args.video_file)
    write_to_file(text)
    print("Successful transcription!")
