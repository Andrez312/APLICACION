import streamlit as st
from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols

st.set_page_config(page_title="Truss", page_icon="👾", layout="wide")

st.sidebar.header("TABLA DE CONTENIDOS")

st.title("Resolviendo Problemas de Flexión de Vigas Usando Funciones de Singularidad")

st.write("""
Una viga plana es un elemento estructural que es capaz de soportar cargas a través de la resistencia al cizallamiento interno y a la flexión. Las vigas se caracterizan por: su longitud, restricciones, segundo momento de área de la sección transversal y elástico Módulo. En SymPy, los objetos de viga 2D se construyen especificando lo siguiente Propiedades:

-Largura

-Módulo elástico

-Segundo Momento de Área

Variable : Símbolo que representa la ubicación a lo largo de la longitud de la viga. Por De forma predeterminada, se establece en .Symbol(x)

-Condiciones de contorno
--bc_slope : Condiciones de contorno para la pendiente.

--bc_deflection : Condiciones de contorno para la deflexión.

Distribución de la carga

Una vez especificado lo anterior, se utilizan los siguientes métodos para calcular Información sobre la viga cargada:

-solve_for_reaction_loads()

-shear_force()

-bending_moment()

-slope()
""")



st.markdown("### ejemplo")
st.text("Hay una manga de 30 metros de longitud. Un momento de magnitud 120 Nm es Se aplica en el sentido contrario a las agujas del reloj en el extremo del haz. Una carga puntual de magnitud 8 N se aplica desde la parte superior del haz en el punto. Hay dos soportes simples debajo de la viga. Uno al final y otro a una distancia de 10 metros de la salida. El La deflexión está restringida en ambos soportes")

st.code('''
 || 8 N                                       ⭯ 120 Nm
 \/______________________________________________|
 |_______________________________________________|
             /\                                 /\
 |------------|---------------------------------|
    10 m                  20 m
''')

st.info("Usando la convención de signos de fuerzas descendentes y momento en sentido contrario a las agujas del reloj Ser positivo")

st.code('''
from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
E, I = symbols('E, I')
R1, R2 = symbols('R1, R2')
b = Beam(30, E, I)
b.apply_load(8, 0, -1)
b.apply_load(R1, 10, -1)
b.apply_load(R2, 30, -1)
b.apply_load(120, 30, -2)
b.bc_deflection.append((10, 0))
b.bc_deflection.append((30, 0))
b.solve_for_reaction_loads(R1, R2)
b.reaction_loads
b.load
b.shear_force()
b.bending_moment()
b.slope()
b.deflection()
''')


E, I = symbols('E, I')
R1, R2 = symbols('R1, R2')
b = Beam(30, E, I)
b.apply_load(8, 0, -1)
b.apply_load(R1, 10, -1)
b.apply_load(R2, 30, -1)
b.apply_load(120, 30, -2)
b.bc_deflection.append((10, 0))
b.bc_deflection.append((30, 0))
b.solve_for_reaction_loads(R1, R2)
b.reaction_loads
b.load
b.shear_force()
b.bending_moment()
b.slope()
b.deflection()


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
