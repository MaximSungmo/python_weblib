from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

port = 9999

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # urlparse를 간단하게 구현
        # print(self.path)
        #
        # if '?' in self.path:
        #     urls = self.path.split('?')
        #     path = urls[0]
        #     qs = urls[1].split('&')
        #     print(path, qs)

        result = urlparse(self.path)
        print(result, type(result))
        param = parse_qs(result.query)
        print(param)

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()  # 빈 개행을 보내는 것
        # body 시작
        self.wfile.write('<h1>안녕하세요</h1>'.encode('utf-8'))

# server 객체를 생성
httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
print(f'Server running on port{port}')
httpd.serve_forever()


