from calculator import *


def main():
    distancia_km = 100
    valor_diesel = 5.9
    km_por_litro_diesel = 9.2
    quant_pedagio = 1
    valor_pedagio = 6.3
    mao_de_obra = 15 #salario / dias trabalhados = mao de obra por dia / quantidade de entregas dia
    manutencao_km = 0.40
    deprecriacao_km = 0.50 #valor compra - valor de venda / kilometragem
    frequencia_semana = 3

    cost = delivery_cost(distancia_km, valor_diesel, km_por_litro_diesel, quant_pedagio, valor_pedagio, mao_de_obra, manutencao_km, deprecriacao_km)
    cost_week = delivery_cost_weekly(frequencia_semana, cost)





if __name__ == "__main__":
    main()