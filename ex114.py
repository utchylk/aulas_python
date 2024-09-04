import urllib
import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('https://www.google.com/')
except urllib.error.URLError as e:
    print('\033[31mO site Pokemon Showdown não está disponível no momento.\033[m')
    print(f'Erro: {e}')
else:
    print('\033[32mO site Pokemon Showdown está disponível!\033[m')


