def factorial(n: int) -> int:
    res = 1
    for i in range(1, n +1, 1):
        res *= i
    return res

def harmonic_sum(n: int) -> float:
    res = 0
    for i in range(1, n +1, 1):
        res += 1/i
    return res

def multiplication_table(n: int) -> None:
    for i in range(1, n+1, 1):
        for j in range(1 , n+1, 1):
            print(f"{i * j:4d}", end="")
        print()

def main():
    while(True):
        try:
            n = int(input("Введіть число n: "))
        except ValueError:
            print("Потрібно ввести ціле число")
            continue

        print(f"{n}! = {factorial(n)}")

        print(f"Гармонічна сума H({n}) = {harmonic_sum(n):.6f}")

        print(f"\nТаблиця множення {n}×{n}:")

        multiplication_table(n)

        break

if __name__ == "__main__":

    main()
