
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
        print(f"O custo de entrega é: R${total_cost} considerando a distância de: {distance_km} km.")
        return total_cost
    #tool cost
    toll_cost = toll_count * toll_price
    #total cost
    print(f"O custo de entrega é: R${total_cost + toll_cost} considerando a distância de: {distance_km} km.")
    return total_cost + toll_cost
    

def delivery_cost_weekly(frequency, time, delivery_cost):
    time_cost = time / 60 * 18
    cost_delivery = delivery_cost + time_cost
    weekly_cost = cost_delivery * frequency
    print(f"Custo semanal: R${weekly_cost}")
    return weekly_cost
