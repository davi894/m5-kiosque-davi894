from management import get_product_by_id


def calculate_tab(comandas):

    value = 0

    for item in comandas:
        product = get_product_by_id(item["_id"])
        print(product)
        value += product["price"] * item["amount"]

    valeuTratado = round(value.real, 2)

    return {f'subtotal': f'${valeuTratado}'}
