def main():
    while(True):
        try:
            raw_input = input("Введіть число: ")
        
            val_int = int(raw_input)
            val_float = float(raw_input)
            val_bool = bool(raw_input)
        except ValueError:
            print("Потрібно ввести число")
            continue
            

        print(f"Значення int: {val_int}, тип: {type(val_int)}, чи є int: {isinstance(val_int, int)}")
        print(f"Значення float: {val_float:.5f}, тип: {type(val_float)}, чи є float: {isinstance(val_float, float)}")
        print(f"Значення bool: {val_bool}, тип: {type(val_bool)}, чи є bool: {isinstance(val_bool, bool)}")

        try:
            age = int(input("Введіть вік: "))
        except ValueError:
            print("Вік повинен бути цілим числом")
            continue
        name = input("Введіть імя: ")
        
    
        print(f"Ваше ім'я: {name}, ваш вік: {age}")

        numbers = list(range(1 , 7))
        print(numbers)
        print(len(numbers))
        print(id(numbers))

        break

if __name__ == "__main__":

    main()