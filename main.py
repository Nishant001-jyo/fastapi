# import json

# from fastapi import FastAPI, HTTPException , Path, Query


# app=FastAPI()
# def load_data():
#     with open("patients.json", "r") as file:
#         data = json.load(file)
#     return data 


# @app.get("/")
# def hello():
#     return {"message": "Patient Management System API "}

# @app.get("/about")
# def about():
#     return {"message": "This is a simple Patient Management System API built using FastAPI. It allows you to manage patient information and perform CRUD operations."}


# @app.get("/contact")
# def contact():
#     return {"message": "Contact us at example@email.com"}

# # to run this application, use the command: uvicorn main:app --reload


# @app.get("/view")
# def view_patients():
#     data = load_data()

#     return data

# # @app.get("/patients/{patient_id}")
# # def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve" , example="P0001")):
# #     data = load_data()
# #     if patient_id in data:
# #         return data[patient_id]
# #     raise HTTPException(status_code=404, detail="Patient not found")

# @app.get("/patients/{patient_id}")
# def view_patient(
#     patient_id: str = Path(
#         ...,
#         description="The ID of the patient to retrieve",
#         examples=["P0001"]
#     )
# ):
#     data = load_data()

#     for patient in data["patients"]:
#         if patient["patient_id"] == patient_id:
#             return patient

#     raise HTTPException(status_code=404, detail="Patient not found")


# # @app.get('/sort')
# # def sort_patients(sort_by : str = Query(..., description="The field to sort patients by age and gender", ), order: str = Query("asc", description="The order of sorting, either 'asc' for ascending or 'desc' for descending")):

# #     valid_field=["age", "gender","admission_date"]
# #     if sort_by not in valid_fields:
# #         raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {valid_fields}")
# #     if order not in ["asc", "desc"]:
# #         raise HTTPException(status_code=400, detail="Invalid order. Valid orders are: 'asc' or 'desc'")
# #     data = load_data()
# #     sort_order = False if order == "desc" else True
# #     sorted_patients = sorted(data.values(),key=lambda x:x.get(sort_by, 0 ), reverse=sort_order)
# #     return {"sorted_patients": sorted_patients}



# @app.get("/sort")
# def sort_patients(
#     sort_by: str = Query(
#         ...,
#         description="The field to sort patients by"
#     ),
#     order: str = Query(
#         "asc",
#         description="The order of sorting: 'asc' or 'desc'"
#     )
# ):
#     valid_fields = ["age", "gender", "admission_date"]

#     if sort_by not in valid_fields:
#         raise HTTPException(
#             status_code=400,
#             detail=f"Invalid sort field. Valid fields are: {valid_fields}"
#         )

#     if order not in ["asc", "desc"]:
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid order. Valid orders are: 'asc' or 'desc'"
#         )

#     data = load_data()

#     sort_order = True if order == "desc" else False

#     sorted_patients = sorted(
#         data["patients"],
#         key=lambda x: x.get(sort_by, 0),
#         reverse=sort_order
#     )

#     return {"sorted_patients": sorted_patients}





# from fastapi import FastAPI , Path , HTTPException , Query
# from pydantic import BaseModel, computed_field
# from typing import Annotated , Literal , Optional
# from fastapi.responses import JSONResponse
# import json
# app=FastAPI()
# class Patient(BaseModel):
#     patient_id: Annotated[str, Path(..., description="The ID of the patient", example="P0001")]
#     name: Annotated[str, Path(..., description="The name of the patient",)]
#     age: Annotated[int, Path(...,gt =0, lt=100, description="The age of the patient", example=30)]
#     gender: Annotated[Literal["Male", "Female"], Path(..., description="The gender of the patient",)]
#     admission_date: Annotated[str, Path(..., description="The admission date of the patient",)]

#     @computed_field
#     @property
#     def is_adult(self) -> bool:
#         return self.age >= 18

#     @computed_field
#     @property
#     def verdict(self) -> str:
#         if self.age < 18:
#             return "Minor"
#         elif self.age >= 18 and self.age < 60:
#             return "Adult"
#         else:
#             return "Senior"
#     @computed_field
#     @property
#     def bmi(self)->float:
#         bmi=round(self.weight/(self.height**2),2)
#         return bmi
# class PatientUpdate(BaseModel):
#         name: Annotated[Optional[str], Field(default=None)]
#         age: Annotated[Optional[int], Field(default=None)]
#         gender: Annotated[Optional[Literal['male','female']], Field(default=None)]
#         admission_date: Annotated[Optional[str], Field(default=None)]
    
    
# def load_data():
#     with open("patients.json", "r") as file:
#         data = json.load(file)
#     return data

