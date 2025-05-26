import temperature as temp

def main():
    temperatures = [20, 30, 40, 50, 60]
    for t in temperatures:
        print("Temperature at ", t, "is", temp.process_temperature(t))

if __name__ == "__main__":
    main()