from operator import truediv


cart = []
exe = True

id_user = input('Insira o id do usuario: ')

def add_item_cart(item):
    cart.append(item)

def get_all_items_cart():
    print('Id do usuario: ', id_user)
    for item in cart:
        print('---------------------------')
        print(f'Id do produto: {item[1]}\nPreço: {item[2]}\nQuantidade: {item[3]}')

def print_item(item):
    print(f'Id do produto: {item[1]}\nPreço: {item[2]}\nQuantidade: {item[3]}')
    
def get_item_cart_by_id(id_product):
    product = filter(lambda item: item[1] == id_product, cart)
    print(list(product))
    #print_item(list(product))

def remove_item_id(id_product):
    for index, item in enumerate(cart):
        if item[1] == id_product:
            print("Removido: ")
            #print_item(list.pop(index))
            print(cart.pop(index))
            break

while exe:
    id_product = input('Insira o id do produto: ')
    #Verificar se item já existe antes de adicionar
    price_product = float(input ('Insira o preço do produto: '))
    quantity_product = int(input('Insira a quantidade de produto: '))
    item = [id_user, id_product, price_product, quantity_product]
    add_item_cart(item)
    exe = 'S' == input("Deseja adicionar mais algum item?\nDigite 'S' para continuar e qualquer outro caracter para sair: ")
    

get_all_items_cart()

search = input("Digite o id do produto que deseja encontrar:" )
get_item_cart_by_id(search)
remove = input("Digite o id do produto que deseja remover:")
remove_item_id(remove)