# def save_data(data):
#     with open("patients.json", "w") as file:
#         json.dump(data, file)

# @app.get("/")
# def hello():
#     return {"message": "Patient Management System API"}

# @app.get("/about")
# def about():
#     return {"message": "This is a simple Patient Management System API built using FastAPI. It allows you to manage patient information and perform CRUD operations."}


# @app.get("/sort")
# def sort_patients(
#     sort_by: str = Query(
#         ...,
#         description="The field to sort patients by"
#     ),
#     order: str = Query(
#         "asc",
#         description="The order of sorting: 'asc' or 'desc'"
#     )
# ):
#     valid_fields = ["age", "gender", "admission_date"]

#     if sort_by not in valid_fields:
#         raise HTTPException(
#             status_code=400,
#             detail=f"Invalid sort field. Valid fields are: {valid_fields}"
#         )

#     if order not in ["asc", "desc"]:
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid order. Valid orders are: 'asc' or 'desc'"
#         )

#     data = load_data()

#     sort_order = True if order == "desc" else False

#     sorted_patients = sorted(
#         data["patients"],
#         key=lambda x: x.get(sort_by, 0),
#         reverse=sort_order
#     )

#     return {"sorted_patients": sorted_patients}

# @app.post('/create')
# def create_patient(patient: Patient):
#     data = load_data()
# # check if patient with the same ID already exists
#     if patient.id in data:
#         raise HTTPException(status_code=400, detail="Patient with this ID already exists")
# # add the new patient to the data
#     data[patient.id] = patient.model_dump(exclude={"id"})
#     # save into json file
#     save_data(data)

#     return JSONResponse(status_code=201, content={"message": "Patient created successfully"})



# @app.put("/edit/{patient_id}")
# def update_patient(patient_id:str , patient_update:PatientUpdate):


#     data=load_data()
#     if patient_id not in data:
#         raise HTTPException(status_code=404,details="Patients not found")
#     existingdata_patient_info=data[patient_id]

#     updated_patient_info=patient_update.model_dump(exclude_unset=True)

#     for key , value in updated_patient_info.items():
#         existingdata_patient_info[key]=value


#     existingdata_patient_info["id"]=patient_id
#     Patient_pydantic_obj=Patient(**existingdata_patient_info)

#     Patient_pydantic_info=Patient_pydantic_obj.model_dump(exclude='id')


#     data[patient_id]= existingdata_patient_info

#     save_data(data)

#     return JSONResponse(status_code=200,content={'message':'patient update'})






# from fastapi import FastAPI, HTTPException, Query
# from pydantic import BaseModel, Field, computed_field
# from typing import Annotated, Literal, Optional
# from fastapi.responses import JSONResponse
# import json


# app = FastAPI()


# # ============================================================
# # PATIENT MODEL
# # ============================================================

# class Patient(BaseModel):

#     patient_id: Annotated[
#         str,
#         Field(
#             ...,
#             description="The ID of the patient",
#             examples=["P0001"]
#         )
#     ]

#     name: Annotated[
#         str,
#         Field(
#             ...,
#             description="The name of the patient"
#         )
#     ]

#     age: Annotated[
#         int,
#         Field(
#             ...,
#             gt=0,
#             lt=100,
#             description="The age of the patient",
#             examples=[30]
#         )
#     ]

#     gender: Annotated[
#         Literal["Male", "Female"],
#         Field(
#             ...,
#             description="The gender of the patient"
#         )
#     ]

#     height: Annotated[
#         float,
#         Field(
#             ...,
#             gt=0,
#             description="Height of the patient in meters",
#             examples=[1.75]
#         )
#     ]

#     weight: Annotated[
#         float,
#         Field(
#             ...,
#             gt=0,
#             description="Weight of the patient in kilograms",
#             examples=[70.0]
#         )
#     ]

#     diagnosis: Annotated[
#         str,
#         Field(
#             ...,
#             description="Diagnosis of the patient"
#         )
#     ]

#     blood_group: Annotated[
#         str,
#         Field(
#             ...,
#             description="Blood group of the patient"
#         )
#     ]

#     admission_date: Annotated[
#         str,
#         Field(
#             ...,
#             description="Admission date of the patient"
#         )
#     ]

#     # ========================================================
#     # COMPUTED FIELD: BMI
#     # ========================================================

#     @computed_field
#     @property
#     def bmi(self) -> float:
#         return round(
#             self.weight / (self.height ** 2),
#             2
#         )

#     # ========================================================
#     # COMPUTED FIELD: IS ADULT
#     # ========================================================

#     @computed_field
#     @property
#     def is_adult(self) -> bool:
#         return self.age >= 18

