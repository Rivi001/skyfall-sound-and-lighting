import requests, re, json, html
from bs4 import BeautifulSoup

url='https://www.instagram.com/skyfall_sound_and_light/'
r=requests.get(url, headers={'User-Agent':'Mozilla/5.0'}, timeout=30)
print('status', r.status_code)
text=r.text
print('len', len(text))
for pat in ['shortcode','edge_owner_to_timeline_media','pinned','edge_media_to_caption','display_url','profile_pic_url']:
    idx=text.lower().find(pat.lower())
    print(pat, idx)
    if idx != -1:
        print(text[idx-300:idx+3000])
        print('---')
