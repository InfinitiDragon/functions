def main():
    # Введення чисел a, b, c та числа k з клавіатури
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    k = float(input("Введіть число k: "))

    # Створення списку для зберігання чисел, які діляться на k
    divisors = []

    # Перевірка кожного числа на ділення на k
    if a % k == 0:
        divisors.append(a)
    if b % k == 0:
        divisors.append(b)
    if c % k == 0:
        divisors.append(c)

    # Виведення результату
    if divisors:
        print("Числа, які діляться на", k, ":", divisors)
    else:
        print("Немає чисел, які діляться на", k)

if __name__ == "__main__":
    main()
