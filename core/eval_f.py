import numpy as np

SAFE_FUNCTIONS = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "log": np.log,
    "exp": np.exp,
    "sqrt": np.sqrt,
    "abs": np.abs,
    "pi": np.pi,
    "e": np.e
}

def evaluate(expr, x):
    local_dict = SAFE_FUNCTIONS.copy()
    local_dict["x"] = x

    return eval(expr, {"__builtins__": {}}, local_dict)