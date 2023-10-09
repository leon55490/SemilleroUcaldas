# `import matplotlib.pyplot as plt` is importing the `pyplot` module from the `matplotlib`
# library and assigning it the alias `plt`. This allows us to use the functions and classes
# from the `pyplot` module by prefixing them with `plt`.
import matplotlib.pyplot as plt


def x_prime(x, a):
    """
    The function `x_prime` takes two parameters `x` and `a` and returns the product of `x` and
    `a`.
    
    :param x: The parameter x is a number that will be multiplied by the value of a
    :param a: The parameter "a" is a constant value that will be multiplied by the input value
    "x"
    :return: the product of `a` and `x`.
    """
    return a * x


def euler(x0, a, Tf, N):
    """
    The function `euler` implements the Euler method to approximate the solution of a
    first-order ordinary differential equation.
    
    :param x0: The initial value of x at t=0
    :param a: The parameter "a" is not defined in the given code. It seems to be a missing
    piece of information. Could you please provide more details about what "a" represents in
    this context?
    :param Tf: Tf is the final time at which we want to evaluate the solution
    :param N: N is the number of steps in the Euler method. It determines the granularity of
    the approximation
    :return: two lists: t and x. The list t contains the time values at each step, and the
    list x contains the corresponding values of x.
    """
    h = (Tf - 0) / N
    t = [0]
    x = [x0]
    for i in range(N):
        x.append(x[-1] + h * x_prime(x[-1], a))
        t.append(t[-1] + h)
    return t, x


a = float(input("Ingrese el valor de a: ")) #Tasa Crecimiento
x0 = float(input("Ingrese el valor de x0: ")) # Valor inicial
Tf = float(input("Ingrese el valor de Tf: ")) #Tiempo Final
N = int(input("Ingrese el valor de N: ")) # Numero de intervalos de tiempo

# `t, x = euler(x0, a, Tf, N)` is calling the `euler` function with the given parameters
# `x0, a, Tf, N` and assigning the returned values to the variables `t` and `x`. The `euler`
# function returns two lists: `t` which contains the time values at each step, and `x` which
# contains the corresponding values of `x`. By assigning the returned values to `t` and `x`,
# we can access and use these lists later in the code.
t, x = euler(x0, a, Tf, N)

# The code `plt.plot(t, x)` is creating a line plot using the values from the lists `t` and
# `x`. The `t` list represents the time values at each step, and the `x` list represents the
# corresponding values of `x`.
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Crecimiento exponencial")
plt.show()
