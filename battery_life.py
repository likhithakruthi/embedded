def battery_life_predictor(capacity_mAh, I_active, I_sleep, T_active, T_sleep):
    # Total time
    T_total = T_active + T_sleep
    
    # Duty cycle
    D = T_active / T_total
    
    # Average current
    I_avg = D * I_active + (1 - D) * I_sleep
    
    # Battery life in hours
    battery_life_hours = capacity_mAh / I_avg
    
    return D, I_avg, battery_life_hours


# Example values
capacity = 2000       # mAh
I_active = 100        # mA
I_sleep = 5           # mA
T_active = 2          # seconds
T_sleep = 8           # seconds

D, I_avg, life = battery_life_predictor(capacity, I_active, I_sleep, T_active, T_sleep)

print("Duty Cycle:", D)
print("Average Current (mA):", I_avg)
print("Battery Life (hours):", life)