def hanoi(n, source, target, auxiliary, rods):
    if n == 1:
        disk = rods[source].pop()
        rods[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {rods}")
        return

    hanoi(n - 1, source, auxiliary, target, rods)

    disk = rods[source].pop()
    rods[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {rods}")

    hanoi(n - 1, auxiliary, target, source, rods)


def main():
    n = int(input("Введіть кількість дисків: "))

    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {rods}")
    hanoi(n, 'A', 'C', 'B', rods)
    print(f"Кінцевий стан: {rods}")


if __name__ == "__main__":
    main()
