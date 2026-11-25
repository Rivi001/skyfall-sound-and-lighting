import requests
import re
import html

headers = {
    'User-Agent': 'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uinform.client.php)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

shortcodes = ['DExrrUZMbsM', 'DExsc6Gs-II', 'C5Y4uXysHZ2']

for sc in shortcodes:
    post_url = f"https://www.instagram.com/p/{sc}/"
    res = requests.get(post_url, headers=headers, timeout=15)
    text = res.text
    
    print(f"Shortcode: {sc} | Status: {res.status_code}")
    
    og_image = re.findall(r'<meta\s+property="og:image"\s+content="([^"]+)"', text)
    if not og_image:
        og_image = re.findall(r'property="og:image"\s+content="([^"]+)"', text)
    if not og_image:
        og_image = re.findall(r'https://scontent[^\s"\'\\]+', text)
        
    if og_image:
        img_url = html.unescape(og_image[0]).replace('\\u0026', '&')
        print(f"Found Original Image URL: {img_url}")
        
        img_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Referer': 'https://www.instagram.com/',
        }
        img_res = requests.get(img_url, headers=img_headers, timeout=20)
        if img_res.status_code == 200 and len(img_res.content) > 2000:
            file_path = f"static/images/insta_{sc}.jpg"
            with open(file_path, "wb") as f:
                f.write(img_res.content)
            print(f"SUCCESS: Saved original Instagram thumbnail ({len(img_res.content)} bytes) to {file_path}")
        else:
            print(f"Image download status: {img_res.status_code}, length: {len(img_res.content)}")
    else:
        print("No og:image meta tag found.")
    print("=" * 60)
