# e-read-Native

## Description
 e-ReadNative aims to read and extract text from a pdf , translate it to the user’s preferred language using azure's cognitive service translation api and text to speech api in order to listen to the text in form of audio

 ## Prerrequisites
 - Azure translate and text to speech api
 - python3 & pip3 installed

 ## How to use
 - Open ```env.ini``` and add your microsoft's azure cognitive services keys and region
 - change port number to your desired number in server.py ```app.run(host='0.0.0.0',port=80)``` if faced any restrictions
 - ```pip3 install req.txt```
 - ```python3 server.py```
 - open ```http://localhost:desired-port-number```  on your browser
 - choose a target language from the dropdown
 - upload a pdf file
 - wait for the response and you will find the translated text and audio for the same.

 # Note:
 - This project takes only the first page of pdf and converts it inorder to minimise the api utilization.
 - This can be expanded to convert the pdf as a whole and also support other file formats
