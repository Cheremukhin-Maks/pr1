import math


def triangle_type(a: float, b: float, c: float) -> str:
    if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a):
   
        is_right = (
            abs(a**2 + b**2 - c**2) < 1e-9
            or abs(a**2 + c**2 - b**2) < 1e-9
            or abs(b**2 + c**2 - a**2) < 1e-9)

       
        if a == b == c:
            return "рівносторонній"
        elif a == b or a == c or b == c:
            if is_right:
                return "прямокутний рівнобедрений"
            return "рівнобедрений"
        elif is_right:
            return "прямокутний"
        else:
            return "різносторонній"
    else:
        return "не є трикутником"
    



def triangle_area(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

def main():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    t_type = triangle_type(a ,b , c)
    
    if t_type == "не є трикутником":
        print("Введені числа не утворюють трикутник!")
    else:
        t_area = triangle_area(a, b, c)
        print(f"Тип трикутника: {t_type}, площа трикутника: {t_area:.2f}")


if __name__ == "__main__":

    main()




