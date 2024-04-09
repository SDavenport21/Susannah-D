# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:05:53 2024
#MOST recent edit 4/8/2024 homework 10.2
@author: susda
"""
from flask import Flask
from flask import request
import uuid
import pandas as pd

file_path = "class.csv"

df = pd.read_csv(file_path)

def init():
  try:
    with open(file_path, 'x') as file:
      file.write("ID,Name,Email,Phone")
  except FileExistsError:
      print(f"The file '{file_path}' already exists.")


def csvWriter(data):
    with open(file_path, 'a') as file:
        file.write(data)
        file.close()

app = Flask(__name__)

init()
file_path = "class.csv"
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to the classroom app!'


####MY MOST RECENTS EDITS### HW 10.2 Validation
#This homework I created a nested function (studentPOST, studentGET, studentDELETE)
# or (teacherPOST, teacherGET, teacherDELETE)
#these functions hold the necessary code to execut the problems outlined on brightspace

def student_requests():
    data = request.get_json()
    if request.method == 'POST': #checking if the request method is POST
        #gets the json data returned w POST
        record = "\n{id},{name},{email},{phone}".format(id=uuid.uuid4(),name=data.get('name'),email=data.get('email'),phone=data.get('phone'))
        # record is a string in csv format n\ creates a new line
        csvWriter(record)
        #this is going to write 'record' to the file
        return "studentPOST"
    def studentPOST(): #nested function
        import re #need this in a few lines
        data = request.get_json()
    
    #validate phone number format using very painful Windows format and lovely \ slashes
        if not re.match(r'^\d{3}-\d{3}-\d{4}$', data["Phone"]):
            return '{"error": "Phone Number must follow xxx-xxx-xxxx format"}', 400

   #if either name or phone are in 'data', the error has a 400 response
        if "Name" not in data or "Phone" not in data:
            return '{"error": "Name and Phone fields are required"}', 400

    #a chance to use my regex skills... I found a Windows friendly version of the emial formula and thought it was cool
        if "Email" in data and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data["Email"]):
            return '{"error": "This email address is invalid"}', 400
        
    if request.method == 'GET':
        data = request.get_json()
        if 'id' in data:
            c = pd.read_csv(file_path) #puts the particular csv indo a pandas df named 'c'
            d = c.loc[c['ID'] == data['id']] #I have to use pandas filtering here so that ONLY the correct rows in the 'ID' column that match the request are retrieved
            return d.to_json(orient='records')
        else:
            return "ID not provided in request" #contingency statement in case the id isn't in the JSON information
        def studentGet(): #another nested function
            data = request.get_json()
            
            if "ID" in data:
                c = pd.read_csv(file_path)
                d = c.loc[c['ID'] == data["ID"]]
                return d.to_json(orient = 'records'), 200
            else:
                return '{"error":"ID field is not set"}', 400
            
            if d.empty:
                return '{"error":"No matching record found for the provided ID"}', 400
            else:
                return d.to_json(orient='records'), 200
        
    elif request.method == 'DELETE':
        data = request.get_json()
        if 'id' in data: #If the JSON data has what we need (the 'id' exists there_ it will execute this block)
            c = pd.read_csv(file_path) 
            c = c[c['ID'] != data['id']]  # Remove record with specified ID
            c.to_csv(file_path, index=False)  # Write the updated df back to CSV file
            return "Record deleted successfully"
        else:
            return "ID not provided in request"
        
        def studentDELETE(): #final nested function
            data = request.get_json()
            if "ID" not in data:
               return '{"error": "ID field is not provided"}', 400
            if "ID" not in df :
                return '{"message": "this ID does not exist"}', 200



def teacher_requests(): ##pretty much identical to the code above with a few differences
    if request.method == 'POST':
        data = request.get_json()
        
        #I decided that teachers and studends alike will have the same id/name/email/phone info pattern of information in their records
        record = "\n{id},{name},{email},{phone}".format(id=uuid.uuid4(),name=data.get('name'),email=data.get('email'),phone=data.get('phone'))
        csvWriter(record) #just keeping 'record' should work for each function, since they are created within different bounds from each other
        return "teacherPOST" #returns the teacher creation
    def teacherPOST(): #nested function
        import re #need this in a few lines
        data = request.get_json()
    
    #validate phone number format using very painful Windows format and lovely \ slashes
        if not re.match(r'^\d{3}-\d{3}-\d{4}$', data["Phone"]):
            return '{"error": "Phone Number must follow xxx-xxx-xxxx format"}', 400

   #if either name or phone are in 'data', the error has a 400 response
        if "Name" not in data or "Phone" not in data:
            return '{"error": "Name and Phone fields are required"}', 400

    #a chance to use my regex skills... I found a Windows friendly version of the emial formula and thought it was cool
        if "Email" in data and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data["Email"]):
            return '{"error": "This email address is invalid"}', 400
    if request.method == 'GET':
        data = request.get_json()
        if 'id' in data:
            c = pd.read_csv(file_path)
            d = c.loc[c['ID'] == data['id']]
            return d.to_json(orient='records')
        else:
            return "ID not provided in request"
        def teacherGet(): #another nested function
            data = request.get_json()
            
            if "ID" in data:
                c = pd.read_csv(file_path)
                d = c.loc[c['ID'] == data["ID"]]
                return d.to_json(orient = 'records'), 200
            else:
                return '{"error":"ID field is not set"}', 400
            
            if d.empty:
                return '{"error":"No matching record found for the provided ID"}', 400
            else:
                return d.to_json(orient='records'), 200
        #following same exact format....
    elif request.method == 'DELETE':
        data = request.get_json()
        if 'id' in data:
            c = pd.read_csv(file_path)
            c = c[c['ID'] != data['id']]  # Remove record with specified ID
            c.to_csv(file_path, index=False)  # Write updated DataFrame back to CSV file
            return "Record deleted successfully"
        else:
            return "ID not provided in request"
        def teacherDELETE(): #final nested function
            data = request.get_json()
            if "ID" not in data:
               return '{"error": "ID field is not provided"}', 400
            if "ID" not in df :
                return '{"message": "this ID does not exist"}', 200


#NOW we call the app route. These functions do't have any logic or other stuff hardcoded into them. They call everything
#stored in the techer_requests() and student_requests() functions that appear below!

@app.route('/student', methods=['POST', 'GET', 'DELETE'])
def students():
    return student_requests()

@app.route('/teacher', methods=['POST', 'GET', 'DELETE'])
def teachers():
    return teacher_requests()

if __name__ == "__main__":
    app.run()
    
app.run(host='0.0.0.0', port=4999)
    