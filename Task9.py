def main():
    # Введення трьох чисел a, b, c з клавіатури
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    # Ініціалізація лічильника цілих чисел
    integer_count = 0

    # Перевірка кожного числа на ціле значення
    if a.is_integer():
        integer_count += 1
    if b.is_integer():
        integer_count += 1
    if c.is_integer():
        integer_count += 1

    # Виведення результату
    print("Кількість цілих чисел серед a, b, c:", integer_count)

if __name__ == "__main__":
    main()
