def main():
    # Введення трьох дійсних чисел з клавіатури
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))

    # Піднесення до квадрата та четвертої ступені відповідно до умови
    a = a ** 2 if a >= 0 else a ** 4
    b = b ** 2 if b >= 0 else b ** 4
    c = c ** 2 if c >= 0 else c ** 4

    # Виведення результату
    print("Результат:")
    print("Перше число:", a)
    print("Друге число:", b)
    print("Третє число:", c)

if __name__ == "__main__":
    main()