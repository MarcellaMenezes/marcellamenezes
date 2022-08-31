# import datetime

# date = datetime.date.today()
# year = date.strftime("%Y")

name        = input("Informe seu nome: ")
city        = input("Informe sua cidade: ")
birth_year  = int(input("Informe o ano que você nasceu: "))

print(f'Nome: {name}\nCidade: {city}\nAno: {birth_year}')
print(f'{name}, em 2030 você terá {2030 - birth_year}')