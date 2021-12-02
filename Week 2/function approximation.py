import math
import scipy.linalg
import matplotlib.pyplot as plt


def f(input_value):
    return float(math.sin(input_value / 5) * math.exp(input_value / 10) + 5 * math.exp(-input_value / 2))


if __name__ == '__main__':
    A = [[1, 1], [1, 15]]
    B = [f(1), f(15)]
    solution = scipy.linalg.solve(A, B)
    x = []
    y = []
    for i in range(1, 16):
        x.append(i)
        y.append(f(i))
    A_closer = [[1, 1.8], [1, 15 * 1.8]]
    B_closer = [f(1.8), f(15)]
    solution_closer = scipy.linalg.solve(A_closer, B_closer)

    A_final = [[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]]
    B_final = [f(1), f(4), f(10), f(15)]
    omega_coefficient = scipy.linalg.solve(A_final, B_final)

    plt.plot(x, y, 'r-', [1, 15], solution, 'g-', [1.8, 15], solution_closer, 'b-', [1, 4, 10, 15],
             omega_coefficient, 'r-')
    print(omega_coefficient)
