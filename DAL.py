import DBL
from uuid import uuid4

#This is the Data Abstraction Layer.
#This program sits in between database operations and application operations

#add serial number generater

#add UID generater
def new_doctor(doctor_name):
    doctor_id = str(uuid4())
    print(doctor_id)

    doctor_isavailable = True
    DBL.createDoctor(doctor_id ,doctor_name, doctor_isavailable)

doctorName = input("Register Doctor Name: ")
new_doctor(doctorName)