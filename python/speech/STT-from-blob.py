#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

from typing import List
from urllib.parse import urlparse

import json
import logging
import os
import sys
import requests
import time
import swagger_client as cris_client


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(message)s")

# Your subscription key and region for the speech service
#SUBSCRIPTION_KEY = "ca306df375254104a0ee9914aba14039"
SUBSCRIPTION_KEY = "fa44075c2edb486e9c932ca29e6807b2"
SERVICE_REGION = "eastasia"

NAME = "Simple transcription"
DESCRIPTION = "Simple transcription description"

LOCALE = "en-US"
#RECORDINGS_BLOB_URI = "<Your SAS Uri to the recording>"

# Set subscription information when doing transcription with custom models
ADAPTED_ACOUSTIC_ID = "fa375b5b-3d62-45fa-882e-b1dbc4394d8d"  # guid of a custom acoustic model
ADAPTED_LANGUAGE_ID = "c8fedff7-37ee-48d7-a9cf-c0cbba5a6381"  # guid of a custom language model


def transcribe(blob_uri: str):
    logging.info("Starting transcription client...")

    # configure API key authorization: subscription_key
    configuration = cris_client.Configuration()
    configuration.api_key['Ocp-Apim-Subscription-Key'] = SUBSCRIPTION_KEY
    configuration.host = "https://{}.cris.ai".format(SERVICE_REGION)

    # create the client object and authenticate
    client = cris_client.ApiClient(configuration)

    # create an instance of the transcription api class
    transcription_api = cris_client.CustomSpeechTranscriptionsApi(api_client=client)

    # Use base models for transcription. Comment this block if you are using a custom model.
    # Note: you can specify additional transcription properties by passing a
    # dictionary in the properties parameter. See
    # https://docs.microsoft.com/azure/cognitive-services/speech-service/batch-transcription
    # for supported parameters.
    
    transcription_definition = cris_client.TranscriptionDefinition(
        name=NAME, description=DESCRIPTION, locale=LOCALE, recordings_url=blob_uri, 
        models=[cris_client.ModelIdentity(ADAPTED_ACOUSTIC_ID), cris_client.ModelIdentity(ADAPTED_LANGUAGE_ID)]
    )
    

    # Uncomment this block to use custom models for transcription.
    # Model information (ADAPTED_ACOUSTIC_ID and ADAPTED_LANGUAGE_ID) must be set above.
    '''
    if ADAPTED_ACOUSTIC_ID is None or ADAPTED_LANGUAGE_ID is None:
        logging.info("Custom model ids must be set to when using custom models")
    
    transcription_definition = cris_client.TranscriptionDefinition(
        name=NAME, description=DESCRIPTION, locale=LOCALE, recordings_url=blob_uri,
        models=[cris_client.ModelIdentity(ADAPTED_ACOUSTIC_ID), cris_client.ModelIdentity(ADAPTED_LANGUAGE_ID)]
    )
    '''        

    data, status, headers = transcription_api.create_transcription_with_http_info(transcription_definition)

    # extract transcription location from the headers
    transcription_location: str = headers["location"]

    # get the transcription Id from the location URI
    created_transcription: str = transcription_location.split('/')[-1]

    logging.info("Created new transcription with id {}".format(created_transcription))

    #logging.info("Checking status.")

    completed = False

    while not completed:
        running, not_started = 0, 0

        # get all transcriptions for the user
        transcriptions: List[cris_client.Transcription] = transcription_api.get_transcriptions()

        # for each transcription in the list we check the status
        for transcription in transcriptions:
            if transcription.status in ("Failed", "Succeeded"):
                # we check to see if it was the transcription we created from this client
                if created_transcription != transcription.id:
                    continue

                completed = True

                if transcription.status == "Succeeded":
                    results_uri = transcription.results_urls["channel_0"]
                    results = requests.get(results_uri)
                    logging.info("Transcription succeeded.")
                    #logging.info(results.content.decode("utf-8"))
                    filename, file_extension = os.path.splitext(os.path.basename(urlparse(blob_uri).path))
                    logging.info("Output file: " + filename + ".json")
                    flush_json(results.json(), filename + ".json")
                else:
                    logging.info("Transcription failed :{}.".format(transcription.status_message))
                    break
            elif transcription.status == "Running":
                running += 1
            elif transcription.status == "NotStarted":
                not_started += 1

        logging.info("Transcriptions status: "
                "completed (this transcription): {}, {} running, {} not started yet".format(
                    completed, running, not_started))
    
        # wait for 5 seconds
        time.sleep(5)

    #input("Press any key...")

def flush_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    # USAGE: python STT-from-blob.py audio_file_uri
    if len(sys.argv) > 1:
        transcribe(sys.argv[1])
    else:
        print("USAGE: python STT-from-blob.py audio_file_uri")
        #transcribe("https://jccsstorage.blob.core.windows.net/audio/TxVoice_20191126074220.wav")
        #transcribe("https://jccsstorage.blob.core.windows.net/audio/RxVoice_20191202033155.wav")
        #transcribe("https://jccsstorage.blob.core.windows.net/audio/RxVoice_repeat.wav")
        #transcribe("https://jccsstorage.blob.core.windows.net/audio/TxVoice_20191126074220-short.wav")
