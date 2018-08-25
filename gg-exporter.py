import json
import requests
import time
import sys
import os

def url(uri):
  #s = time.time()
  #while s+5>time.time():
  #  pass
  try:
    r = requests.get(uri, cookies = {#there your cookies
    })
    return json.loads(r.text)
  except Exception as e:
    print(e, file=sf)
    return url(uri)
try:
  of = open(sys.argv[1], 'w', encoding='utf-8')
  sf = sys.stdout
except Exception as e:
  print(e)
  of = sys.stdout
  sf = open(os.devnull, 'w')
d = url('https://aol.iapps.gg.pl/api/aol/interlocutors?offset=0')
inter = 0
#try:
if 1:
  #print(d)
  import code
  #code.InteractiveConsole(vars()).interact()
  for inte in d['result']['interlocutors']:
    print('<', inte['interlocutorID'], end=' ', sep='', file=of)
    print('<', inte['interlocutorID'], end=' ', sep='', file=sf)
    if inte['interlocutorType'] != 1:
      print('group',file=of)
      print('group',file=sf)
    else:
      print(file=of)
      print(file=sf)
    e = url('https://aol.iapps.gg.pl/api/aol/conversationsInfo?interlocutorType='+str(inte['interlocutorType'])+'&interlocutorID='+str(inte['interlocutorID']))
    #print(e)
    e['result']['conversationsInfo'].reverse()
    for con in e['result']['conversationsInfo']:
      con['conversations'].reverse()
      for convs in con['conversations']:
        print('/', convs['conversationID'], sep='', file=sf)
        f = url('https://aol.iapps.gg.pl/api/aol/conversations?conversationID='+convs['conversationID'])
        #print(f)
        for conv in f['result']['conversations']:
          for wiad in conv['messages']:
            try:
              tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(wiad['sentTime'])))
              sdr = wiad['senderID']
              cnt = wiad['content']
              print('>', tm, sdr, cnt, sep='|', file=of)
            except Exception as e:
              print(e, file=sf)
              print('>', wiad, file=of, sep='|')
    
#finally:
#  input()
