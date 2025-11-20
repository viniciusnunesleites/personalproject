from calculator import delivery_cost, delivery_cost_weekly
from greet import greet

def ask(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Erro! Digite um número válido.")

def main():
    greet()
    distance_km = ask("Distancia em km's -> ")
    diesel_price = ask("Valor do diesel -> ")
    diesel_per_liter = ask("Quantos km/l o veiculo faz? -> ")
    toll_count = ask("Quantos pedágios no trajeto? -> ")
    toll_price = ask("Qual o valor do pedágio? -> ")
    labor_cost = 15 #salario / dias trabalhados = mao de obra por dia / quantidade de entregas dia = labor cost
    maintenence_cost_km = 0.40
    depreciation_cost_km = 0.50 #valor compra - valor de venda / kilometragem na venda do veiculo
    
    cost = delivery_cost(distance_km, diesel_price, diesel_per_liter, toll_count, toll_price, labor_cost, maintenence_cost_km, depreciation_cost_km)
    answer = input("Gostaria de calcular o custo de entrega semanal? (s/n)? ").strip().lower()
    if answer == "s":
        frequency = ask("Quantas coletas/entregas por semana no cliente? -> ")
        time = ask("Quantos minutos o motorista aguarda/fica no cliente? -> ")
        cost_week = delivery_cost_weekly(frequency, cost, time)
    else:
        print("Ok, programa encerrado.")



if __name__ == "__main__":
    main()