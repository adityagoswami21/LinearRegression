import numpy as np


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.001
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        md = (1/n)*sum(x*(y_predicted - y))
        bd = (1/n)*sum(y_predicted - y)
        m_curr = m_curr - learning_rate*md
        b_curr = b_curr - learning_rate*bd
        print(f"m {m_curr}, b {b_curr}, iteration {i}")


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)