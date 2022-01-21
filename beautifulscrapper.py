from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exec
import requests

class ServaError(Exception):
    """Raie when python requests runs into an error."""
    pass



class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []


    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()

def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        perser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text

def main():
    url = 'https://realpython.com/beautiful-soup-web-scraper-python/'
    try:
        r = requests.get(url)
    except:
        raise ServaError("http request encountered an error ")
    with open('htmlpage.xml', 'w') as file:
        file.write(r.text)

    with open('parsedhtml.xml', 'w') as file2:
        file2.write(dehtml(htmlpage.xml))

if __name__ == '__main__':
    main()
