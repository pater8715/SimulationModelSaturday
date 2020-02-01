nombre = input('Como te llamas ')
edad = input('Cuantos años tienes ')
address = input('cual es su dirección ')
telefono = input('cual es tu numero de celular ')
persona = {'nombre': nombre, 'edad': edad, 'address':address, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['address'], 'y su numero de telefono es ', persona['telefono'])