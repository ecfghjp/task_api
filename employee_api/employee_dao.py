from pymongo import MongoClient

#initialise mongo client
client = MongoClient('localhost', 27017)
db_emp = client['iagemployee']
db=db_emp.employee

#retrieve al employees
def getAllEmployees():
    results = db.find()
    final = [result for result in results]
    return final

#create employees
def createEmployee(employee):
    try:
        result = db.insert_one(employee)
        return 'Ok' 
    except:
         return "Problem in saving Employee" 

#delete employees
def deleteEmployee(aid):
    result = db.delete_one({"aid":aid})
    return result

#update employees
def updateEmployee(employee):
    emp = [employee_in_db for employee_in_db in db.find()]
    #newValue =  {"$set":employee }
    db.update_one(emp,employee)

#retrieve single employee
def getEmployee(aid):
    return db.find_one({"aid":aid})