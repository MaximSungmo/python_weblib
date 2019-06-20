from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 성공
# GET / HTTP/1.1
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)  # 200, OK

if resp.status == 200:
    body = resp.read()
    print(body, type(body))

# 실패
# GET / HTTP/1.1
conn.request('GET', '/hello.html')
resp = conn.getresponse()
print(resp.status, resp.reason)  # 404 File Not Found

if resp.status == 404:
    body = resp.read()
    print(body, type(body))

