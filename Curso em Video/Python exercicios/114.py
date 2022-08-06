import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.erroe.URLError:
    print("O site não está up")
else:
    print("O site está funcionando normalmente")