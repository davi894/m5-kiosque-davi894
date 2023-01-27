from management import (
    get_product_by_id,
    get_products_by_type,
    add_product,
    calculate_tab,
    menu_report,
    add_product_extra
)

from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    ...
new_product = {
    "title": "X-Python",
    "price": 5.0,
    "rating": 5,
    "description": "Sanduiche de Python",
    "type": "fast-food"
}

required_keys = ("description", "price", "rating", "title", "type")

new_product_extra = {
    "title": "X-Python",
    "price": 5.0,
    "rating": 5,
    "description": "Sanduiche de Python",
    "type": "fast-food",
    "extra_key_1": "extra_value_1",
    "extra_key_2": "extra_value_2"
}

table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
table_2 = [
    {"_id": 10, "amount": 3},
    {"_id": 20, "amount": 2},
    {"_id": 21, "amount": 5},
]

menu_empty = []

print(get_product_by_id(28))
print(get_products_by_type('drink'))
print(menu_report())
print(calculate_tab(table_1))
print(calculate_tab(table_2))
print(add_product(products, **new_product))
print(add_product(menu_empty, **new_product))
print(add_product_extra(menu_empty, *required_keys, **new_product_extra))
print(add_product_extra(products, *required_keys, **new_product_extra))


def verify_get_product_id():

    try:
        return get_product_by_id(28)
    except TypeError as erro:
        return erro


def verify_get_product_by_type():

    try:
        return get_products_by_type('drink')
    except TypeError as erro:
        return erro


def verify_add_product_extra_products():

    try:
        return add_product_extra(products, *required_keys, **new_product_extra)
    except KeyError as erro:
        return erro


def verify_add_product_extra_menu_empty():

    try:
        return add_product_extra(menu_empty, *required_keys, **new_product_extra)
    except KeyError as erro:
        return erro