#     # ========================================================
#     # COMPUTED FIELD: VERDICT
#     # ========================================================

#     @computed_field
#     @property
#     def verdict(self) -> str:

#         if self.age < 18:
#             return "Minor"

#         elif self.age < 60:
#             return "Adult"

#         else:
#             return "Senior"


# # ============================================================
# # PATIENT UPDATE MODEL
# # ============================================================

# class PatientUpdate(BaseModel):

#     name: Annotated[
#         Optional[str],
#         Field(default=None)
#     ]

#     age: Annotated[
#         Optional[int],
#         Field(
#             default=None,
#             gt=0,
#             lt=100
#         )
#     ]

#     gender: Annotated[
#         Optional[Literal["Male", "Female"]],
#         Field(default=None)
#     ]

#     height: Annotated[
#         Optional[float],
#         Field(
#             default=None,
#             gt=0
#         )
#     ]

#     weight: Annotated[
#         Optional[float],
#         Field(
#             default=None,
#             gt=0
#         )
#     ]

#     diagnosis: Annotated[
#         Optional[str],
#         Field(default=None)
#     ]

#     blood_group: Annotated[
#         Optional[str],
#         Field(default=None)
#     ]

#     admission_date: Annotated[
#         Optional[str],
#         Field(default=None)
#     ]


# # ============================================================
# # LOAD DATA
# # ============================================================

# def load_data():

#     with open("patients_updated.json", "r") as file:
#         data = json.load(file)

#     return data


# # ============================================================
# # SAVE DATA
# # ============================================================

# def save_data(data):

#     with open("patients_updated.json", "w") as file:
#         json.dump(
#             data,
#             file,
#             indent=4
#         )


# # ============================================================
# # HOME
# # ============================================================

# @app.get("/")
# def hello():

#     return {
#         "message": "Patient Management System API"
#     }


# # ============================================================
# # ABOUT
# # ============================================================

# @app.get("/about")
# def about():

#     return {
#         "message": (
#             "This is a simple Patient Management System API "
#             "built using FastAPI. It allows you to manage "
#             "patient information and perform CRUD operations."
#         )
#     }


# # ============================================================
# # GET ALL PATIENTS
# # ============================================================

# @app.get("/patients")
# def get_all_patients():

#     data = load_data()

#     return data["patients"]


# # ============================================================
# # GET SINGLE PATIENT
# # ============================================================

# @app.get("/patients/{patient_id}")
# def get_patient(patient_id: str):

#     data = load_data()

#     for patient in data["patients"]:

#         if patient["patient_id"] == patient_id:

#             return patient

#     raise HTTPException(
#         status_code=404,
#         detail="Patient not found"
#     )


# # ============================================================
# # SORT PATIENTS
# # ============================================================

# @app.get("/sort")
# def sort_patients(
#     sort_by: str = Query(
#         ...,
#         description="The field to sort patients by"
#     ),
#     order: str = Query(
#         "asc",
#         description="The order of sorting: asc or desc"
#     )
# ):

#     valid_fields = [
#         "age",
#         "gender",
#         "admission_date",
#         "height",
#         "weight",
#         "bmi"
#     ]

#     if sort_by not in valid_fields:

#         raise HTTPException(
#             status_code=400,
#             detail=f"Invalid sort field. Valid fields are: {valid_fields}"
#         )

#     if order not in ["asc", "desc"]:

#         raise HTTPException(
#             status_code=400,
#             detail="Invalid order. Valid orders are: 'asc' or 'desc'"
#         )

#     data = load_data()

#     sorted_patients = sorted(
#         data["patients"],
#         key=lambda x: x.get(sort_by, 0),
#         reverse=(order == "desc")
#     )

#     return {
#         "sorted_patients": sorted_patients
#     }


# # ============================================================
# # CREATE PATIENT
# # ============================================================

# @app.post("/create")
# def create_patient(patient: Patient):

#     data = load_data()

#     # Check duplicate patient ID

#     for existing_patient in data["patients"]:

#         if existing_patient["patient_id"] == patient.patient_id:

#             raise HTTPException(
#                 status_code=400,
#                 detail="Patient with this ID already exists"
#             )

#     # Add patient

#     patient_data = patient.model_dump(
#         exclude={"bmi", "is_adult", "verdict"}
#     )

#     data["patients"].append(patient_data)

#     save_data(data)

#     return JSONResponse(
#         status_code=201,
#         content={
#             "message": "Patient created successfully",
#             "patient": patient.model_dump()
#         }
#     )


# # ============================================================
# # UPDATE PATIENT
# # ============================================================

# @app.put("/edit/{patient_id}")
# def update_patient(
#     patient_id: str,
#     patient_update: PatientUpdate
# ):

