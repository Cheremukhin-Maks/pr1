def main():
    raw_input = input("Введіть число: ")


    val_int = int(raw_input)
    val_float = float(raw_input)
    val_bool = bool(raw_input)

    print(f"Значення int: {val_int}, тип: {type(val_int)}, чи є int: {isinstance(val_int, int)}")
    print(f"Значення float: {val_float}, тип: {type(val_float)}, чи є float: {isinstance(val_float, float)}")
    print(f"Значення bool: {val_bool}, тип: {type(val_bool)}, чи є bool: {isinstance(val_bool, bool)}")


    age = int(input("Введіть вік: "))
    name = input("Введіть імя: ")
    
    print(f"Ваше ім'я: {name}, ваш вік: {age}")

    numbers = list(range(1 , 7))
    print(numbers)
    print(len(numbers))
    print(id(numbers))

if __name__ == "__main__":

    main()