from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import requests
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        headers={
            'Content-Type':'application/json',
            'version':'1.1'
        }
        url='https://community-web-cloud-database.ccw.site/cloud_variable/detail/v2'
        req=requests.post(url,headers=headers)
        self.wfile.write(req.text.encode('utf-8'))
        return