#     data = load_data()

#     # Find patient inside the patients list
#     for patient in data["patients"]:

#         if patient["patient_id"] == patient_id:

#             # Get only fields that were provided
#             updated_data = patient_update.model_dump(
#                 exclude_unset=True
#             )

#             # Update patient fields
#             for key, value in updated_data.items():

#                 if value is not None:
#                     patient[key] = value

#             # Validate updated patient
#             updated_patient = Patient(**patient)

#             # Save only actual stored fields
#             patient.update(
#                 updated_patient.model_dump(
#                     exclude={
#                         "bmi",
#                         "is_adult",
#                         "verdict"
#                     }
#                 )
#             )

#             save_data(data)

#             return {
#                 "message": "Patient updated successfully",
#                 "patient": updated_patient.model_dump()
#             }

#     # Patient was not found
#     raise HTTPException(
#         status_code=404,
#         detail="Patient not found"
#     )


# # ============================================================
# # DELETE PATIENT
# # ============================================================

# @app.delete("/delete/{patient_id}")
# def delete_patient(patient_id: str):

#     data = load_data()

#     for index, patient in enumerate(data["patients"]):

#         if patient["patient_id"] == patient_id:

#             deleted_patient = data["patients"].pop(index)

#             save_data(data)

#             return {
#                 "message": "Patient deleted successfully",
#                 "patient": deleted_patient
#             }

#     raise HTTPException(
#         status_code=404,
#         detail="Patient not found"
#     )















from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
from fastapi.responses import JSONResponse

import pickle
import pandas as pd


# ============================================================
# LOAD ML MODEL
# ============================================================

MODEL_PATH = r"C:\Users\HP\OneDrive\Desktop\FastAPI\model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


app = FastAPI(
    title="Insurance Premium Prediction API",
    description="ML API for insurance premium category prediction",
    version="1.0"
)


# ============================================================
# CITY TIERS
# ============================================================

tier1 = {
    "Delhi",
    "Mumbai",
    "Bengaluru",
    "Chennai",
    "Hyderabad",
    "Pune",
    "Kolkata",
    "Ahmedabad"
}

tier2 = {
    "Chandigarh",
    "Jaipur",
    "Lucknow",
    "Amritsar"
}


# ============================================================
# INPUT MODEL
# ============================================================

class UserInput(BaseModel):

    age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=120,
            description="Age of the user"
        )
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Weight in kilograms"
        )
    ]

    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            lt=2.5,
            description="Height in meters"
        )
    ]

    income_lpa: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Annual income in LPA"
        )
    ]

    smoker: Annotated[
        bool,
        Field(
            ...,
            description="Whether the user is a smoker"
        )
    ]

    city: Annotated[
        str,
        Field(
            ...,
            description="City of the user"
        )
    ]

    occupation: Annotated[
        Literal[
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job"
        ],
        Field(
            ...,
            description="Occupation of the user"
        )
    ]


    # ========================================================
    # BMI
    # ========================================================

    @computed_field
    @property
    def bmi(self) -> float:

        return round(
            self.weight / (self.height ** 2),
            2
        )


    # ========================================================
    # LIFESTYLE RISK
    # ========================================================

    @computed_field
    @property
    def lifestyle_risk(self) -> str:

        if self.smoker and self.bmi > 30:
            return "high"

        elif self.smoker or self.bmi > 27:
            return "medium"

        else:
            return "low"


    # ========================================================
    # AGE GROUP
    # ========================================================

    @computed_field
    @property
    def age_group(self) -> str:

        if self.age <= 25:
            return "young"

        elif self.age <= 35:
            return "adult"

        else:
            return "middle aged"


    # ========================================================
    # CITY TIER
    # ========================================================

    @computed_field
    @property
    def city_tier(self) -> int:

        if self.city in tier1:
            return 1

        elif self.city in tier2:
            return 2

        else:
            return 3


# ============================================================
# PREDICTION API
# ============================================================

@app.post("/predict")
def predict_premium(data: UserInput):

    input_df = pd.DataFrame([
        {
            "bmi": data.bmi,
            "age_group": data.age_group,
            "lifestyle_risk": data.lifestyle_risk,
            "city_tier": data.city_tier,
            "income_lpa": data.income_lpa,
            "occupation": data.occupation
        }
    ])

    prediction = model.predict(input_df)[0]

    return JSONResponse(
        status_code=200,
        content={
            "predicted_category": prediction,
            "bmi": data.bmi,
            "age_group": data.age_group,
            "lifestyle_risk": data.lifestyle_risk,
            "city_tier": data.city_tier
        }
    )