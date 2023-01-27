from menu import products
import json


def get_product_by_id(_id):

    id = type(_id)

    if id is not int:
        raise TypeError("product id must be an int")

    result = []

    for item in products:
        if item["_id"] == _id:
            result.append(item)

    if result == []:
        return {}

    return result[0]


def get_products_by_type(typeProduct):

    tipo = type(typeProduct)

    if tipo is not str:
        raise TypeError("product type must be a str")

    list = []

    for itens in products:
        if itens["type"] == typeProduct:
            list.append(itens)

    if list == []:
        return []

    return list


def add_product(array, **objProduct):

    arr_index = []

    if array == []:
        key, value = '_id', 1
        objProduct.update({key: value})
        array.append(objProduct)
        return objProduct

    for itens in array:
        arr_index.append(itens["_id"])

    index_update = max(arr_index) + 1

    key, value = '_id', index_update
    objProduct.update({key: value})
    array.append(objProduct)

    return objProduct


def contagem_de_tipos(lista):
    array_tipo_e_contagem = []

    for listaItem in lista:
        array_tipo_e_contagem.append(listaItem.split(","))

    array_number_maior = []

    for x in array_tipo_e_contagem:
        array_number_maior.append(int(x[1]))

    maior_numero_contagem_tipos = max(array_number_maior)

    type = ""

    for x in array_tipo_e_contagem:
        if int(x[1]) == maior_numero_contagem_tipos:
            type += x[0]

    return type


def menu_report():

    contagem_de_produtos = len(list(products))
    value = 0
    tipos = []

    for itens in products:
        tipos.append(itens["type"])
        value += itens["price"]

    tipos.sort()

    selecionando_quantidade_e_tipo = []

    for itens in tipos:
        selecionando_quantidade_e_tipo.append(f'{itens},{tipos.count(itens)}')

    retirando_valores_repetidos = list(
        set(selecionando_quantidade_e_tipo))

    typeFinal = contagem_de_tipos(retirando_valores_repetidos)

    preco_medio = round((value / contagem_de_produtos).real, 2)

    return f'Products Count: {contagem_de_produtos} - Average Price: ${preco_medio} - Most Common Type: {typeFinal}'


def add_product_extra(products_list, *required_keys_args, **new_product_args):

    arr_verify_keys_required = []

    for keys_required in required_keys_args:
        for new_keys in new_product_args:
            if keys_required == new_keys:
                arr_verify_keys_required.append(new_keys)

    if len(arr_verify_keys_required) < len(required_keys_args):
        raise KeyError("field rating is required")

    arr_index = []

    if products_list == []:
        key, value = '_id', 1
        new_product_args.update({key: value})
        products_list.append(new_product_args)
        return new_product_args

    for itens in products_list:
        arr_index.append(itens["_id"])

    index_update = max(arr_index) + 1

    key, value = '_id', index_update
    new_product_args.update({key: value})
    products_list.append(new_product_args)

    return new_product_args
