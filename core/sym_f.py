import sympy as sp

x = sp.symbols('x')

def derivative(expr):
    f = sp.sympify(expr)
    return sp.diff(f, x)

def integral(expr):
    f = sp.sympify(expr)
    return sp.integrate(f, x)


def to_numpy_func(sym_expr):
    return sp.lambdify(x, sym_expr, "numpy")