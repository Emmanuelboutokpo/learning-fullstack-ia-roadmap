from pydantic import BaseModel, Field, computed_field
from typing import Optional, Annotated, Literal

class User(BaseModel):
    id: Annotated[str, Field(..., min_length=3, max_length=10)]
    name: Annotated[str, Field(..., min_length=3, max_length=50)]
    city : Annotated[Optional[str], Field(..., description="The city of the user")]
    age: Annotated[int, Field(..., gt=0, lt=120)]
    gender: Annotated[Literal["Male", "Female", "Other"], Field(..., description="The gender of the user")]
    height : Annotated[float, Field(..., gt=0.0)]
    weight : Annotated[float, Field(..., gt=0.0)]
    
    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100
        return self.weight / (height_in_meters ** 2)
    
    @computed_field
    @property
    def weight_category(self) -> str:
        if self.bmi < 18:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal weight'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'


class UserUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city : Annotated[Optional[str], Field(default=None, description="The city of the user")]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120)]
    gender: Annotated[Optional[Literal["Male", "Female", "Other"]], Field(default=None)]
    height : Annotated[Optional[float], Field(default=None, gt=0.0)]
    weight : Annotated[Optional[float], Field(default=None, gt=0.0)]
 