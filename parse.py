from urllib.parse import urlparse

result = urlparse('http://www.python.org:80/guido/python.html;philosophy?overall=3#here')
# ParseResult(scheme='http', netloc='www.python.org:80', path='/guido/python.html', params='philosophy', query='overall=3', fragment='here')
print(result)

