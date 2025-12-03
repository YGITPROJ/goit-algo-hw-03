import turtle


def koch_curve(t, order, size):
    """
    Обна сторона сніжинки

    :param t: Description
    :param order: Description
    :param size: Description
    """
    if order == 0:
        t.forward(size)
    else:
        new_size = size/3
        koch_curve(t, order - 1, new_size)
        t.left(60)
        koch_curve(t, order - 1, new_size)
        t.right(120)
        koch_curve(t, order - 1, new_size)
        t.left(60)
        koch_curve(t, order - 1, new_size)

def draw_snowflake(order, size=600):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    
    t.goto(-size / 2, size / 3) 
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    try:
        level = int(input("Введіть рівень рекурсії (рекомендовано 0-5): "))
        if level < 0:
            print("Рівень має бути невід'ємним числом.")
        else:
            print("Малюємо... Дивіться у вікно Turtle.")
            draw_snowflake(level)
    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
