from orm_sqlite import *
import os

import orm_sqlite
file_path = os.path.join(os.getcwd(), 'test_data.db')
print(os.path.exists(file_path))


class employee_details(Model):
        id = IntegerField(primary_key=True)
        name = StringField()
        email = StringField()
        gender = IntegerField()
        contact = IntegerField()
        age = IntegerField()
class gender(Model):
        id = IntegerField(primary_key=True)
        gender = StringField()


db = orm_sqlite.Database(file_path,check_same_thread=False)

    
    
  

    