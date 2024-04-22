import os
import openai
import webbrowser
import base64
import datetime

openai.api_key = 'YOUR-API-KEY-HERE'

prompt = "Office room with fifteen chairs"
image_size = "512x512"

prefix = 'C:/Users/E.Mazarakis/Desktop/DALLE_IMAGES/000.DL_'
task = 'counting'
suffix = '.png'
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_format = "b64_json"
s = "512" if image_size == "512x512" else "1024"




res = openai.Image.create(
        prompt = prompt,
        n = 1,
        size = image_size,
        response_format = output_format
)

#The following code open the image on a web-browser.
for i in range(0, len(res['data'])):
        b64 = res['data'][i]['b64_json']
        filename = f'{prefix}{s}_{task}_{timestamp}{suffix}'
        print('Saving file ' + filename)
        with open(filename, 'wb') as f:
            f.write(base64.urlsafe_b64decode(b64))
      
