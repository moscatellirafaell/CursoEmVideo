# import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except urllib.error.URLError:
    print('Offline')
else:
    print('Online')
#    print(site.read())
