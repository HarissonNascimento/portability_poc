from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# class Enterprise:
#     def __init__(self, name, cnpj, address,):
#         self.name = name
#         self.cnpj = cnpj
#         self.address = address

# class AccountData:
#     def __init__(self, user_name, cpf, agency, account, dac, bank_code, enterprise,):
#         self.user_name = user_name
#         self.cpf = cpf
#         self.agency = agency
#         self.account = account
#         self.dac = dac
#         self.bank_code = bank_code
#         self.enterprise = enterprise

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
    data: AccountData

app = FastAPI()

@app.get("/account_data", response_model=ResponseData)
def account_data():
    account_data = AccountData(
        user_name = 'João',
        cpf = '14785692465',
        agency = '2526',
        account = '54786',
        dac = '1',
        bank_code = '237',
        enterprise = Enterprise(
            name = 'Empresa Mock Filial 1 - LTDA',
            cnpj = '12345678000200',
            address = 'Rua Mock',
        ),
        )
    # return {'data': account_data}
    response = ResponseData(data=account_data)
    return response