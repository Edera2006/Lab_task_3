import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x1, x2):
    """
    Функция f(x1, x2) = 0.5 + (cos^2(sin(|x1^2 - x2^2|)) - 0.5) / [1 + 0.001(x1^2 + x2^2)]^2
    """
    # Вычисляем |x1^2 - x2^2|
    arg = np.abs(x1 ** 2 - x2 ** 2)

    # Вычисляем функцию
    numerator = np.cos(np.sin(arg)) ** 2 - 0.5
    denominator = (1 + 0.001 * (x1 ** 2 + x2 ** 2)) ** 2

    return 0.5 + numerator / denominator


def create_data():
    """Создание сетки данных для построения графиков"""
    # Увеличиваем количество точек для более гладкого графика
    x1 = np.linspace(-2.0, 2.0, 150)
    x2 = np.linspace(-2.0, 2.0, 150)

    # Создаем двумерную сетку
    X1, X2 = np.meshgrid(x1, x2)

    # Вычисляем значения функции
    Z = f(X1, X2)

    return x1, x2, X1, X2, Z


def main():
    # Создаем данные
    x1, x2, X1, X2, Z = create_data()

    # Тестовая точка (x10, x20) = (0.0, 0.0)
    x10, x20 = 0.0, 0.0
    z_test = f(x10, x20)

    # Создаем фигуру с подграфиками
    fig = plt.figure(figsize=(18, 14))
    fig.suptitle('Визуализация функции f(x₁, x₂)', fontsize=18, fontweight='bold', y=0.95)

    # 1. 3D поверхность - изометрический вид с градиентной заливкой
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    surf1 = ax1.plot_surface(X1, X2, Z, cmap='viridis', alpha=0.9,
                             rcount=80, ccount=80, linewidth=0,
                             antialiased=True, edgecolors='none')
    ax1.set_xlabel('x₁', fontsize=12, fontweight='bold')
    ax1.set_ylabel('x₂', fontsize=12, fontweight='bold')
    ax1.set_zlabel('y = f(x₁, x₂)', fontsize=12, fontweight='bold')
    ax1.set_title('3D поверхность (изометрический вид)', fontsize=12)
    ax1.view_init(elev=30, azim=45)

    # Добавляем тестовую точку
    ax1.scatter([x10], [x20], [z_test], color='red', s=150,
                label=f'Тестовая точка ({x10}, {x20})\nf({x10}, {x20}) = {z_test:.4f}',
                edgecolors='black', linewidth=2)
    ax1.legend(fontsize=10)

    # Добавляем колорбар
    cbar1 = fig.colorbar(surf1, ax=ax1, shrink=0.6, aspect=15, pad=0.1)
    cbar1.set_label('Значение функции', rotation=270, labelpad=20, fontsize=10)

    # 2. 3D поверхность - вид сверху
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    surf2 = ax2.plot_surface(X1, X2, Z, cmap='plasma', alpha=0.9,
                             rcount=80, ccount=80, linewidth=0,
                             antialiased=True, edgecolors='none')
    ax2.set_xlabel('x₁', fontsize=12, fontweight='bold')
    ax2.set_ylabel('x₂', fontsize=12, fontweight='bold')
    ax2.set_zlabel('y = f(x₁, x₂)', fontsize=12, fontweight='bold')
    ax2.set_title('3D поверхность (вид сверху)', fontsize=12)
    ax2.view_init(elev=90, azim=0)

    # Добавляем тестовую точку
    ax2.scatter([x10], [x20], [z_test], color='red', s=150,
                label=f'Тестовая точка ({x10}, {x20})\nf({x10}, {x20}) = {z_test:.4f}',
                edgecolors='black', linewidth=2)
    ax2.legend(fontsize=10)

    # Добавляем колорбар
    cbar2 = fig.colorbar(surf2, ax=ax2, shrink=0.6, aspect=15, pad=0.1)
    cbar2.set_label('Значение функции', rotation=270, labelpad=20, fontsize=10)

    # 3. Контурный график
    ax3 = fig.add_subplot(2, 3, 3)
    contour = ax3.contourf(X1, X2, Z, levels=50, cmap='coolwarm', alpha=0.8)
    contour_lines = ax3.contour(X1, X2, Z, levels=20, colors='black', alpha=0.4, linewidths=0.5)
    ax3.clabel(contour_lines, inline=True, fontsize=8, fmt='%.3f')
    ax3.set_xlabel('x₁', fontsize=12, fontweight='bold')
    ax3.set_ylabel('x₂', fontsize=12, fontweight='bold')
    ax3.set_title('Контурный график', fontsize=12)
    ax3.grid(True, alpha=0.3)

    # Добавляем тестовую точку на контурный график
    ax3.plot(x10, x20, 'ro', markersize=12, markeredgecolor='black',
             markeredgewidth=2, label=f'({x10}, {x20})')
    ax3.annotate(f'Тестовая точка\n({x10}, {x20})\ny = {z_test:.4f}',
                 xy=(x10, x20), xytext=(0.5, 1.0),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2),
                 fontsize=10, ha='center',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

    # Добавляем колорбар для контурного графика
    cbar3 = fig.colorbar(contour, ax=ax3)
    cbar3.set_label('y = f(x₁, x₂)', rotation=270, labelpad=20, fontsize=10)

    # 4. График y = f(x1) при x2 = x20
    ax4 = fig.add_subplot(2, 3, 4)
    y_x1 = f(x1, x20)
    ax4.plot(x1, y_x1, 'b-', linewidth=3, label=f'y = f(x₁, {x20})', alpha=0.8)
    ax4.axvline(x=x10, color='red', linestyle='--', alpha=0.7, linewidth=2,
                label=f'x₁ = {x10}')
    ax4.plot(x10, z_test, 'ro', markersize=12, markeredgecolor='black',
             markeredgewidth=2, label=f'f({x10}, {x20}) = {z_test:.4f}')
    ax4.set_xlabel('x₁', fontsize=12, fontweight='bold')
    ax4.set_ylabel('y = f(x₁, x₂)', fontsize=12, fontweight='bold')
    ax4.set_title(f'Сечение при x₂ = {x20}', fontsize=12)
    ax4.grid(True, alpha=0.3)
    ax4.legend(fontsize=10)

    # 5. График y = f(x2) при x1 = x10
    ax5 = fig.add_subplot(2, 3, 5)
    y_x2 = f(x10, x2)
    ax5.plot(x2, y_x2, 'g-', linewidth=3, label=f'y = f({x10}, x₂)', alpha=0.8)
    ax5.axvline(x=x20, color='red', linestyle='--', alpha=0.7, linewidth=2,
                label=f'x₂ = {x20}')
    ax5.plot(x20, z_test, 'ro', markersize=12, markeredgecolor='black',
             markeredgewidth=2, label=f'f({x10}, {x20}) = {z_test:.4f}')
    ax5.set_xlabel('x₂', fontsize=12, fontweight='bold')
    ax5.set_ylabel('y = f(x₁, x₂)', fontsize=12, fontweight='bold')
    ax5.set_title(f'Сечение при x₁ = {x10}', fontsize=12)
    ax5.grid(True, alpha=0.3)
    ax5.legend(fontsize=10)

    # 6. Информационная панель
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.axis('off')

    # Создаем текстовую информацию
    info_text = f"""
    ИНФОРМАЦИЯ О ФУНКЦИИ И ТЕСТОВОЙ ТОЧКЕ

    Функция:
    f(x₁, x₂) = 0.5 + [cos²(sin(|x₁² - x₂²|)) - 0.5] / [1 + 0.001(x₁² + x₂²)]²

    Параметры построения:
    • Интервал: x₁, x₂ ∈ [-2.0, 2.0]
    • Шаг дискретизации: 150 точек по каждой оси
    • Цветовая схема: градиентная заливка

    Тестовая точка:
    • Координаты: (x₁₀, x₂₀) = ({x10}, {x20})
    • Значение функции: y = f({x10}, {x20}) = {z_test:.6f}

    Дополнительная информация:
    • Максимальное значение: {np.max(Z):.4f}
    • Минимальное значение: {np.min(Z):.4f}
    • Среднее значение: {np.mean(Z):.4f}
    """

    ax6.text(0.05, 0.95, info_text, transform=ax6.transAxes, fontsize=11,
             verticalalignment='top', horizontalalignment='left',
             bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.8))

    # Улучшаем компоновку
    plt.tight_layout(rect=[0, 0.03, 1, 0.93])

    # Выводим информацию в консоль
    print("=" * 60)
    print("АНАЛИЗ ФУНКЦИИ f(x₁, x₂)")
    print("=" * 60)
    print("Функция:")
    print("f(x₁, x₂) = 0.5 + [cos²(sin(|x₁² - x₂²|)) - 0.5] / [1 + 0.001(x₁² + x₂²)]²")
    print(f"Параметры построения:")
    print(f"• Интервал построения: x₁, x₂ ∈ [-2.0, 2.0]")
    print(f"• Количество точек по каждой оси: 150")
    print(f"• Общее количество точек: {150 * 150}")
    print(f"Тестовая точка:")
    print(f"• Координаты (x₁₀, x₂₀) = ({x10}, {x20})")
    print(f"• Значение функции: f({x10}, {x20}) = {z_test:.8f}")
    print(f"Статистика функции:")
    print(f"• Максимальное значение: {np.max(Z):.6f}")
    print(f"• Минимальное значение: {np.min(Z):.6f}")
    print(f"• Среднее значение: {np.mean(Z):.6f}")
    print(f"• Стандартное отклонение: {np.std(Z):.6f}")
    print("=" * 60)

    plt.show()


if __name__ == '__main__':
    main()