from menu import products
from collections import Counter
import json


def get_product_by_id(_id):

    result = []

    for item in products:
        object = json.dumps(item)
        index = json.loads(object)["_id"]
        if index == _id:
            result.append(item)

    if result == []:
        return {}

    return result[0]


def get_products_by_type(typeProduct):
    list = []

    for itens in products:
        object = json.dumps(itens)
        type = json.loads(object)["type"]
        if type == typeProduct:
            list.append(itens)

    if list == []:
        return []

    return list


def add_product(list, objProduct):

    arrIndex = []

    if list == []:
        key, value = '_id', 1
        objProduct.update({key: value})
        list.append(objProduct)
        return objProduct

    for itens in products:
        object = json.dumps(itens)
        index = json.loads(object)["_id"]
        arrIndex.append(index)

    indexUpdate = max(arrIndex) + 1

    key, value = '_id', indexUpdate
    objProduct.update({key: value})
    list.append(objProduct)

    return objProduct


def continuacao(lista):
    arrayTipoEContagem = []

    for listaItem in lista:
        arrayTipoEContagem.append(listaItem.split(","))

    arrayNumberMaior = []

    for x in arrayTipoEContagem:
        arrayNumberMaior.append(int(x[1]))

    maiorNumeroDosTipos = max(arrayNumberMaior)

    type = ""

    for x in arrayTipoEContagem:
        if int(x[1]) == maiorNumeroDosTipos:
            type += x[0]

    return type


def menu_report():

    contagem_de_produtos = len(list(products))
    value = 0
    tipos = []

    for itens in products:
        object = json.dumps(itens)
        price = json.loads(object)["price"]
        type = json.loads(object)["type"]
        tipos.append(type)
        value += price

    tipos.sort()

    selecionandoQuantidadeETipagem = []

    for itens in tipos:
        selecionandoQuantidadeETipagem.append(f'{itens},{tipos.count(itens)}')

    retirandoValoresRepetidosDosTypes = list(
        set(selecionandoQuantidadeETipagem))

    typeFinal = continuacao(retirandoValoresRepetidosDosTypes)

    preco_medio = round((value / contagem_de_produtos).real, 2)

    return f'Products Count: {contagem_de_produtos} - Average Price: ${preco_medio} - Most Common Type: {typeFinal}'


# Product Count: Contagem do total de produtos do menu.
# Average Price: Média dos preços de todos os produtos do
# menu, arredondada para 2 casas decimais no máximo.
# Most Common Type: O tipo de produto mais comum, ou seja, o tipo
# que contém maior quantidade de produtos no menu.
# O retorno deve ser uma string formatada exatamente
# como no exemplo abaixo, com o devido dinamismo de
# cada característica:
# "Products
# Count: <contagem_de_produtos> -
# Average Price: $<preco_medio> -
# Most Common Type: <tipo_mais_comum>"
