# 📦 Stock Management API (FastAPI)

A simple **Stock Management REST API** built with **FastAPI** that allows you to manage products in inventory.

This API supports:

* Viewing all products
* Sorting products
* Getting a product by ID
* Creating a new product
* Deleting a product
* Automatic request validation with Pydantic

---

## 🎯 Project Purpose

This project was created to practice:

* Building REST APIs with FastAPI
* Using Path & Query parameters
* Request validation with Pydantic schemas
* Generating unique IDs with UUID
* Handling HTTP errors properly
* Creating custom validation exception handlers

---

## 🛠 Tech Stack

* Python
* FastAPI
* Pydantic
* UUID
* In-memory dictionary storage

---

## 📂 Project Structure

```
project/
│
├── main.py        # FastAPI app & routes
├── bd.py          # stock dictionary (fake database)
├── schema.py      # Product Pydantic model
├── requirements.txt
└── README.md
```

---

## ▶️ Installation & Run

### 1️⃣ Clone repository

```
git clone https://github.com/Emmanuelboutokpo/learning-fullstack-ia-roadmap/tree/master/fastApi/fastapi_basic/day2/
cd stock-fastapi
```

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```
pip install fastapi uvicorn
```

### 4️⃣ Run server

```
uvicorn main:app --reload
```

---

## 📚 API Documentation

After starting the server:

* Swagger UI → http://127.0.0.1:8000/docs
* ReDoc → http://127.0.0.1:8000/redoc

---

## 🔌 API Endpoints

---

### 📌 Get all products

```
GET /api/products
```

Optional query parameters:

| Parameter | Description      | Example |
| --------- | ---------------- | ------- |
| sorted_by | Field to sort by | price   |
| order     | asc or desc      | desc    |

Example:

```
GET /api/products?sorted_by=price&order=desc
```

Valid fields:

```
name, category, price, quantity, in_stock
```

---

### 📌 Get product by ID

```
GET /api/product/{product_id}
```

Example:

```
GET /api/product/PR001
```

Response:

```
{
  "data": {
    "name": "Laptop HP EliteBook",
    "price": 850,
    "quantity": 12
  }
}
```

---

### 📌 Create product

```
POST /api/products
```

Example request body:

```
{
  "name": "Gaming Mouse",
  "category": "Accessories",
  "price": 45.5,
  "quantity": 20,
  "in_stock": true
}
```

Response:

```
{
  "message": "Product created successfully",
  "id": "generated-uuid",
  "data": {...}
}
```

A unique **UUID** is automatically generated for each product.

---

### 📌 Delete product

```
DELETE /api/product/{product_id}
```

Example:

```
DELETE /api/product/PR001
```

---

## ⚠️ Error Handling

The API returns proper HTTP status codes:

| Code | Meaning           |
| ---- | ----------------- |
| 200  | Success           |
| 201  | Created           |
| 400  | Bad request       |
| 404  | Product not found |
| 422  | Validation error  |

Validation errors return:

```
{
  "detail": [...],
  "body": {...}
}
```

---

## 🧠 What I Learned

* Designing REST endpoints with FastAPI
* Query-based sorting logic
* Using UUID for unique identifiers
* Structuring small backend projects
* Handling validation errors globally
* Returning consistent JSON responses

---

## 🔮 Possible Improvements

* Add UPDATE endpoint (PUT / PATCH)
* Replace dictionary with SQLite/PostgreSQL
* Add authentication (JWT)
* Add pagination
* Add unit tests with pytest
* Dockerize the application
* Deploy online

---

## 👨‍💻 Author

Built as part of my journey to become a **Full-Stack AI Engineer** through hands-on projects and daily practice.

Feedback and suggestions are welcome 🙂
