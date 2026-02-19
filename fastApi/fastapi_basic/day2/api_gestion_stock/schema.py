from pydantic import BaseModel, Field, computed_field
from typing import Optional, Annotated

class Product(BaseModel):
    id : Annotated[Optional[str], Field(default=None, description="The unique identifier of the product", example="P001")]
    name : Annotated[str, Field(..., description="The name of the product", example="Laptop", min_length=3, max_length=50)]
    category : Annotated[str, Field(...,description="The category of the product", example="Electronics", min_length=3, max_length=30)]
    price : Annotated[float, Field(...,description="The price of the product", example=999.99, gt=0)] 
    quantity : Annotated[int, Field(...,description="The available quantity of the product", example=10, ge=0)]
    supplier : Annotated[str, Field(...,description="The supplier of the product", example="Tech Supplier Inc.", min_length=3, max_length=50)]
    reorder_level : Annotated[int, Field(...,description="The quantity at which the product should be reordered", example=5, ge=0)]
    
    @computed_field
    @property
    def in_stock(self) -> bool:
        if self.quantity > 0:
            return True
        else:
            return False
