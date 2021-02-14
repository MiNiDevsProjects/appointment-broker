from tinydb import Query, TinyDB

#This is the DB Layer. All DB operations will be handled here.
db = TinyDB('db/db.json')
table_doctor = db.table('doctor')
table_patient = db.table('patient')
doctor = {}
patient = {}

Doc = Query()
Pat = Query()

########
#Create

def createDoctor(doc_id, doc_name, isAvailable):
    table_doctor.insert({'doctor_id': doc_id, 'doctor_name': doc_name, 'isAvailable': isAvailable})
    # for row in table_doctor:
    #     print(row)

def createPatient(patient_id, patient_name, patient_dob, nextAppointment, prevAppointment):
    table_patient.insert({'patient_id': patient_id, 'patient_name': patient_name, 'patient_dob': patient_dob, 'nextAppointment': nextAppointment, 'prevAppointment': prevAppointment})

########
#Read
def getDoctor():
    doctor = table_doctor.all()
    return doctor

def getPatient():
    patient = table_patient.all()
    return patient

########
#Update

def updateDoctor(doc_name, isAvailable):
    table_doctor.update({'isAvailable': isAvailable}, Doc.doctor_name == doc_name)

def updatePatient(pat_name, update_field, update_value):
    table_doctor.update({update_field: update_value}, Pat.patient_name == pat_name)


########
#Delete
def delDoctor(doctor_name):
    table_doctor.remove(Doc.doctor_name == doctor_name)

def delPatient(patient_name):
    table_patient.remove(Pat.patient_name == patient_name)
