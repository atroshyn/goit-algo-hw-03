import os
import shutil
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Копіює файли у вихідній директорії та сортує їх в піддиректоріях за розширенням.")
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dst_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням: dist)')
    return parser.parse_args()

def copy_files(src_dir, dst_dir):
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                if os.path.abspath(src_path) != os.path.abspath(dst_dir):  # Запобігає рекурсивному копіюванню
                    copy_files(src_path, dst_dir)
            elif os.path.isfile(src_path):
                extension = os.path.splitext(item)[1][1:]  # Отримуємо розширення файлу без крапки
                if extension:  # Перевіряємо, що у файлу є розширення
                    dst_path = os.path.join(dst_dir, extension)
                    os.makedirs(dst_path, exist_ok=True)  # Створюємо директорію, якщо вона не існує
                    shutil.copy2(src_path, os.path.join(dst_path, item))
    except Exception as e:
        print(f"Помилка обробки {src_dir}: {e}")

def main():
    args = parse_args()
    src_dir = args.src_dir
    dst_dir = args.dst_dir

    if not os.path.exists(src_dir):
        print(f"Вихідна директорія '{src_dir}' не існує.")
        return

    if not os.path.exists(dst_dir):
        try:
            os.makedirs(dst_dir)
        except Exception as e:
            print(f"Не вдалося створити директорію '{dst_dir}': {e}")
            return

    if os.path.abspath(src_dir).startswith(os.path.abspath(dst_dir)):
        print(f"Директорія призначення '{dst_dir}' не може бути піддиректорією вихідної директорії '{src_dir}'.")
        return

    copy_files(src_dir, dst_dir)
    print(f"Файли скопійовано та відсортовано у {dst_dir}")

if __name__ == "__main__":
    main()
