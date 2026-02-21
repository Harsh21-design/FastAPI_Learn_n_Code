# from fastapi import FastAPI, Path, HTTPException
# import json
# app = FastAPI()

# # Load Patient Data
# def load_patients_data():
#     with open("patients.json","r") as file:
#         patients_data = json.load(file)

#     return patients_data

# @app.get("/")
# def home():
#     return {
#         "message":"Welcome to our FastAPI App - Patient Management APIs System For Doctors"
#     }

# @app.get("/about")
# def about():
#     return {
#         "message":"A fully funtional APIs to Manage Patient's Record."
#     }

# @app.get("/patients")
# def get_patients():
#     all_patients = load_patients_data()
#     return all_patients

# @app.get("/patients/{patients_id}")
# def get_patient(patients_id: str = Path(...,description="ID of the Patient in the Database",example="P001")):
#     patients = load_patients_data()
#     if patients_id in patients:
#         return patients[patients_id]
    
#     # static json response
#     # return {
#     #     "Error":f"Patient with ID '{patients_id}' is NOT FOUND!"
#     # }
    
#     # HTTP Error Response ->status code
#     raise HTTPException(status_code=404,detail="Patient Not Found!")

