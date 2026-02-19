from fastapi import FastAPI, HTTPException, Request, status, Query, Path
from fastapi.exceptions import RequestValidationError
import uuid
from fastapi.responses import JSONResponse
from bd import stock
from schema import Product

app = FastAPI()

@app.get("/api/products")
async def get_stock(sorted_by: str = Query(default=None, description="The field to sort by (name, category, price, quantity, in_stock)", examples="name, category, price, quantity, in_stock"),
order: str = Query("asc", description="The sort order (asc or desc)", examples="asc")) :
    
    valid_sort_fields = ["name", "category", "price", "quantity", "in_stock"]
    if sorted_by not in valid_sort_fields:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid sort field. Valid options are: {', '.join(valid_sort_fields)}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid sort order. Must be 'asc' or 'desc'.")
    
    sorted_order = False if order == "asc" else True
    
    sorted_stock = sorted(stock.values(), key=lambda x: x[sorted_by], reverse=sorted_order)
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": sorted_stock}) 


@app.get("/api/product/{product_id}")
async def get_product(product_id: str = Path(..., description="The ID of the product to retrieve", examples="P001")) : 
     product = stock.get(product_id)
     if product:
       return JSONResponse(status_code=status.HTTP_200_OK, content={"data": product})
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

@app.post("/api/products")
async def post_product(product: Product):
    product_id = str(uuid.uuid4())
    
    if product_id in stock:
        raise HTTPException(status_code=400, detail="Product already exists")
    
    product_dict = product.model_dump(exclude={"id"})
    product_dict["id"] = product_id  # Ajouter l'ID généré
    stock.update({product_id: product_dict})
    
    return JSONResponse(
        status_code=201,
        content={"message": "Product created successfully", "id": product_id, "data": product_dict}
    )


@app.delete("/api/product/{product_id}")
async def delete_product(product_id: str = Path(..., description="The ID of the product to delete", examples="P001")):
    if product_id in stock:
        del stock[product_id]
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Product deleted successfully"})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body},
    )