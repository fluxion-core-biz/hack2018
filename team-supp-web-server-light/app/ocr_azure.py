import requests
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle
import cv2
from PIL import Image
from io import BytesIO

subscription_key = "b4cbcd88f0c04ed785e9173d062793ab"
assert subscription_key

vision_base_url = "https://japanwest.api.cognitive.microsoft.com/vision/v2.0/"
ocr_url = vision_base_url + "ocr"

def crop_center(pil_img, crop_width, crop_height):
  img_width, img_height = pil_img.size
  return pil_img.crop( ( (img_width  - crop_width ) // 2,
                         (img_height - crop_height) // 2,
                         (img_width  + crop_width ) // 2,
                         (img_height + crop_height) // 2))

def crop(image_path):
  # Read the image into a byte array
  input_data = Image.open(image_path + '.jpg')
#  input_data = Image.open(image_path)

  img_width, img_height = input_data.size

  image_data = crop_center(input_data, img_width, 1400).save(image_path + '_croped.jpg', quality=95)


def ocr(image_path):
  image_data = open(image_path + '_binimage.jpg', "rb").read()

  headers = {'Ocp-Apim-Subscription-Key': subscription_key,
             'Content-Type': 'application/octet-stream'}
  params  = {'language': 'ja', 'detectOrientation': 'true'}
  response = requests.post(ocr_url, headers=headers, params=params, data=image_data)
  response.raise_for_status()

  analysis = response.json()

  line_infos = [region["lines"] for region in analysis["regions"]]
  word_infos = []
  for line in line_infos:
    for word_metadata in line:
      for word_info in word_metadata["words"]:
        word_infos.append(word_info["text"])

  return ''.join(word_infos)

def binImager(image_path):
  t = 140

  img = cv2.imread(image_path + '_croped.jpg',)

  gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

  th1 = gray.copy()

  th1[gray < t] = 0
  th1[gray >= t] = 255

  cv2.imwrite(image_path + '_binimage.jpg', th1)


def execute_ocr_azure(image_path):
  crop(image_path)
  binImager(image_path)
  analysis = ocr(image_path)

  print(analysis)

  return analysis

# exec('C:\\DSC_0873')

