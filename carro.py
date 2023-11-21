# Exercício Python 01: Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km
# rodado

def aluguel(km, dias):
    preco_d = dias * 60
    preco_km = km * 0.15 
    preco_final = preco_d + preco_km
    print(preco_final)

print("saiba quanto você devera pagar no aluguel de um carro")
km = float(input("digite quantos km você rodou:"))
dias = int(input("digite por quantos dias você alugou o carro:"))
aluguel(km, dias)