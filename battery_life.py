def battery_life_predictor(capacity_mAh, I_active, I_sleep, T_active, T_sleep):

    T_total = T_active + T_sleep
    
    D = T_active / T_total
    
    I_avg = D * I_active + (1 - D) * I_sleep
    
    battery_life_hours = capacity_mAh / I_avg
    
    return D, I_avg, battery_life_hours

capacity = 2000
I_active = 100
I_sleep = 5
T_active = 2
T_sleep = 8           

D, I_avg, life = battery_life_predictor(capacity, I_active, I_sleep, T_active, T_sleep)

print("Duty Cycle:", D)
print("Average Current (mA):", I_avg)
print("Battery Life (hours):", life)