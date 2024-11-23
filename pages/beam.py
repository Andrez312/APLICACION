import streamlit as st
from sympy import symbols
from sympy.physics.continuum_mechanics.beam import Beam
import sympy as sp

st.set_page_config(page_title="Beam", page_icon="👾", layout="wide")

# Título y descripción
st.title("Mecánica de Vigas con SymPy: Momento Flector Máximo")
st.text("El método apply_load de la clase Beam en SymPy permite aplicar cargas puntuales, distribuidas y momentos a vigas. Se pueden especificar magnitudes, direcciones y puntos de aplicación o usar funciones simbólicas para distribuciones variables. Es esencial para analizar el comportamiento estructural de vigas bajo diferentes condiciones.")

codigo = 'apply_load(valor, inicio, orden, fin=Ninguno)'
st.code(codigo, language="phyton")

st.markdown("""
Este método suma las cargas dadas a un objeto de viga en particular.

Parámetros:
value : Sintipificable

El valor insertado debe tener las unidades [Fuerza/(Distancia**(n+1)] donde n es el orden de la carga aplicada. Unidades para cargas aplicadas:

-Por momentos, unidad = kN*m

-Para cargas puntuales, unidad = kN

-Para carga distribuida constante, unidad = kN/m

-Para cargas en rampa, unidad = kN/m/m

-Para cargas en rampa parabólica, unidad = kN/m/m/m

… y así sucesivamente.

start : Sintipible

El punto de inicio de la carga aplicada. Para momentos puntuales y Fuerzas puntuales: Esta es la ubicación de la aplicación.

orden : Entero

El orden de la carga aplicada.

-Por momentos, orden = -2

-Para cargas puntuales, orden =-1

-Para carga distribuida constante, orden = 0

-Para cargas en rampa, pedido = 1

-Para cargas de rampa parabólica, pedido = 2

… y así sucesivamente.

end : Sympificable, opcional

Un argumento opcional que se puede usar si la carga tiene un punto final dentro de la longitud de la viga.
""")

st.code('''
-apply_load(): Aplica una carga (puntual, distribuida, o momento) a la viga.
-apply_support(): Define condiciones de apoyo (empotrado, simple, rodillo).
-reaction_loads: Calcula las reacciones en los apoyos.
-bending_moment(): Calcula el momento flector a lo largo de la viga.
-shear_force(): Calcula la fuerza cortante a lo largo de la viga.
-deflection(): Determina la deflexión (desplazamiento) de la viga bajo carga.
-slope(): Calcula la pendiente de la viga en cada punto.
-boundary_conditions: Define las condiciones de contorno de la viga.
-length: Longitud de la viga.
-load: Representación simbólica de las cargas aplicadas.
-max_bmoment(), max_deflection(), max_fuerza_de_corte(): Encuentran los valores máximos de momento flector, deflexión y fuerza cortante.
-draw() y plot_*(): Generan gráficos para visualizar momento, deflexión, fuerza cortante, etc.
''')

st.markdown("#### codigo")
st.code("""
        from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
E, I = symbols('E, I')
b = Beam(4, E, I)
b.apply_load(-3, 0, -2)
b.apply_load(4, 2, -1)
b.apply_load(-2, 2, 2, end=3)
b.load
-3*SingularityFunction(x, 0, -2) + 4*SingularityFunction(x, 2, -1) - 2*SingularityFunction(x, 2, 2) + 2*SingularityFunction(x, 3, 0) + 4*SingularityFunction(x, 3, 1) + 2*SingularityFunction(x, 3, 2)
       """, language="phyton")

st.markdown("#### ejemplo")
st.text("Una viga en voladizo de 9 metros de longitud tiene una carga constante distribuida de 8 kN/m Se aplica hacia abajo desde el extremo fijo a una distancia de 5 metros. A en sentido contrario a las agujas del reloj Se aplica un momento de 50 kN-m a 5 metros del extremo fijo. Por último, una Se aplica una carga puntual de 12 kN en el extremo libre de la viga.")

st.code('''
        from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
E, I = symbols('E, I')
b = Beam(4, E, I)
b.apply_load(-3, 0, -2)
b.apply_load(4, 2, -1)
b.apply_load(5, 2, -1)
b.load
b.applied_loads
        ''')


E, I = symbols('E, I')
b = Beam(4, E, I)
b.apply_load(-3, 0, -2)
b.apply_load(4, 2, -1)
b.apply_load(5, 2, -1)
b.load
b.applied_loads        

st.markdown("##### Parametros")
st.write("""
         
value : Sintipificable

El valor insertado debe tener las unidades [Fuerza/(Distancia**(n+1)] donde n es el orden de la carga aplicada. Unidades para cargas aplicadas:

Por momentos, unidad = kN*m

-Para cargas puntuales, unidad = kN

-Para carga distribuida constante, unidad = kN/m

-Para cargas en rampa, unidad = kN/m/m

-Para cargas en rampa parabólica, unidad = kN/m/m/m

… y así sucesivamente.

start : Sintipible

-El punto de inicio de la carga aplicada. Para momentos puntuales y Fuerzas puntuales: Esta es la ubicación de la aplicación.

orden : Entero

El orden de la carga aplicada.

-Por momentos, orden = -2

-Para cargas puntuales, orden =-1

-Para carga distribuida constante, orden = 0

-Para cargas en rampa, pedido = 1

-Para cargas de rampa parabólica, pedido = 2

… y así sucesivamente.

end : Sympificable, opcional

Un argumento opcional que se puede usar si la carga tiene un punto final dentro de la longitud de la viga.
""")

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