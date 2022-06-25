import json
from urllib import request as rq

# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://my.api.mockaroo.com/personas.json?key=a6704150'
respuesta = rq.urlopen(url)
# print('respuesta \n', respuesta, '\n\n')
contenido = respuesta.read()
# print('contenido \n', contenido, '\n\n')
json_obtenido = json.loads(contenido.decode('utf-8'))
# print('json obtenido \n', json_obtenido, '\n\n')
for persona in json_obtenido:
    print(f'Nombre: {persona["nombre"]} \n')
