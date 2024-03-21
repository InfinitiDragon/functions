def is_triangle_possible(angle_a, angle_b):
    # Перевірка чи існує трикутник з вказаними кутами
    if angle_a + angle_b < 180:
        return True
    else:
        return False

def is_right_triangle(angle_a, angle_b):
    # Перевірка чи є трикутник прямокутним за вказаними кутами
    if 90 in (angle_a, angle_b):
        return True
    else:
        return False

def main():
    # Введення величин кутів трикутника з клавіатури
    angle_a = float(input("Введіть величину першого кута (в градусах): "))
    angle_b = float(input("Введіть величину другого кута (в градусах): "))

    # Перевірка існування трикутника з введеними кутами
    if is_triangle_possible(angle_a, angle_b):
        print("Трикутник з такими кутами існує.")
        # Перевірка чи є трикутник прямокутним
        if is_right_triangle(angle_a, angle_b):
            print("Трикутник є прямокутним.")
        else:
            print("Трикутник не є прямокутним.")
    else:
        print("Трикутник з такими кутами не існує.")

if __name__ == "__main__":
    main()
