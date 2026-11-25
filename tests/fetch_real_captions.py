import requests
import re
import html

headers = {
    'User-Agent': 'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uinform.client.php)',
}

shortcodes = ['DExrrUZMbsM', 'DExsc6Gs-II', 'C5Y4uXysHZ2']

for sc in shortcodes:
    res = requests.get(f'https://www.instagram.com/p/{sc}/', headers=headers)
    text = res.text
    
    og_desc = re.findall(r'property="og:description"\s+content="([^"]+)"', text)
    if not og_desc:
        og_desc = re.findall(r'name="description"\s+content="([^"]+)"', text)
        
    print(f"SHORTCODE: {sc}")
    if og_desc:
        cap = html.unescape(og_desc[0])
        # Clean string to ASCII safe for Windows terminal
        clean_cap = cap.encode('ascii', 'ignore').decode('ascii')
        print("AUTHENTIC CAPTION:", clean_cap)
    print("=" * 60)
