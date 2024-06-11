def move_disk(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск з {source} на {target}")
        towers[target].append(towers[source].pop())
        print_state()
    else:
        move_disk(n-1, source, auxiliary, target)
        move_disk(1, source, target, auxiliary)
        move_disk(n-1, auxiliary, target, source)

def print_state():
    print(f"Проміжний стан: {{'A': {towers['A']}, 'B': {towers['B']}, 'C': {towers['C']}}}")

def print_final_state():
    print(f"Кінцевий стан: {{'A': {towers['A']}, 'B': {towers['B']}, 'C': {towers['C']}}}")

# Вхідні дані
n = int(input("Введіть кількість дисків: "))

# Початковий стан стрижнів
towers = {'A': list(reversed(range(1, n+1))), 'B': [], 'C': []}
print("Початковий стан:")
print_state()

# Запуск алгоритму
move_disk(n, 'A', 'C', 'B')

# Виведення кінцевого стану
print_final_state()
