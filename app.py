import streamlit as st
from component.plotter import plot_functions
from core.sym_f import derivative, integral
from core.sym_f import derivative, integral, to_numpy_func

st.set_page_config(layout="wide")
st.title("Sketcher")

expr_input = st.text_area(
    "Enter functions (comma separated):",
    "sin(x), x**2"
)

expressions = [e.strip() for e in expr_input.split(",")]

x_min, x_max = st.slider("X Range", -50, 50, (-10, 10))
y_min, y_max = st.slider("Y Range", -50, 50, (-10, 10))

fig = plot_functions(expressions, (x_min, x_max),(y_min,y_max))
st.plotly_chart(fig, use_container_width=True)

st.subheader("Symbolic Analysis")

selected_expr = st.selectbox("Select function", expressions)


extra_funcs = []

if st.button("Derivative"):
    d = derivative(selected_expr)
    st.latex(str(d))

    d_func = to_numpy_func(d)
    extra_funcs.append((f"d/dx {selected_expr}", d_func))

if st.button("Integral"):
    i = integral(selected_expr)
    st.latex(str(i))

    i_func = to_numpy_func(i)
    extra_funcs.append((f"∫ {selected_expr}", i_func))

fig = plot_functions(
    expressions,
    (x_min, x_max),
    (y_min, y_max),
    extra_funcs
)

st.plotly_chart(fig, use_container_width=True)
