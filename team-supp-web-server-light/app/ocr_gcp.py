from base64 import b64encode
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'

def execute_ocr_gcp(img_file):
    img_requests =[]
    
    with open(img_file, 'rb') as image:
      ctxt = b64encode(image.read()).decode('utf-8')
      img_requests.append({
                    'image':{'content': ctxt},
                    'features':{'type': 'DOCUMENT_TEXT_DETECTION'},
                    'imageContext':{'languageHints':'ja'}
            })

    api_key = 'AIzaSyC3Ay3_2MkROMcPMYRPCTqo4JqAXot3WsE'
    response = requests.post(ENDPOINT_URL,
                             data=json.dumps({"requests": img_requests}).encode(),
                             params={'key': api_key},
                             headers={'Content-Type': 'application/json'})

#    for idx, resp in enumerate(response.json()['responses']):
#        print(json.dumps(resp, indent=2))
    
#    print(response)
    
    return response.json()["responses"][0]["textAnnotations"][0]["description"]
