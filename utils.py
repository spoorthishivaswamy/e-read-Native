import requests,json
import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = "1553bca817174d4592e527c8af58d4e2", "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

headers = {
    'Ocp-Apim-Subscription-Key': '79658f3fc6614494bbc6d6e9bc66caba',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Region': 'centralindia'
  }
def call_translate(text,tgt_lang):
  translate_url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to="+tgt_lang
  payload = [{"Text":text}]
  response = requests.request("POST", translate_url, headers=headers, data = json.dumps(payload))
  filename = call_tts(json.loads(response.text)[0]['translations'][0]['text'])
  resp = json.loads(response.text)
  resp[0]['filename'] = filename
  return resp

def call_tts(text):
  audio_filename = "voice.wav"
  audio_output = speechsdk.audio.AudioOutputConfig(filename=audio_filename)
  speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output)
  text = text
  result = speech_synthesizer.speak_text_async(text).get()

  # Checks result.
  if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
      print("Speech synthesized to [{}] for text [{}]".format(audio_filename, text))
      return audio_filename
  elif result.reason == speechsdk.ResultReason.Canceled:
      cancellation_details = result.cancellation_details
      print("Speech synthesis canceled: {}".format(cancellation_details.reason))
      return "Error"
      if cancellation_details.reason == speechsdk.CancellationReason.Error:
          if cancellation_details.error_details:
              print("Error details: {}".format(cancellation_details.error_details))
              return "Error"
      print("Did you update the subscription info?")