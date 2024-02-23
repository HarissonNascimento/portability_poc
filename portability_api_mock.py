from fastapi import FastAPI
from pydantic import BaseModel

class Enterprise(BaseModel):
    name: str
    cnpj: str
    address: str

class AccountData(BaseModel):
    user_name: str
    cpf: str
    agency: str
    account: str
    dac: str
    bank_code: str
    enterprise: Enterprise

class ResponseData(BaseModel):
    message: str
    data: AccountData

app = FastAPI()

@app.post("/effect_portability")
def effect_portability(portability_data: AccountData):
    return ResponseData(message='Portabilidade solicitada com sucesso!', data=portability_data)
    # return {'message': 'Portabilidade solicitada com sucesso!', 'data': '{portability_data}'}