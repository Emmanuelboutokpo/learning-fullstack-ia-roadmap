from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from validator import User, UserUpdate

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open("patients.json", 'w') as f:
        json_str = json.dumps(data, indent=4)
        return f.write(json_str)

@app.get("/patients")
def get_patients():
    data = load_data()
    return data

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", examples="P001")):
    data = load_data()
    for key, patient in data.items():
        if key == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(sorted_by: str = Query(..., description="The field to sort by (height, weight, or bmi)", examples="height, weight, bmi"),
order: str = Query("asc", description="The sort order (asc or desc)", examples="asc")):
     
    valid_sort_fields = ["height", "weight", "bmi"]

    if sorted_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Must be one of {valid_sort_fields}.")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order. Must be 'asc' or 'desc'.")
   
    data = load_data()

    sorted_order = False if order == "asc" else True
 
    sorted_patients = sorted(data.values(), key=lambda x: x[sorted_by], reverse=sorted_order)
    
    return sorted_patients


@app.post('/create')
def create_patient(user: User):
    data = load_data()
    patient_id = user.id
    if patient_id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    data[patient_id] = user.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(content={"message": "Patient created successfully"}, status_code=201)


@app.put('/update/{patient_id}')
def update_patient(patient_id: str, user: UserUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    exiting_patient = data[patient_id]
    user_exit = user.model_dump(exclude_unset=True)

    for key, value in user_exit.items():
        exiting_patient[key] = value
    
    exiting_patient['id'] = patient_id
    pydantic_schema = User(**exiting_patient)
    exiting_patient = pydantic_schema.model_dump(exclude=['id'])
    data[patient_id] = exiting_patient
    save_data(data)
    return JSONResponse(content={"message": "Patient updated successfully"}, status_code=200)


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    del data[patient_id]
    save_data(data)
    return JSONResponse(content={"message": "Patient deleted successfully"}, status_code=200)
