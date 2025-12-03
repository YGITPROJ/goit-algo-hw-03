import argparse
from pathlib import Path
import shutil


def parse_args():
    """
    Робота з аргументами командного рядка
    """
    parser = argparse.ArgumentParser(description="Сортування за розширенням")
    parser.add_argument("source", type=Path, help="Віхідна директорія")
    parser.add_argument(
        "--output", "-o", type=Path, default=Path("dist"), help="Вихідна директорія"
    )
    return parser.parse_args()


def copy_file(file_path: Path, output_root: Path):
    """
    Копіювання файлу

    :param file_path: Description
    :type file_path: Path
    :param output_root: Description
    :type output_root: Path
    """
    try:
        extension = file_path.suffix[1:] if file_path.suffix else "others"
        target_dir = output_root / extension
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / file_path.name
        shutil.copy2(file_path, target_file)
        print(f"Скопіювано: {file_path.name} -> {target_dir}")
    except PermissionError:
        print(f"Немає доступу до файлу {file_path}")
    except Exception as err:
        print(f"Не вдалося скопіювати {file_path}: {err}")


def recursive_copy(source: Path, output: Path):
    """
    Рекурсивний обхід вхідної директорії
    з побальшим копіюванням та сортуванням файлів

    :param source: Description
    :type source: Path
    :param output: Description
    :type output: Path
    """
    try:
        for item in source.iterdir():
            if item.is_dir():
                recursive_copy(item, output)
            elif item.is_file():
                copy_file(item, output)
    except PermissionError:
        print(f"Немає доступу до директорії {source}")
    except Exception as err:
        print(f"Error: Помилка при обробці {source}: {err}")


def main():

    # шлях необхідно передавати в лапках
    args = parse_args()
    if not args.source.exists():
        print(f"Вихідна директорія '{args.source}' не існує.")
        return
    print(f"Сортування з '{args.source}' в '{args.output}'")

    recursive_copy(args.source, args.output)

    print("Завершено")


if __name__ == "__main__":
    main()
