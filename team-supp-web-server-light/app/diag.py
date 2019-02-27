
# import MeCab

"""
"""
def diag_mecab():
  str_report = "MeCab:\n" + \
               " Not installed (light-version)\n"

  # str_input  = "1)【般】ペポタスチンベジル酸塩錠10mg2錠今日は帰宅後すぐ服用【1日2回朝夕に】(14日分)"

  # str_report = "MeCab:\n" + \
  #              ' Input=' + str_input + '\n'

  # tagger = MeCab.Tagger( "-Owakati" )
  # str_result = tagger.parse( str_input )
  # str_report += '-Owakati:\n' + \
  #               ' Result=' + str_result + '\n'

  # tagger = MeCab.Tagger( "-d /usr/lib/mecab/dic/mecab-ipadic-neologd" )
  # str_result = tagger.parse( str_input )
  # str_report += '-d /usr/lib/mecab/dic/mecab-ipadic-neologd:\n' + \
  #               ' Result=' + str_result + '\n'

  print( str_report )
  return str_report


"""
"""
def diag():
  str_report = '<Self diag result>\n' + \
               'r00.06\n' + \
               'merge igo-ocr by GCP\n' + \
               'support POST on /api/analyser\n' + \
               'usage:\n' + \
               'curl -F \'file=@sample.jpg\' localhost:80/api/analyser\n' + \
               '\n'
  str_report += diag_mecab()
  return str_report


