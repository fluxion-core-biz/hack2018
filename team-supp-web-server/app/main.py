
from flask import Flask

import MeCab

from flask import request, jsonify
import json
import traceback
from mimetypes import guess_extension
from time import time, sleep
from urllib.request import urlopen, Request
from urllib.parse import quote
import sys
from datetime import datetime


app = Flask(__name__)


"""
"""
def diag_mecab():
  str_input  = "1)【般】ペポタスチンベジル酸塩錠10mg2錠今日は帰宅後すぐ服用【1日2回朝夕に】(14日分)"

  str_report = "MeCab:\n" + \
               ' Input=' + str_input + '\n'

  tagger = MeCab.Tagger( "-Owakati" )
  str_result = tagger.parse( str_input )
  str_report += '-Owakati:\n' + \
                ' Result=' + str_result + '\n'

#  tagger = MeCab.Tagger( "-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd" )
#  str_result = tagger.parse( str_input )
#  str_report += '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd:\n' + \
#                ' Result=' + str_result + '\n'

  print( str_report )
  return str_report


"""
"""
def diag():
  str_report = '<Self diag result>\n'
  str_report += diag_mecab()
  return str_report


"""
"""
def to_html( str_std_out ):
  return "<br />".join( str_std_out.split( "\n" ) )
  
  
"""
"""
@app.route("/")
def hello():
  str_diag_report = diag()
  str_output = "Hello Team-Supp.\n" + \
               "Web Server by uWSGI + NGINX + Flask\n" + \
               str_diag_report
  print( str_output )
  return to_html( str_output )



RPATH_DIR_UPLOADS = './uploads'

# Limit of Upload file length
app.config[ 'MAX_CONTENT_LENGTH' ] = 32 * 1024 * 1024
app.config[ 'RPATH_DIR_UPLOADS' ] = RPATH_DIR_UPLOADS

SET_AVAILABLED_EXT = set( [ 'png', 'jpg', 'gif' ] )

"""
"""
def get_file_ext( filename ):
  if '.' in filename:
    return filename.rsplit( '.', 1 )[ 1 ]
  else:
    return filename

"""
"""
def availabled_file( filename ):
  return '.' in filename and \
    get_file_ext( filename ) in SET_AVAILABLED_EXT

"""
"""
def upload_image( img_file ):
  filename = secure_filename( img_file.filename )
  img_file.save( os.path.join( app.config[ 'RPATH_DIR_UPLOADS' ], filename ) )
  img_url = '/uploads/' + filename
  return;

