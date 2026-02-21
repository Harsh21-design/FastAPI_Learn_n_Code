from fastapi import FastAPI, Path, HTTPException, Query
import json
app = FastAPI()

# Load Patient Data
def load_patients_data():
    with open("patients.json","r") as file:
        patients_data = json.load(file)

    return patients_data

# home page
@app.get("/")
def home():
    return {
        "message":"Welcome to our FastAPI App - Patient Management APIs System For Doctors"
    }

# about page
@app.get("/about")
def about():
    return {
        "message":"A fully funtional APIs to Manage Patient's Record."
    }

# Get all patients
@app.get("/patients")
def get_all_patients():
    all_patients = load_patients_data()
    return all_patients

# get single patients
# @app.get("/patients/{patients_id}")
# def get_single_patient(patients_id: str):
#     patients = get_all_patients()
#     if patients_id in patients:
#         return patients[patients_id]
    
#     # static json response
#     return {
#         "Error":f"Patient with ID '{patients_id}' is NOT FOUND!"
#     }

# get single patients : proper PATH validation & Custom HTTP Exception
@app.get("/patients/{patients_id}")
def get_patient(patients_id: str = Path(...,description="ID of the Patient in the Database",example="P001")):
    patients = load_patients_data()
    if patients_id in patients:
        return patients[patients_id]
    
    # HTTP Error Response ->status code
    raise HTTPException(status_code=404,detail=f"Patient with ID '{patients_id}' is NOT FOUND!")

# get sorted patients : Example of Query Params
@app.get("/sort")
def get_sorted_patients(sort_by: str = Query(..., description="Sort on the basis of height,weight or age"),order_by: str = Query('asc', description="Sort in asc or desc order" )):
    # valid sorting field in url
    valid_sorted_fields = ['weight','height','age']

    # validation rule/error handling
    if sort_by not in valid_sorted_fields:
        raise HTTPException(status_code=400,detail=f"Invalid fields select from {valid_sorted_fields}") # 400-> Bad Request
    
    if order_by not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f"Invalid order select between asc and desc")
    
    # get all patient
    patient_data = get_all_patients()

    # sort order reverse rule
    sort_order = True if order_by == 'desc' else False

    # sorting logic by sorted() func
    sorted_patient_data = sorted(
        patient_data.values(), # only dict values
        key=lambda x: x.get(sort_by,0), # dict key based rule
        reverse=sort_order # true/false
    )

    return sorted_patient_data
    
    # example endpoint for testing
    # http://127.0.0.1:8000/sort?sort_by=height&order_by=desc