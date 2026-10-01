def classify_grade(score: int) -> str:
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 82 and score <= 89:
        return "B"
    elif score >= 74 and score <= 81:
        return "C"
    elif score >= 64 and score <= 73:
        return "D"
    elif score >=60 and score <= 63:
        return "E"
    elif score >= 35 and score <= 59:
        return "FX"
    elif score >= 0 and score <= 34:
        return "F"
    

def main():
    raw = input("Введіть оцінку (0-100): ")
    score = int(raw)
    if score < 0 or score > 100:
        print("Помилка: оцінка має бути від 0 до 100")
    else:
        grade = classify_grade(score)
        print(f"Оцінка {score} → ЄКТС: {grade}")
        passed = grade not in ("FX", "F")
        print(f"Результат: {'Зараховано' if passed else 'Не зараховано'}")

if __name__ == "__main__":

    main()





