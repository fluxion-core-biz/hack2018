
from flask import Flask

import MeCab

from flask import request, jsonify
import json
import traceback
from mimetypes import guess_extension
from time import time, sleep
from urllib.request import urlopen, Request
from urllib.parse import quote

from werkzeug.utils import secure_filename

import os
import sys
import subprocess
from datetime import datetime

from ocr import execute_ocr
from ocr_azure import execute_ocr_azure
from ocr_gcp import execute_ocr_gcp
from diag import diag
from morphological import analyse_morphological
from grouping import grouping


app = Flask( __name__, static_folder='static' )


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

  subprocess.call( "pwd" )
  subprocess.call( "ls" )
  
  print( str_output )
  return to_html( str_output )



RPATH_DIR_UPLOADS = './static/uploads'

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
  img_url = '/static/uploads/' + filename
  return;


"""
"""        
@app.route( '/api/analyser', methods=[ 'GET', 'POST' ] )
def analyse_medicine_info():
  print( 'method=' + request.method )
  if request.method == 'POST':

    if 'file' not in request.files:
      flash( 'No file part' )
      return '<p>Not exists file part</p>'
#    if request.headers[ 'Content-Type' ] != 'multipart/form-data':
#      print( request.headers[ 'Content-Type' ] )
#      return jsonify( res='error' ), 400
  
    print( 'start proc' )
    print( 'request.form=' + json.dumps( request.form.to_dict() ) + '\n' )
#    print( 'request.files[ file ]=' + request.files[ 'file' ] + '\n' )
#    print( 'request.files[ filedata ]=' + request.files[ 'filedata' ] + '\n' )
    img_file = request.files[ 'file' ]
    
    print( 'file.filename=' + img_file.filename + '\n' )
    
    if img_file and availabled_file( img_file.filename ):
      print( '--> start analyse' )
    
      # Upload request image
      upload_image( img_file )

      # Execute OCR
      str_prescription = execute_ocr()
#      str_prescription = execute_ocr_gcp()
      
      # analyse morrphological
      str_words = analyse_morphological( str_prescription )

      # grouping words
      map = grouping( str_words )
 
      print( '<-- compl analyse' )
      return jsonify( map )
      
    else:
      str_error = '<p>Not supported file=' + fileneme + '</p>'
      print( str_error )
      return str_error

  else:
    str_error = 'Not supported GET' + \
                '<p>Sample Image</p>' + \
                '<p><img src="/static/uploads/sample.jpg" /></p>'
    print( str_error )
    return str_error
#    return redirect( url_for('index') )


@app.route( '/api/azure', methods=[ 'GET', 'POST' ] )
def ocr_by_azure():
  print( 'method=' + request.method )
#  res = execute_ocr_azure( '/app/static/uploads/sample.jpg' )
  res = execute_ocr_azure( '/app/static/uploads/sample' )
  return '<p>' + res + '</p>'


@app.route( '/api/gcv', methods=[ 'GET', 'POST' ] )
def ocr_by_gcv():
  print( 'method=' + request.method )
  if request.method == 'GET':

    print( '--> start analyse' )
     
    res = execute_ocr_gcp( '/app/static/uploads/sample.jpg' )
      
    print( '<-- compl analyse' )
    return to_html( res )
#    return '<p>' + prescriptionJson + '</p>'
#    return jsonify( prescriptionJson )

  else:
    str_error = 'Not supported else GET' + \
                '<p>Sample Image</p>' + \
                '<p><img src="/static/uploads/sample.jpg" /></p>'
    print( str_error )
    return str_error


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)



