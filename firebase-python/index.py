import pyrebase
import os

firebaseConfig = {
    'apiKey': "AIzaSyAV1f-7TKAdwHCqIUtVxf1b3ZDFHQy1Pf0",
    'authDomain': "python-example-c6be8.firebaseapp.com",
    'databaseURL': "https://python-example-c6be8-default-rtdb.firebaseio.com",
    'projectId': "python-example-c6be8",
    'storageBucket': "python-example-c6be8.appspot.com",
    'messagingSenderId': "625887155472",
    'appId': "1:625887155472:web:e4cbf93c97ae74bcbb0195"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
#auth = firebase.auth()
storage = firebase.storage()

#Autenticacion
#Login
#email = input('Ingrese su email: ')
#password = input('Ingrese su contrasenhia: ')

#try:
    #auth.sign_in_with_email_and_password(email, password)
    #print('Usuario autenticado correctamente')
#except:
    #print('Ha ocurrido un error en la autenticacion')


#signup
#email = input('Ingrese su email: ')
#password = input('Ingrese su contrasenhia: ')
#confirmpass = input('Confirmar contrasenhia: ')

#if password == confirmpass:
#    try:
#        auth.create_user_with_email_and_password(email, password)
#        print('Success')
#    except:
#        print('Email ya existe')



#Storage
#fileName = input('Ingrese el nombre del archivo que desea subir: ')
fileName = 'images/biggie.png'
#cloudFileName = input('Ingrese el nombre del archivo en la nube: ')
cloudFileName = 'biggie/mi-folder'
storage.child(cloudFileName).put(fileName)
#try:
#    os.remove(fileName)
#except:
#    print('No se pudo eliminar el archivo')

#Obtenemos la url del archivo que acabamos de subir
print(storage.child(cloudFileName).get_url(None))

#Descargar los archivos del Storga
#cloudFileName = input('Ingrese el nombre del archivo que desee descargar: ')
#storage.child(cloudFileName).download('', 'descarga.pdf')

#Database
#Create
data = {
    'age': 32,
    'addres': 'Las Vegas',
    'employed': True,
    'name':'James Simons'
}

#db.child('people').child('person').push(data)
#db.child('people').child('myid').set(data)


#Update
#db.child('people').child('myid').update({'name': 'Jane'})


#Read
#people = db.child('people').get()

#for person in people.each():
#    if person.val()['name'] == 'Jane':
#        db.child('people').child(person.key()).update({'name': 'Mark'})
#    #print(person.val())
#    #print(person.key())


#Delete
#db.child('people').child('person').remove()
#people = db.child('people').get()
#for person in people.each():
#    if person.val()['name'] == 'Jhon Smith':
#        db.child('people').child(person.key()).child('age').remove()

#Read
#people = db.child('people').child('-MerFf5JC2d3DHiE9T8i').get()
#print(people.val())
