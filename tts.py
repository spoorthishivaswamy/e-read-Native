import azure.cognitiveservices.speech as speechsdk
from xml.etree import ElementTree

# Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
speech_key, service_region = "1553bca817174d4592e527c8af58d4e2", "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# # Creates an audio configuration that points to an audio file.
# # Replace with your own audio filename.
# audio_filename = "helloworld.wav"
# audio_output = speechsdk.audio.AudioOutputConfig(filename=audio_filename)

# # # Creates a synthesizer with the given settings
# speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output)

# # # Synthesizes the text to speech.
# # # Replace with your own text.
# text = "你好"
# result = speech_synthesizer.speak_text(text)

# # Checks result.
# if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print("Speech synthesized to [{}] for text [{}]".format(audio_filename, text))
# elif result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = result.cancellation_details
#     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         if cancellation_details.error_details:
#             print("Error details: {}".format(cancellation_details.error_details))
#     print("Did you update the subscription info?")


def xmlaudio():
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    xml_body = ElementTree.Element('speak', version='1.0')
    # xml_body.set('{https://www.w3.org/2001/10/synthesis}lang', 'en-US')
    xml_body.set("xmlns", 'https://www.w3.org/2001/10/synthesis')
    xml_body.set("xml:lang", 'hi-IN')

    voice = ElementTree.SubElement(xml_body, 'voice')
    voice.set("name", 'hi-IN-Kalpana-Apollo')
    voice.text = str("हिंदी")
    body = ElementTree.tostring(xml_body)
    # f = open("sample.xml","w")
    # f.write(str(body))



    # ssml_string = open("sample.xml", "r",encoding="UTF-8").read()
    # print(ssml_string)
    result = synthesizer.speak_ssml_async(body.decode("utf-8")).get()

    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("voice.wav")