"""
"""
def execute_ocr():
#TODO: Implement here
#   with open( './dummy_ocr_result.txt' ) as f
#     print( f )
#     return f
  return '''{"orientation":"Up","regions":[{"boundingBox":"397,15,1240,57","lines":[{"boundingBox":"422,15,1215,31","words":[{"boundingBox":"422,20,26,25","text":"個"},{"boundingBox":"454,22,17,18","text":"々"},{"boundingBox":"479,22,24,21","text":"の"},{"boundingBox":"507,21,25,24","text":"処"},{"boundingBox":"539,20,19,26","text":"方"},{"boundingBox":"563,20,25,25","text":"薬"},{"boundingBox":"592,22,22,21","text":"に"},{"boundingBox":"618,25,24,17","text":"つ"},{"boundingBox":"646,25,24,18","text":"い"},{"boundingBox":"673,24,23,20","text":"て"},{"boundingBox":"701,38,6,8","text":"、"},{"boundingBox":"728,22,25,24","text":"後"},{"boundingBox":"756,21,23,25","text":"発"},{"boundingBox":"783,23,22,23","text":"医"},{"boundingBox":"809,21,24,24","text":"薬"},{"boundingBox":"836,22,23,23","text":"品"},{"boundingBox":"877,21,8,24","text":"("},{"boundingBox":"891,20,21,24","text":"ジ"},{"boundingBox":"918,29,20,13","text":"ェ"},{"boundingBox":"944,21,21,24","text":"ネ"},{"boundingBox":"974,22,13,22","text":"リ"},{"boundingBox":"998,27,18,18","text":"ッ"},{"boundingBox":"1025,22,18,23","text":"ク"},{"boundingBox":"1049,22,23,24","text":"医"},{"boundingBox":"1075,20,23,25","text":"薬"},{"boundingBox":"1102,21,22,23","text":"品"},{"boundingBox":"1128,21,7,22","text":")"},{"boundingBox":"1153,25,23,13","text":"へ"},{"boundingBox":"1179,22,22,19","text":"の"},{"boundingBox":"1205,19,23,24","text":"変"},{"boundingBox":"1233,21,21,22","text":"史"},{"boundingBox":"1259,21,20,20","text":"に"},{"boundingBox":"1284,19,21,23","text":"差"},{"boundingBox":"1312,20,17,22","text":"し"},{"boundingBox":"1338,19,19,23","text":"攴"},{"boundingBox":"1362,20,19,21","text":"え"},{"boundingBox":"1386,18,22,22","text":"が"},{"boundingBox":"1413,18,20,22","text":"あ"},{"boundingBox":"1438,18,19,22","text":"る"},{"boundingBox":"1466,18,16,21","text":"と"},{"boundingBox":"1488,17,22,23","text":"判"},{"boundingBox":"1513,17,23,22","text":"断"},{"boundingBox":"1543,16,16,22","text":"し"},{"boundingBox":"1566,16,20,21","text":"た"},{"boundingBox":"1590,16,22,23","text":"場"},{"boundingBox":"1616,15,21,24","text":"合"}]},{"boundingBox":"397,41,1227,31","words":[{"boundingBox":"397,48,22,22","text":"に"},{"boundingBox":"425,48,25,23","text":"は"},{"boundingBox":"452,64,7,8","text":"、"},{"boundingBox":"496,46,7,22","text":"「"},{"boundingBox":"509,47,24,24","text":"変"},{"boundingBox":"538,48,23,24","text":"更"},{"boundingBox":"565,48,23,24","text":"不"},{"boundingBox":"595,48,21,24","text":"可"},{"boundingBox":"620,51,8,21","text":"」"},{"boundingBox":"646,48,25,24","text":"欄"},{"boundingBox":"676,50,21,20","text":"に"},{"boundingBox":"717,46,8,22","text":"「"},{"boundingBox":"732,52,22,16","text":"ノ"},{"boundingBox":"756,52,9,20","text":"」"},{"boundingBox":"784,48,23,23","text":"乂"},{"boundingBox":"812,48,23,22","text":"は"},{"boundingBox":"851,46,9,20","text":"「"},{"boundingBox":"868,51,16,17","text":"x"},{"boundingBox":"891,51,8,20","text":"」"},{"boundingBox":"920,47,17,23","text":"を"},{"boundingBox":"945,48,23,23","text":"記"},{"boundingBox":"972,47,24,24","text":"載"},{"boundingBox":"1001,48,17,22","text":"し"},{"boundingBox":"1024,64,5,7","text":"、"},{"boundingBox":"1064,46,8,20","text":"「"},{"boundingBox":"1076,47,24,24","text":"保"},{"boundingBox":"1103,46,23,24","text":"険"},{"boundingBox":"1130,47,21,22","text":"医"},{"boundingBox":"1155,46,21,23","text":"署"},{"boundingBox":"1183,45,19,24","text":"名"},{"boundingBox":"1208,50,8,19","text":"」"},{"boundingBox":"1232,45,23,23","text":"欄"},{"boundingBox":"1260,47,20,19","text":"に"},{"boundingBox":"1285,45,21,23","text":"署"},{"boundingBox":"1312,44,19,24","text":"名"},{"boundingBox":"1339,46,20,20","text":"乂"},{"boundingBox":"1362,45,23,21","text":"は"},{"boundingBox":"1388,44,22,23","text":"記"},{"boundingBox":"1415,43,19,24","text":"名"},{"boundingBox":"1447,52,5,5","text":"・"},{"boundingBox":"1464,42,22,23","text":"押"},{"boundingBox":"1491,42,20,22","text":"印"},{"boundingBox":"1515,41,21,23","text":"す"},{"boundingBox":"1543,41,18,23","text":"る"},{"boundingBox":"1570,43,16,18","text":"こ"},{"boundingBox":"1595,41,16,22","text":"と"},{"boundingBox":"1617,56,7,8","text":"。"}]}]},{"boundingBox":"416,90,809,37","lines":[{"boundingBox":"416,90,809,37","words":[{"boundingBox":"416,90,42,36","text":"い"},{"boundingBox":"510,90,10,37","text":"【"},{"boundingBox":"526,90,37,36","text":"般"},{"boundingBox":"569,90,10,37","text":"】"},{"boundingBox":"609,94,35,24","text":"べ"},{"boundingBox":"650,91,34,34","text":"ボ"},{"boundingBox":"694,92,26,33","text":"タ"},{"boundingBox":"731,96,32,27","text":"ス"},{"boundingBox":"771,92,32,32","text":"チ"},{"boundingBox":"813,94,29,28","text":"ン"},{"boundingBox":"849,93,34,24","text":"ペ"},{"boundingBox":"890,93,31,29","text":"シ"},{"boundingBox":"928,92,34,30","text":"ル"},{"boundingBox":"965,90,36,35","text":"酸"},{"boundingBox":"1005,90,35,34","text":"塩"},{"boundingBox":"1043,90,36,34","text":"錠"},{"boundingBox":"1093,90,12,30","text":"1"},{"boundingBox":"1127,90,21,30","text":"0"},{"boundingBox":"1161,98,30,20","text":"m"},{"boundingBox":"1205,98,20,26","text":"g"}]}]},{"boundingBox":"1432,87,18,28","lines":[{"boundingBox":"1432,87,18,28","words":[{"boundingBox":"1432,87,18,28","text":"2"}]}]},{"boundingBox":"1610,81,36,34","lines":[{"boundingBox":"1610,81,36,34","words":[{"boundingBox":"1610,81,36,34","text":"錠"}]}]},{"boundingBox":"1780,177,150,34","lines":[{"boundingBox":"1780,177,150,34","words":[{"boundingBox":"1780,180,13,29","text":"1"},{"boundingBox":"1812,180,22,28","text":"4"},{"boundingBox":"1848,180,26,31","text":"日"},{"boundingBox":"1882,179,30,31","text":"分"},{"boundingBox":"1917,177,13,34","text":")"}]}]},{"boundingBox":"181,290,1291,596","lines":[{"boundingBox":"181,851,35,35","words":[{"boundingBox":"181,851,35,35","text":"方"}]},{"boundingBox":"1409,290,58,29","words":[{"boundingBox":"1409,291,19,28","text":"2"},{"boundingBox":"1448,290,19,29","text":"5"}]},{"boundingBox":"1414,341,58,29","words":[{"boundingBox":"1414,342,19,28","text":"2"},{"boundingBox":"1453,341,19,29","text":"5"}]}]},{"boundingBox":"275,625,39,36","lines":[{"boundingBox":"275,625,39,36","words":[{"boundingBox":"275,625,39,36","text":"X"}]}]},{"boundingBox":"411,142,653,626","lines":[{"boundingBox":"487,142,397,37","words":[{"boundingBox":"487,142,36,35","text":"今"},{"boundingBox":"533,146,26,30","text":"日"},{"boundingBox":"572,144,35,32","text":"は"},{"boundingBox":"610,144,36,34","text":"帰"},{"boundingBox":"650,144,37,34","text":"宅"},{"boundingBox":"692,144,36,35","text":"後"},{"boundingBox":"731,143,36,35","text":"す"},{"boundingBox":"778,144,26,33","text":"ぐ"},{"boundingBox":"812,144,36,34","text":"服"},{"boundingBox":"852,144,32,33","text":"用"}]},{"boundingBox":"513,193,312,38","words":[{"boundingBox":"513,193,41,36","text":"い"},{"boundingBox":"576,198,26,30","text":"日"},{"boundingBox":"620,197,20,28","text":"2"},{"boundingBox":"654,197,33,34","text":"回"},{"boundingBox":"693,196,35,34","text":"朝"},{"boundingBox":"736,197,31,33","text":"夕"},{"boundingBox":"777,198,31,30","text":"に"},{"boundingBox":"815,195,10,35","text":"】"}]},{"boundingBox":"412,294,652,39","words":[{"boundingBox":"412,297,20,29","text":"2"},{"boundingBox":"448,294,11,37","text":")"},{"boundingBox":"515,295,9,37","text":"【"},{"boundingBox":"530,296,38,35","text":"般"},{"boundingBox":"574,296,10,36","text":"】"},{"boundingBox":"616,304,36,20","text":"へ"},{"boundingBox":"657,298,35,28","text":"パ"},{"boundingBox":"704,299,21,32","text":"リ"},{"boundingBox":"742,301,30,29","text":"ン"},{"boundingBox":"779,299,38,34","text":"類"},{"boundingBox":"819,298,37,35","text":"似"},{"boundingBox":"858,297,35,36","text":"物"},{"boundingBox":"899,297,35,35","text":"質"},{"boundingBox":"938,297,37,35","text":"軟"},{"boundingBox":"977,297,36,35","text":"膏"},{"boundingBox":"1024,298,21,29","text":"O"},{"boundingBox":"1058,321,6,7","text":"."}]},{"boundingBox":"491,348,523,36","words":[{"boundingBox":"491,352,33,31","text":"ア"},{"boundingBox":"536,352,31,28","text":"ン"},{"boundingBox":"576,352,35,31","text":"テ"},{"boundingBox":"617,352,36,24","text":"べ"},{"boundingBox":"659,363,35,7","text":"ー"},{"boundingBox":"710,351,21,33","text":"ト"},{"boundingBox":"740,350,38,34","text":"軟"},{"boundingBox":"781,350,36,34","text":"膏"},{"boundingBox":"829,352,21,29","text":"O"},{"boundingBox":"863,376,7,6","text":"."},{"boundingBox":"909,352,21,28","text":"0"},{"boundingBox":"950,352,19,29","text":"5"},{"boundingBox":"982,348,32,36","text":"%"}]},{"boundingBox":"490,403,206,29","words":[{"boundingBox":"490,414,37,6","text":"ー"},{"boundingBox":"532,403,38,29","text":"M"},{"boundingBox":"588,403,12,29","text":"I"},{"boundingBox":"620,404,33,28","text":"X"},{"boundingBox":"660,415,36,6","text":"ー"}]},{"boundingBox":"489,453,547,37","words":[{"boundingBox":"489,453,40,37","text":"顔"},{"boundingBox":"534,456,38,32","text":"以"},{"boundingBox":"576,454,39,36","text":"外"},{"boundingBox":"662,456,37,31","text":"か"},{"boundingBox":"705,454,34,34","text":"ゆ"},{"boundingBox":"745,459,36,25","text":"い"},{"boundingBox":"792,455,25,30","text":"と"},{"boundingBox":"832,457,27,27","text":"こ"},{"boundingBox":"870,454,29,31","text":"ろ"},{"boundingBox":"911,455,33,29","text":"に"},{"boundingBox":"996,453,20,28","text":"2"},{"boundingBox":"1029,475,7,11","text":","}]},{"boundingBox":"518,504,363,40","words":[{"boundingBox":"518,507,10,37","text":"【"},{"boundingBox":"536,509,36,35","text":"医"},{"boundingBox":"579,507,37,36","text":"師"},{"boundingBox":"621,511,36,29","text":"の"},{"boundingBox":"663,506,37,37","text":"指"},{"boundingBox":"706,507,36,35","text":"示"},{"boundingBox":"746,506,38,35","text":"通"},{"boundingBox":"796,506,21,33","text":"り"},{"boundingBox":"832,508,32,30","text":"に"},{"boundingBox":"871,504,10,37","text":"】"}]},{"boundingBox":"411,608,580,48","words":[{"boundingBox":"411,622,22,32","text":"3"},{"boundingBox":"449,618,13,38","text":")"},{"boundingBox":"492,625,38,21","text":"ニ"},{"boundingBox":"540,616,37,35","text":"ゾ"},{"boundingBox":"584,619,29,32","text":"ラ"},{"boundingBox":"624,630,36,6","text":"ー"},{"boundingBox":"667,617,37,31","text":"ル"},{"boundingBox":"712,618,30,28","text":"ロ"},{"boundingBox":"752,627,35,6","text":"ー"},{"boundingBox":"795,616,33,29","text":"シ"},{"boundingBox":"841,621,23,22","text":"ョ"},{"boundingBox":"880,614,29,29","text":"ン"},{"boundingBox":"925,612,19,28","text":"2"},{"boundingBox":"958,608,33,37","text":"%"}]},{"boundingBox":"494,668,336,41","words":[{"boundingBox":"494,674,36,35","text":"あ"},{"boundingBox":"538,673,36,34","text":"た"},{"boundingBox":"586,672,30,35","text":"ま"},{"boundingBox":"680,671,13,30","text":"1"},{"boundingBox":"711,696,9,10","text":"、"},{"boundingBox":"762,669,19,30","text":"2"},{"boundingBox":"796,668,34,35","text":"回"}]},{"boundingBox":"520,718,372,50","words":[{"boundingBox":"520,729,10,39","text":"【"},{"boundingBox":"539,730,37,37","text":"医"},{"boundingBox":"583,728,38,37","text":"師"},{"boundingBox":"626,731,36,29","text":"の"},{"boundingBox":"668,725,39,37","text":"指"},{"boundingBox":"712,726,37,34","text":"示"},{"boundingBox":"754,723,39,37","text":"通"},{"boundingBox":"805,722,21,35","text":"り"},{"boundingBox":"842,723,32,32","text":"に"},{"boundingBox":"881,718,11,39","text":"】"}]}]},{"boundingBox":"1074,293,93,191","lines":[{"boundingBox":"1102,293,65,37","words":[{"boundingBox":"1102,297,19,29","text":"3"},{"boundingBox":"1135,293,32,37","text":"%"}]},{"boundingBox":"1074,451,65,33","words":[{"boundingBox":"1074,452,19,28","text":"3"},{"boundingBox":"1106,451,33,33","text":"回"}]}]},{"boundingBox":"1440,598,85,245","lines":[{"boundingBox":"1440,598,58,31","words":[{"boundingBox":"1440,600,18,29","text":"5"},{"boundingBox":"1477,598,21,29","text":"0"}]},{"boundingBox":"1463,810,62,33","words":[{"boundingBox":"1463,812,20,31","text":"3"},{"boundingBox":"1502,810,23,32","text":"0"}]}]},{"boundingBox":"407,821,765,298","lines":[{"boundingBox":"407,821,765,66","words":[{"boundingBox":"407,852,27,32","text":"4"},{"boundingBox":"449,848,12,39","text":")"},{"boundingBox":"505,846,64,34","text":"10"},{"boundingBox":"584,840,36,41","text":"%"},{"boundingBox":"627,840,38,37","text":"サ"},{"boundingBox":"677,839,22,36","text":"リ"},{"boundingBox":"716,837,36,37","text":"チ"},{"boundingBox":"759,837,37,33","text":"ル"},{"boundingBox":"800,833,40,39","text":"酸"},{"boundingBox":"848,835,28,33","text":"ワ"},{"boundingBox":"886,832,34,32","text":"セ"},{"boundingBox":"934,829,22,35","text":"リ"},{"boundingBox":"973,832,31,29","text":"ン"},{"boundingBox":"1010,825,39,38","text":"軟"},{"boundingBox":"1051,824,37,38","text":"膏"},{"boundingBox":"1093,822,37,38","text":"東"},{"boundingBox":"1134,821,38,36","text":"豊"}]},{"boundingBox":"493,894,303,48","words":[{"boundingBox":"493,907,40,35","text":"か"},{"boundingBox":"539,904,39,36","text":"か"},{"boundingBox":"589,902,28,34","text":"と"},{"boundingBox":"671,896,41,40","text":"夜"},{"boundingBox":"729,896,13,32","text":"1"},{"boundingBox":"761,894,35,38","text":"回"}]},{"boundingBox":"520,944,383,61","words":[{"boundingBox":"520,963,10,42","text":"【"},{"boundingBox":"539,963,38,41","text":"医"},{"boundingBox":"584,960,40,39","text":"師"},{"boundingBox":"629,962,38,32","text":"の"},{"boundingBox":"673,955,39,40","text":"指"},{"boundingBox":"718,955,38,37","text":"示"},{"boundingBox":"761,951,39,40","text":"通"},{"boundingBox":"813,950,22,37","text":"り"},{"boundingBox":"851,950,33,33","text":"に"},{"boundingBox":"892,944,11,40","text":"】"}]},{"boundingBox":"629,1070,171,49","words":[{"boundingBox":"629,1080,41,39","text":"以"},{"boundingBox":"674,1077,40,39","text":"下"},{"boundingBox":"720,1072,39,42","text":"余"},{"boundingBox":"768,1070,32,41","text":"白"}]}]}],"textAngle":0,"language":"ja"}'''

"""
"""        
def analyse_morphological( str_prescription ):
  str = 'くすり 2錠 朝夕 7'
  return str

"""
"""        
def grouping( str_words ):
  result = {}
  result[ 'name' ] = 'くすり'
  result[ 'amount' ] = '2錠'
  result[ 'timing' ] = '朝夕'
  result[ 'days' ] = '7'
  return result


"""
"""        
@app.route( '/api/analyser', methods=[ 'GET', 'POST' ] )
def analyse_medicine_info():
  if request.method == 'POST':

    if request.headers[ 'Content-Type' ] != 'multipart/form-data':
      print( request.headers[ 'Content-Type' ] )
      return jsonify( res='error' ), 400
  
    img_file = request.files[ 'img_file' ]
    if img_file and availabled_file( img_file.filename ):
    
      # Upload request image
      upload_image( img_file )

      # Execute OCR
      str_prescription = execute_ocr()
      
      # analyse morrphological
      str_words = analyse_morphological( str_prescription )

      # grouping words
      map = grouping( str_words )
    
      return jsonify( map )
      
    else:
      return '<p>Not supported file=' + fileneme + '</p>'

  else:
    return redirect( url_for('index') )

    
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)



