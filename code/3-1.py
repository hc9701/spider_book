import requests
req = requests.get('http://www.xicidaili.com/nn/')
print('content',req.content,sep=': ')
print(type(req.content))
print('-'*10,'end','-'*10,end='来个换行吧')
