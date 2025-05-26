def process_temperature(temp):
    if temp > 50:
        return "hot"
    elif temp > 30:
        return "warm"
    else:
        return "cold"