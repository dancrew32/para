# Para

Because concurrent.futures is impossible to memorize.

https://docs.python.org/3/library/concurrent.futures.html


## Test

```
make venv deps test
```

## Usage

```python
import requests
import para


def handler(url):
    import re
    data = requests.get(url).content.decode('utf-8')
    return re.findall(r'<title>(.*?)</title>', data)


def callback(titles):
    print(titles)


urls = (
    'https://danmasq.com', 
    'https://www.google.com', 
    'http://news.ycombinator.com', 
    'http://reddit.com',
    'http://ebay.com',
)

para.by_thread(handler, urls, callback, workers=5)
para.by_process(handler, urls, callback, workers=5)
```
