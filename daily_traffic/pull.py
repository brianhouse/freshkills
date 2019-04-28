#!/usr/bin/env python3

import json, sys, os, requests, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from util import *

lat, lon = 40.566909, -74.193448
url = "https://traffic.api.here.com/traffic/6.2/flow.json?prox=%s,%s,100&app_id=%s&app_code=%s" % (lat, lon, config['traffic']['id'], config['traffic']['code'])
print(url)


r = requests.get(url)
data = r.json()

# with open('response.json', 'w') as f:
#     f.write(json.dumps(data, indent=4))

# with open('response.json') as f:    
#     data = json.loads(f.read())

readings = [item for item in data['RWS'][0]['RW']]

item = None
for reading in readings:
    for fi in reading['FIS'][0]['FI']:
        if fi['TMC']['DE'] != "RT-440/Muldoon Ave":
            continue
        else:
            item = fi
            item['time'] = reading['PBT']
            item['CF'] = item['CF'][0]
            del item['SHP']
            break
    if item is not None:
        break

result = json.dumps(item, indent=4)
print(result)

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.json'))
with open(path, 'a') as f:
    f.write(',' + result)
