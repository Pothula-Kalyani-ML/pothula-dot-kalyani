import os.path
import os
from peewee import *

#from peewee import SqliteDatabase, Model,TextField ,IntegerField
file_path = os.path.join(os.getcwd(),'test_data.db')
print(os.path.exists(file_path))
db=SqliteDatabase(file_path)
print(db)
class employee(Model):
    class Meta:
        Database=db
        db_table='employee_details'
class employee_details(employee):
      id= PrimaryKeyField
      name= TextField
      email= TextField
      gender=ForeignKeyField	
      contact=IntegerField
      age= IntegerField
db.connect()        
if __name__=='__main__': 

 employees=db.select()
 for employee in employees:
        print(employee)   
   
  
db.close()