def main():
    # Введення трьох чисел a, b, c з клавіатури
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    # Ініціалізація лічильника негативних чисел
    negative_count = 0

    # Перевірка кожного числа на негативність
    if a < 0:
        negative_count += 1
    if b < 0:
        negative_count += 1
    if c < 0:
        negative_count += 1

    # Виведення результату
    print("Кількість негативних чисел серед a, b, c:", negative_count)

if __name__ == "__main__":
    main()
