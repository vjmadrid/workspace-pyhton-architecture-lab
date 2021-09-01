# acme-selenium

This project represents a architecture library (dependency) related with selenium to develop the different parts in a homogeneus way

This library stands out for:

* Define selenium framework and their versioning




## Technological Stack

* [Python](https://www.python.org/)

Dependencies with architecture projects

* **acme-test** [0.0.1] : Architecture library for testing used in the test environment -> Custom Library [Documentation](XXXX)
* **acme-common** [0.0.1] : Architecture library for common used -> Custom Library [Documentation](xxx)

Third Party

* **grequests** [0.6.0] : Framework combinated : rquests + gevent -> [Pypi](https://pypi.org/project/grequests/) [Documentation](https://github.com/spyoungtech/grequests)

  * Includes :
    * gevent
    * requests

```bash
import grequests

BATCH_LENGTH = 5

urls = [...] 
results = []

while urls:

    batch = urls[:BATCH_LENGTH]
    rs = (grequests.get(url) for url in batch)
    batch_results = grequests.map(rs)
    results += batch_results
    urls = urls[BATCH_LENGTH:]

print(results)
```

* **html5lib** [1.1] : HTML parser based on the WHATWG HTML specification -> [Pypi](https://pypi.org/project/html5lib/) [Documentation](https://github.com/html5lib/html5lib-python)

  * Includes :
    * six
    * webencodings

* **lxml** [4.6.3] : XML / HTML processing library combining libxml2/libxslt with the ElementTree API -> [Pypi](https://pypi.org/project/lxml/) [Documentation](https://lxml.de/)

  * Provide extract data from an XML / HTML document with XPath

```bash
# Example
from lxml import html

data_string = r.data.decode('utf-8', errors='ignore')
tree = html.fromstring(data_string)
links = tree.xpath('//a')
```


* **bs4** [0.0.1] : Dummy package for Beautiful Soup -> [Pypi](https://pypi.org/project/bs4/) [Documentation](https://pypi.org/project/beautifulsoup4/)

  * Includes :
    * **beautifulsoup4 :** library that will help us parse the HTML returned by the server

* **selenium** [3.141.0] : Python bindings for Selenium -> [Pypi](https://pypi.org/project/selenium/) [Documentation](https://github.com/SeleniumHQ/selenium/)

  * Includes :
    * urllib3


* **webdriver-manager** [3.4.2] : Framework provides the way to automatically manage drivers for different browsers -> [Pypi](https://pypi.org/project/webdriver-manager/) [Documentation](https://github.com/SergeyPirogov/webdriver_manager)

  * Includes :
    * requests
    * crayons
    * configparsers

