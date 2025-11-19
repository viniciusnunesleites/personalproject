
def delivery_cost(distance_km, 
                  diesel_price, 
                  diesel_per_liter, 
                  toll_count, 
                  toll_price,
                  labor_cost,
                  maintenence_cost_km,
                  depreciation_cost_km):
    #fuel needed
    fuel_needed = distance_km / diesel_per_liter
    fuel_cost = fuel_needed * diesel_price
    #operational cost
    maintenence_cost = maintenence_cost_km * distance_km
    depreciation_cost = depreciation_cost_km * distance_km

    total_cost = fuel_cost + labor_cost + maintenence_cost + depreciation_cost

    if not toll_count:
        print(f"The delivery cost is: R${total_cost} considering a distance of: {distance_km} km.\nO custo do frete é: R${total_cost} considerando a distancia de: {distance_km} km")
        return total_cost
    #tool cost
    toll_cost = toll_count * toll_price
    #total cost
    print(f"The delivery cost is: R${total_cost + toll_cost} considering a distance of: {distance_km} km.\nO custo do frete é: R${total_cost + toll_cost} considerando a distancia de: {distance_km} km")
    return total_cost + toll_cost
    
def delivery_cost_weekly(frequency, delivery_cost):
    weekly_cost = delivery_cost * frequency
    print(f"weekly cost is: R${weekly_cost}\ncusto mensal é: R${weekly_cost}")
    return weekly_cost
