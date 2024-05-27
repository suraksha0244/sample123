import serial
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('final-8e024-firebase-adminsdk-8qvgk-c7ef5119f0.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://final-8e024-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


arduino = serial.Serial('COM4', 9600)  


while True:
 
    data = arduino.readline().decode().strip()
    if data:
        print("Received:", data)
        

        ref = db.reference('/heart_rate') 
        ref.set(data)  
        
arduino.close()