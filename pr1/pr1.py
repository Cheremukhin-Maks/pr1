import math




def main():
    while(True):
        try:
            a = float(input("Введіть a: "))
            b = float(input("Введіть b: "))
            c = float(input("Введіть c: "))
        except ValueError:
            print("Потрібно ввсети числа")
            continue


        sum_squares = a ** 2 + b ** 2 + c ** 2
        total_sum = a + b + c
        average = total_sum/3
        avg_int = total_sum // 3
        avg_rem = total_sum % 3
        discriminant = b**2 - 4 * a * c
        hypotenuse = math.sqrt(a**2 + b **2)
        is_triangle = (a + b > c) and (a + c > b) and (b + c > a)


        print(f"Сума квадратів: {sum_squares:.2f}")
        print(f"Середнє арифметичне: {average:.2f}")
        print(f"Середнє арифметичне: { avg_int:.2f}")
        print(f"Середнє арифметичне: {avg_rem:.2f}")
        print(f"Дискримінант: {discriminant:.2f}")
        print(f"Гіпотенуза: {hypotenuse:.2f}")
        print(f"Утворюють трикутник: {is_triangle}")

        break
if __name__ == "__main__":
    main()