import requests

url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=ta"

payload = "[\n\t{\"Text\":\"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum\"},\n\t{\"Text\":\"ஹலோ\"}\n]"
headers = {
  'Ocp-Apim-Subscription-Key': '79658f3fc6614494bbc6d6e9bc66caba',
  'Content-Type': 'application/json',
  'Ocp-Apim-Subscription-Region': 'centralindia',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
