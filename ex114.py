import urllib.request
import  urllib.error

url = "https://www.pudim.com.br"

try:
    conexao = urllib.request.urlopen(url, timeout=5)
    print(f'O SITE DO PUDIM ESTA ACESSIVEL!!')
except urllib.error.HTTPError:
    print('O SITE ESTÁ ACESSÍVEL!')

except urllib.error.URLError:
    print('O SITE NÃO ESTÁ ACESSÍVEL!')