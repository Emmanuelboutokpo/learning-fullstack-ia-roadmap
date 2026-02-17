# 🏥 Patient Management API (FastAPI)

A simple **Patient Management REST API** built with **FastAPI**.
This project allows you to **create, read, update, delete, and sort patients**, while automatically calculating **BMI** and **weight category** using Pydantic computed fields.

---

## 🎯 Project Goal

The goal of this project is to practice:

* Building REST APIs with FastAPI
* Using **Path parameters** and **Query parameters**
* Data validation with **Pydantic models**
* Automatic computed fields (BMI & weight category)
* JSON file storage instead of a database
* Error handling with HTTPException

---

## 🚀 Features

✅ Get all patients
✅ Get patient by ID
✅ Sort patients by height / weight / bmi
✅ Create new patient
✅ Update existing patient
✅ Delete patient
✅ Automatic BMI calculation
✅ Automatic weight classification

---

## 🛠 Tech Stack

* Python
* FastAPI
* Pydantic
* JSON file storage

---

## 📂 Project Structure

```
project/
│
├── main.py              # FastAPI application
├── validator.py         # Pydantic models & validation
├── patients.json        # Local data storage
├── requirements.txt
└── README.md
```

---

## ▶️ Installation & Run

### 1️⃣ Clone the repository

```
https://github.com/Emmanuelboutokpo/learning-fullstack-ia-roadmap.git
cd patient-fastapi
```

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```
pip install "fastapi[standard]"
```

### 4️⃣ Run the server

```
fastapi dev main.py

```

---

## 📚 API Documentation

After running the server, open:

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

## 🔌 API Endpoints

### 📌 Get all patients

```
GET /patients
```

### 📌 Get patient by ID

```
GET /patients/{patient_id}
```

Example:

```
GET /patients/P001
```

---

### 📌 Sort patients

```
GET /sort?sorted_by=height&order=asc
```

Query parameters:

* `sorted_by` → height | weight | bmi
* `order` → asc | desc

---

### 📌 Create patient

```
POST /create
```

Example body:

```
{
  "id": "P010",
  "name": "John Doe",
  "city": "Cotonou",
  "age": 25,
  "gender": "Male",
  "height": 175,
  "weight": 70
}
```

---

### 📌 Update patient

```
PUT /update/{patient_id}
```

Example:

```
PUT /update/P010
```

Body (partial allowed):

```
{
  "weight": 75
}
```

---

### 📌 Delete patient

```
DELETE /delete/{patient_id}
```

---

## 🧠 Automatic Calculations

The API automatically computes:

### ✔ BMI

```
BMI = weight / (height_in_meters²)
```

### ✔ Weight Category

| BMI     | Category      |
| ------- | ------------- |
| < 18    | Underweight   |
| 18–24.9 | Normal weight |
| 25–29.9 | Overweight    |
| ≥ 30    | Obese         |

---

## 💡 What I Learned

* Building CRUD APIs with FastAPI
* Using Pydantic advanced validation
* Computed fields with `@computed_field`
* Handling JSON as a mini database
* Structuring endpoints properly
* Returning custom HTTP responses

---

## 🔮 Future Improvements

* Add real database (PostgreSQL / SQLite)
* Add authentication (JWT)
* Dockerize the project
* Deploy online (Render / Railway)
* Add unit tests

---

## 👨‍💻 Author

Built as part of my journey to become a **Full-Stack AI Engineer** through daily project practice.

If you have feedback or suggestions, feel free to connect 🙂
