import urllib2
import re
from BeautifulSoup import BeautifulSoup

ROOT_URL = "http://www.aip2.com/zip.htm"

def state_to_zipcodes(state_url):
    html = urllib2.urlopen(state_url).read()
    # Note the preceding space!!
    regex = re.compile('[0-9]{5}', re.IGNORECASE|re.DOTALL)
    zips = regex.findall(html)
    assert (len(zips) > 25)
    return zips

def write_zips(zips):
    f = open('zipcodes.txt', 'a+')
    for z in zips:
        f.write(str(z)+'\r\n')
    f.close()

def extract_states(ROOT_URL):
    html = urllib2.urlopen(ROOT_URL).read()
    soup = BeautifulSoup(html)
    state_urls = [ tag['href'] for tag in soup.findAll() if tag.getText()  # sorry
            and tag.getText()[0]=='[' and tag.getText()[-1]==']' and tag.name=='a' ]
    for state_url in state_urls[2:]:
        zips = state_to_zipcodes(state_url)
        write_zips(zips)
        print 'zipcodes finished and written for', state_url

if __name__ == '__main__':
    extract_states(ROOT_URL)
