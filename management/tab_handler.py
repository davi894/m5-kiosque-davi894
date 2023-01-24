from management import get_product_by_id
import json


def calculate_tab(comandas):

    value = 0

    for item in comandas:
        object = json.dumps(item)
        index = json.loads(object)["_id"]
        amount = json.loads(object)["amount"]
        value += get_product_by_id(index)["price"]*amount
        
    valeuTratado = round(value.real, 2)
    
    return {f'subtotal': f'${valeuTratado}'}
