from fastapi import FastAPI, HTTPException, Query
from  fastapi.responses import JSONResponse
from validator import Todo
import uuid

app = FastAPI()

todos = []

@app.get("/todos")
async def root(sorted_by: str = Query(default=None, description="sort by field", examples="id, title, description, completed"),
            order: str = Query("asc", description="sort order", examples="asc, desc")) :
    
    result = todos
    if sorted_by is not None :
        if sorted_by not in ['id', 'title', 'description', 'completed'] :
           raise HTTPException(status_code=400, detail="Invalid sort field")
    
        if order not in ['asc', 'desc'] :
           raise HTTPException(status_code=400, detail="Invalid sort order")

        sorted_orders = False if order == 'desc' else True
        result = sorted(todos, key=lambda x: x[sorted_by], reverse=sorted_orders) 

    return JSONResponse(content=result, status_code=200)


@app.get("/todos/{todo_id}")
async def get_todo(todo_id: str) :
    for todo in todos :
        if todo['id'] == todo_id :
            return JSONResponse(content=todo, status_code=200)
    raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/todos")
async def create_todo(todo : Todo) : 
    nouvel_id= str(uuid.uuid4())
    todo_dict = todo.model_dump()
    todo_dict['id'] = nouvel_id
    todos.append(todo_dict)
    return JSONResponse(content={"message": "Todo created successfully"}, status_code=201)


@app.put("/todos/{todo_id}")
async def update_todo(todo_id: str, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo['id'] == todo_id:
            updated_dict = updated_todo.model_dump(exclude_unset=True)
            todo.update(updated_dict)
            todo['id'] = todo_id
            return JSONResponse(content={"message": "Todo updated successfully"}, status_code=200)
    
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str) :
    for index, todo in enumerate(todos) :
        if todo['id'] == todo_id :
            del todos[index]
            return JSONResponse(content={"message": "Todo deleted successfully"}, status_code=200)
    raise HTTPException(status_code=404, detail="Todo not found")


    