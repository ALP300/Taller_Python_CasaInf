import requests
def obtener_info_usuarios(user_id):
    url= f'https://jsonplaceholder.typicode.com/users/{user_id}'
    respuesta= requests.get(url)
    if respuesta.status_code==200:
        datos= respuesta.json()
        nombre= datos['name']
        correo= datos['email']
        ciudad= datos['address']['city']
        compania= datos['company']['name']
        
        return{
            'Nombre':nombre,
            'Correo Electrónico': correo,
            'Ciudad': ciudad,
            'Compañía': compania
        }
    else:
        return{'Error':'No se pudo tener la información'}
    

user_id=2
info_usuario= obtener_info_usuarios(user_id)
for clave, valor in info_usuario.items():
    print(f'{clave}:{valor}')    
