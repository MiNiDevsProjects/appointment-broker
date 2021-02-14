from tinydb import Query, TinyDB

#This is the DB Layer. All DB operations will be handled here.
db = TinyDB('db/db.json')
table_doctor = db.table('doctor')

def createDoctor(doc_id, doc_name, isAvailable):
    table_doctor.insert({'doctor_id': doc_id, 'doctor_name': doc_name, 'isAvailable': isAvailable})
    for row in table_doctor:
        print(row)