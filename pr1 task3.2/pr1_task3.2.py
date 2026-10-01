def calculator():

    """Інтерактивний калькулятор з підтримкою +, -, *, /, //, %, **."""

    print("=== Калькулятор ===")

    print("Введіть вираз у форматі: число оператор число")

    print("Введіть 'quit' для виходу, 'history' для історії")


    history = []

    while True:
        user_input = input("\n> ").strip()

        if user_input.lower() == "quit":
            break

        if user_input.lower() == "history":
                if not history:
                    print("Історія обчислень порожня.")
                else:
                    print("\n--- Історія обчислень ---")
                    for item in history:
                        print(item)
                continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Помилка: Некоректний формат! Введіть: число оператор число")
            continue

        str_num1, operator, str_num2 = parts
        num1 = float(str_num1)
        num2 = float(str_num2)

        result = None

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Помилка: Ділення на нуль неможливе!")
                continue
            result = num1 / num2
        elif operator == "//":
            if num2 == 0:
                print("Помилка: Цілочисельне ділення на нуль неможливе!")
                continue
            result = num1 // num2
        elif operator == "%":
            if num2 == 0:
                print("Помилка: Ділення на нуль (остача) неможливе!")
                continue
            result = num1 % num2
        elif operator == "**":
            result = num1**num2
        else:
            print(f"Помилка: Непідтримуваний оператор '{operator}'!")
            print("Допустимі оператори: +, -, *, /, //, %, **")
            continue

        

        entry = f"{num1} {operator} {num2} = {result}"
        print(f"Результат: {result}")

        history.append(entry)



    
if __name__ == "__main__":

    calculator()