from urllib.request import urlopen

def get_html(url):
    arquivo = open('exercicio08.txt', 'w')
    html = urlopen(url).read().decode('latin1')
    print(html)
    arquivo.writelines(html)


get_html('http://google.com')
