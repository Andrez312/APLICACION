import streamlit as st

st.set_page_config(page_title="Beam", page_icon="👾", layout="wide")

st.title("Beam")
st.write("""
Este módulo se puede utilizar para resolver problemas de flexión de vigas 2D con Funciones de singularidad en mecánica.
         """)

codigo = '''
Clase sympy.physics.continuum_mechanics.beam.Viga (longitud, elastic_modulus,
    second_moment, área = A, variable = x, base_char = 'C') [fuente]
'''
st.code(codigo, language='phyton')


# CSS para estilizar la barra de contenidos
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
    text-align: center;
    background-color: #212F3C;
    width: 300px;
    }
    [data-testid="stSidebar"] a:hover {
        color: #007BFF; /* Color al pasar el mouse */
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("TABLA DE CONTENIDOS")