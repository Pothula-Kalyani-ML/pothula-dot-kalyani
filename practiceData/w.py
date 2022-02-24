import os.path
import os
from peewee import *

#from peewee import SqliteDatabase, Model,TextField ,IntegerField
file_path = os.path.join(os.getcwd(),'test_data.db')
print(os.path.exists(file_path))
db=SqliteDatabase(file_path)
db.connect()        

class employee(Model):
    class Meta:
        Database=db
        
class employee_details(employee):
      id= PrimaryKeyField()
      name= TextField()
      email= TextField()
      gender=IntegerField()	
      contact=IntegerField()
      age= IntegerField()
class gender (employee):
      id=PrimaryKeyField()
      gender=IntegerField()

employees=employee_details.select()
for employee in employees:
        print(employee)   
   
  
db.close()