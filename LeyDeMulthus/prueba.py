import matplotlib.pyplot as plt


def x_prime(x, a):
    return a * x


def euler(x0, a, Tf, N):
    h = (Tf - 0) / N
    t = [0]
    x = [x0]
    for i in range(N):
        x.append(x[-1] + h * x_prime(x[-1], a))
        t.append(t[-1] + h)
    return t, x


a = float(input("Ingrese el valor de a: "))
x0 = float(input("Ingrese el valor de x0: "))
Tf = float(input("Ingrese el valor de Tf: "))
N = int(input("Ingrese el valor de N: "))

t, x = euler(x0, a, Tf, N)

plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Crecimiento exponencial")
plt.show()
