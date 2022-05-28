from http import client
from iiot_device import Sensor
import json
import time

''' Creacion de un objeto de la clase HTTPConnection'''
_conn = client.HTTPConnection(host='localhost', port=5000)

''' Creación de un objeto de la clase Sensor'''
s = Sensor()

''' Para formar el JSON que se va para el servidor'''
h = {'Content-type':'application/json'}



while True:
    
    inclination = s.get_random_number()
    
    data = {
        'id': 1,
        'name': 'Sensor',
        'value': inclination
    }

    json_data = json.dumps(data)
    
    '''Enviar datos al servidor'''
    _conn.request('POST','/devices',json_data, headers=h)
    
    
    _conn.close()
    ''' If the inclination is higher then print the message '''
    if(inclination >= 15):
        print("Esta demasiado inclinado: ", inclination, "°")
    else:
        print("Inclinación: ", inclination,"°")
        
    time.sleep(1)