import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, size):
    def koch_curve(order, size):
        if order == 0:
            return np.array([[0, 0], [size, 0]])
        points = koch_curve(order - 1, size / 3)
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            dx, dy = p2 - p1
            new_points.extend([
                p1,
                p1 + np.array([dx, dy]) / 3,
                p1 + np.array([dx, dy]) / 3 + np.array([dx - dy * np.sqrt(3), dy + dx * np.sqrt(3)]) / 6,
                p1 + np.array([dx, dy]) * 2 / 3,
            ])
        new_points.append(points[-1])
        return np.array(new_points)

    def rotate(points, angle):
        theta = np.radians(angle)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        return points.dot(rotation_matrix)

    def create_snowflake(order, size):
        triangle_points = koch_curve(order, size)
        snowflake_points = [triangle_points]
        for angle in [120, 240]:
            snowflake_points.append(rotate(triangle_points, angle) + snowflake_points[-1][-1])
        return np.vstack(snowflake_points)

    points = create_snowflake(order, size)
    return points

def plot_koch_snowflake(order, size):
    points = koch_snowflake(order, size)
    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], 'b-')
    plt.axis('equal')
    plt.title(f"Сніжинка Коха порядку {order}")
    plt.show()

# Введення рівня рекурсії
level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

# Вивід сніжинки Коха
plot_koch_snowflake(level, 300)
