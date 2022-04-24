from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from lib import delivery_fee_calculator

app = FastAPI()


class Request(BaseModel):
	cart_value: int
	delivery_distance: int
	number_of_items: int
	time: datetime

# {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}


@app.post("/calculate")
async def root(request: Request):
	res = delivery_fee_calculator.calc_delivery_fee(request.cart_value, request.delivery_distance, request.number_of_items, request.time)
	return {"delivery_fee": res}













