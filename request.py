from urllib.parse import urlencode
from urllib.request import urlopen, Request

# Get
http_response = urlopen('http://www.naver.com?a=ssss')
print(type(http_response))  # <class 'http.client.HTTPResponse'>
body = http_response.read
print(body)


# Post
data = {
    'email': 'ksm5318@gmail.com',
    'password': '1234',
    'name': '김성모'
}
# encode를 통해서 binary type으로 변형되었음
data = urlencode(data).encode('utf-8')
# print(data)

# Post 방식으로 보낼때는 request 객체가 꼭 필요하다.
request = Request('http://www.example.com', data)
request.add_header('Content-Type', 'text/html')
request.add_header('cookies', 'jsessionid=1232')
http_response2 = urlopen(request)
print(http_response2)
body = http_response2.read
print(body)









