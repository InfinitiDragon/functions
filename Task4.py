def main():
    # Введення двох дійсних чисел з клавіатури
    x = float(input("Введіть число x: "))
    y = float(input("Введіть число y: "))

    # Перевірка, що числа не рівні одне одному
    if x != y:
        # Знаходження меншого і більшого чисел
        smaller = min(x, y)
        larger = max(x, y)

        # Заміна значень згідно умови
        smaller = (smaller + larger) / 2
        larger = 2 * x * y if x > y else 2 * y * x

        # Виведення результатів
        print("Менше число після заміни: ", smaller)
        print("Більше число після заміни: ", larger)
    else:
        print("Числа повинні бути різними.")

if __name__ == "__main__":
    main()
