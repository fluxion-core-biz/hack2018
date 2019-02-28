       
def grouping( in_words ):
  results = []
 
  result = {}
  result[ 'name' ] = 'アレグラ錠60mg'
  result[ 'amount' ] = '1錠'
  result[ 'timing' ] = '1日2回朝夕に'
  result[ 'days' ] = '14'
  results.append( result )

  result2 = {} 
  result2[ 'name' ] = 'リボスチン点眼液0.025%'
  result2[ 'amount' ] = '数滴'
  result2[ 'timing' ] = '1日4回朝昼タ晩に'
  result2[ 'days' ] = '14'
  results.append( result2 )
  
  result3 = {}
  result3[ 'name' ] = 'ラックビー錠'
  result3[ 'amount' ] = '2錠'
  result3[ 'timing' ] = '1日3回朝昼タに'
  result3[ 'days' ] = '7'  
  results.append( result3 )
  
  return results

  """ 
  medicineMatch = [words for words in in_words if re.match('[0-9]*\)')]
  lines = str_words.splitlines()
   
  return medicineMatch
  """


