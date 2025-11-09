def get_sensor_data():
    gas = float(input("Gas Sensor (ppm): "))
    temp = float(input("Temperature (°C): "))
    air = float(input("Air Flow Rate (m³/h): "))
    fuel = float(input("Fuel Rate (kg/h): "))
    particle_size = float(input("Particle Size (mm): "))
    moisture = float(input("Moisture Content (%): "))
    
    ER = fuel / air if air != 0 else 0
    return [[gas, temp, air, fuel, ER, particle_size, moisture]]
