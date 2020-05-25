import requests,json,configparser,time
import azure.cognitiveservices.speech as speechsdk
from xml.etree import ElementTree

config = configparser.ConfigParser()
config.read('env.ini')
speech_key, service_region = config['general']['speech_key'], config['general']['speech_region']
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

tts_lang = {"hi":"hi-IN","ta":"ta-IN","te":"te-IN","it":"it-IT","ja":"ja-JP"}
tts_voice = {"hi":"hi-IN-Kalpana-Apollo","ta":"ta-IN-Valluvar","te":"te-IN-Chitra","it":"it-IT-Cosimo-Apollo","ja":"ja-JP-Ayumi-Apollo"}
headers = {
    'Ocp-Apim-Subscription-Key': config['general']['translate_key'],
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Region': config['general']['translate_region']
  }
def call_translate(text,tgt_lang):
  translate_url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to="+tgt_lang
  payload = [{"Text":text}]
  response = requests.request("POST", translate_url, headers=headers, data = json.dumps(payload))
  filename = call_tts(json.loads(response.text)[0]['translations'][0]['text'],tgt_lang)
  resp = json.loads(response.text)
  resp[0]['filename'] = filename
  return resp

def call_tts(text,tgt_lang):
  synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
  xml_body = ElementTree.Element('speak', version='1.0')
  xml_body.set("xmlns", 'https://www.w3.org/2001/10/synthesis')
  xml_body.set("xml:lang", tts_lang[tgt_lang])
  voice = ElementTree.SubElement(xml_body, 'voice')
  voice.set("name", tts_voice[tgt_lang])
  voice.text = str(text)
  body = ElementTree.tostring(xml_body)
  result = synthesizer.speak_ssml(body.decode("utf-8"))
  stream = speechsdk.AudioDataStream(result)
  audio_filename = str(time.time())+".wav"
  stream.save_to_wav_file("static/"+audio_filename)
  print("Audio file saved to: "+audio_filename,"lang: "+tgt_lang)
  return audio_filename