import urllib.error
import urllib.request

# Criamos um cabeçalho para fingir que é um navegador acessando
req = urllib.request.Request(
    'https://pudim.com.br/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

try:
    site = urllib.request.urlopen(req)
except urllib.error.URLError:
    print('O SITE NÃO ESTÁ ACESSÍVEL!')
else:
    print('O SITE DO PUDIM ESTÁ ACESSÍVEL!!')
    
    # Opcional: você pode ler o conteúdo se quiser
    print(site.read())