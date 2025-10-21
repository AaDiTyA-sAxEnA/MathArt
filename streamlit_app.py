import streamlit as st
st.set_page_config(layout="wide")
st.title("MATH-ART")
st.header('A website which shows mathematics as an *art form*')
st.subheader('It uses 9 basic mathematical functions and display the graph of the'
             ' original function along with its derivative and integral showcasing '
             'that art is present even in the subject which appears very daunting at first.')
st.divider()
st.subheader('''Geometrical significance: ''')
st.write('''The DERIVATIVE of a function is its slope''')
st.write('''The INTEGRAL of a function is the area under its functional curve''')
st.divider()

st.markdown("You can press any one of the 9 buttons given below and the app will display the graph "
            "that function along with its corresponding derivative and integral")




button_labels = [r"$x^2$",r"$x^3$", r"$\sin x$", r"$\tan x$", r"$e^x$", r"$\ln(x)$", r"$\frac{1}{x}$",r"$\sin^{-1}x$",r"$\tan^{-1}x$"]
cols = st.columns(9)

col1, col2, col3 = st.columns(3)
for label, col in zip(button_labels, cols):
    with col:

        if st.button(label):
            if label == r"$x^2$":

                with col1:
                    st.header("FUNCTION")
                    st.image('square.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('square_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('square_integral.jpg')
            if label == r"$x^3$":

                with col1:
                    st.header("FUNCTION")
                    st.image('cube.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('cube_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('cube_integral.jpg')
            if label == r"$\tan x$":
                with col1:
                    st.header("FUNCTION")
                    st.image('tan x.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('tan x_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('tan x_integral.jpg')
            if label == r"$\sin x$":
                with col1:
                    st.header("FUNCTION")
                    st.image('sin x.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('sin x_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('sin x_integral.jpg')
            if label == r"$e^x$":

                with col1:
                    st.header("FUNCTION")
                    st.image('exp.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('exp_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('exp_integral.jpg')
            if label == r"$\ln(x)$":
                with col1:
                    st.header("FUNCTION")
                    st.image('ln.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('ln_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('ln_integral.jpg')
            if label == r"$\frac{1}{x}$":
                with col1:
                    st.header("FUNCTION")
                    st.image('reciprocal.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('reciprocal_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('reciprocal_integral.jpg')
            if label == r"$\sin^{-1}x$":
                with col1:
                    st.header("FUNCTION")
                    st.image('sin-1.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('sin-1_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('sin-1_integral.jpg')
            if label == r"$\tan^{-1}x$":
                with col1:
                    st.header("FUNCTION")
                    st.image('tan-1.jpg')

                with col2:
                    st.header("DERIVATIVE")
                    st.image('tan-1_deriv.jpg')

                with col3:
                    st.header("INTEGRAL")
                    st.image('tan-1_integral.jpg')
