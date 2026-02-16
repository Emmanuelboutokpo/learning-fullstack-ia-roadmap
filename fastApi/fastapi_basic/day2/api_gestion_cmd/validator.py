from pydantic import BaseModel, Field
from typing import Annotated, List, Optional

class OrderItem(BaseModel) :
    item_id : Annotated[Optional[str], Field(default=None, description="Item de la commande")]
    size : Annotated[str, Field(..., description="Taille de la commande", pattern="^(S|M|L)$")]
    supplements : Annotated[List[str], Field(..., description="Liste des suppléments de la commande")]
    qty : Annotated[int, Field(..., description="Quantité de la commande")]

class OrderDrink(BaseModel) :
    drink_id : Annotated[Optional[str], Field(default=None, description="Boisson de la commande")]
    qty : Annotated[int, Field(..., description="Quantité de la commande")]


class Order(BaseModel) :
    id : Annotated[Optional[str], Field(default=None, description="ID de la commande")]
    items : Annotated[List[OrderItem], Field(..., description="Liste des items de la commande")]
    drinks : Annotated[List[OrderDrink], Field(..., description="Liste des boissons de la commande")]
 