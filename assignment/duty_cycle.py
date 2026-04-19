def battery_life_predictor():
    print("=== Battery Life Predictor (Duty Cycle Model) ===")

    capacity = float(input("Enter Battery Capacity (mAh): "))
    I_active = float(input("Enter Active Current (mA): "))
    I_sleep = float(input("Enter Sleep Current (mA): "))
    T_active = float(input("Enter Active Time (seconds): "))
    T_sleep = float(input("Enter Sleep Time (seconds): "))

    T_total = T_active + T_sleep
    duty_cycle = T_active / T_total

    I_avg = duty_cycle * I_active + (1 - duty_cycle) * I_sleep
    battery_life = capacity / I_avg

    print("\n--- Results ---")
    print(f"Duty Cycle: {duty_cycle:.3f} ({duty_cycle*100:.2f}%)")
    print(f"Average Current: {I_avg:.2f} mA")
    print(f"Estimated Battery Life: {battery_life:.2f} hours")


battery_life_predictor()