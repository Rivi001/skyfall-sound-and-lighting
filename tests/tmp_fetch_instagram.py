import requests, re, json
url='https://www.instagram.com/skyfall_sound_and_light/'
r=requests.get(url, headers={'User-Agent':'Mozilla/5.0'}, timeout=20)
print('status', r.status_code)
text=r.text
m=re.search(r'window\._sharedData\s*=\s*({.*?});', text, re.S)
print('shareddata', bool(m))
if m:
    data=json.loads(m.group(1))
    print(data.keys())
    print(type(data.get('entry_data')))
    print(json.dumps(list(data.keys())[:20], indent=2))
    print(text[text.find('window._sharedData')-200:text.find('window._sharedData')+3000])
