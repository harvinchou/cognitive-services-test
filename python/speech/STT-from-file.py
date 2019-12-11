import azure.cognitiveservices.speech as speechsdk
import time
import wave
import sys
import os

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "fa44075c2edb486e9c932ca29e6807b2", "eastasia"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)


def speech_recognize_continuous_from_file(audio_filename):
    """performs continuous speech recognition with input from an audio file"""
    # <SpeechContinuousRecognitionWithFile>
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.endpoint_id = "fa375b5b-3d62-45fa-882e-b1dbc4394d8d"

    audio_config = speechsdk.audio.AudioConfig(filename=audio_filename)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # write recognized text to a file (create a new file)
    filename, file_extension = os.path.splitext(os.path.basename(audio_filename))
    recognized_text_file = "text/" + filename + ".txt"
    open(recognized_text_file, 'w').close()

    done = False

    def stop_cb(evt):
        """callback that stops continuous recognition upon receiving an event `evt`"""
        #print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    def recognized_cb(evt):
        recognized_text = evt.result.text.strip()
        if recognized_text:
            print(recognized_text)
            with open("text/" + filename + ".txt", 'a', encoding="utf-8") as fa:
                fa.writelines(f"{recognized_text}\n")

    # Connect callbacks to the events fired by the speech recognizer
    #speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))
    #speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.recognized.connect(recognized_cb)
    #speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    #speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    #speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)    

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.1)
        #continue
    # </SpeechContinuousRecognitionWithFile>


if __name__ == "__main__":
    # USAGE: python STT-from-file.py audio_filename
    if len(sys.argv) > 1:
        # Give an audio file.
        speech_recognize_continuous_from_file(sys.argv[1])
    else:
        print("USAGE: python STT-from-file.py audio_filename")