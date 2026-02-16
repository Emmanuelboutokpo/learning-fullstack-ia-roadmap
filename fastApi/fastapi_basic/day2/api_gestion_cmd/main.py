from fastapi  import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uuid
import json
from validator import *

app = FastAPI()

orders = []

def get_data() : 
    with open("menu.json", "r") as f : 
        data = json.load(f)
    return  data

@app.get("/menu")
async def menu() : 
    data = get_data()
    return data

@app.post("/order")
async def order(order : Order) : 
    data = get_data()
    nouvel_id= str(uuid.uuid4())
    order_dict = []

    for item in order.items : 
        item_found = False
        for i in data["items"] : 
            if i["id"] == item.item_id : 
                item_found = True
                order_dict.append({"item" : {
                    "name": i["name"],
                    "size": item.size,
                    "supplements": item.supplements
                }, "quantity" : item.qty})
                break
        if not item_found :
            return JSONResponse(content={"message" : f"Item {item.item_id} not found in menu"}, status_code=404)

    for drink in order.drinks : 
        drink_found = False
        for d in data["drinks"] : 
            if d["id"] == drink.drink_id : 
                drink_found = True
                order_dict.append({"drink" : {
                    "name": d["name"],
                    "quantity" : drink.qty
                 }, 
                })
                break
        if not drink_found :
            return JSONResponse(content={"message" : f"Drink {drink.drink_id} not found in menu"}, status_code=404)
    orders.append({"id": nouvel_id, "order" : order_dict})
    return JSONResponse(content={"message" : f"Order {nouvel_id} created successfully"}, status_code=201)
    

@app.post("/order/total")
async def calculate_total(order: Order):
    data = get_data()
    total = 0
    
    for item in order.items:
       
        item_found = False
        for i in data["items"]:
            if i["id"] == item.item_id:
                item_found = True
              
                price = i["base_price"]
                if item.size == "S":
                    price += i["sizes"]["S"]
                elif item.size == "M":
                    price += i["sizes"]["M"]
                elif item.size == "L":
                    price += i["sizes"]["L"]
                for supplement in item.supplements:
                    for s in i["supplements"]:
                        if s["name"] == supplement:
                            price += s["price"]
                            break
                
                price *= item.qty
                
                total += price
                break
        if not item_found:
            return JSONResponse(content={"message": f"Item {item.item_id} not found in menu"}, status_code=404)
    
    for drink in order.drinks :
        drink_found = False
        for d in data["drinks"] : 
            if d["id"] == drink.drink_id : 
                drink_found = True
                price = d["price"] * drink.qty
                total += price
                break
        if not drink_found :
            return JSONResponse(content={"message" : f"Drink {drink.drink_id} not found in menu"}, status_code=404)
      
    
    return {"total": total}