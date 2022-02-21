from peewee import *

database = SqliteDatabase('test_data.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class employee_details(BaseModel):
        email = TextField()
        name = TextField()
        gender = IntegerField()
        contact = IntegerField()
        age = IntegerField()
        class Meta:
            table_name = 'employee_details'

class gender(BaseModel):
    id = IntegerField(primary_key=True)
    gender = TextField()

    class Meta:
        table_name = 'gender'  
emp=employee_details.select()
for x in emp:
    print(x)
g=gender.select() 
for g1 in g:
    print(g1) 
database.close()   