import streamlit as st
from sympy.physics.continuum_mechanics.cable import Cable
st.set_page_config(page_title="Cable", page_icon="👾", layout="wide")

st.title("Cable (Docstring)")
st.write("""
Este módulo se puede utilizar para resolver problemas relacionados con a cables 2D.
Los cables son estructuras de ingeniería que soportan las cargas transversales aplicadas a través de la tracción resistencia desarrollada en sus miembros.
Los cables son ampliamente utilizados en puentes colgantes, tensión Tramo de plataformas marinas, líneas de transmisión y hallazgo uso en varias otras aplicaciones de ingeniería.
""")

st.code('''
Clase sympy.physics.continuum_mechanics.cable.Cable(support_1, support_2)[fuente]
''')

st.code("""
Los codigos de cable son:
-Cable.apply_length()- longitud
-Cable.apply_load()- orden, carga
-Cable.change_support()- Cambia el soporte
-Cable.left_support- devuelve la posicion al soporte izquierdo
-Cable.longitud- devuelve longitud de cable
-Cable.loads -devuelve a magnitud y direccion de las cargas
-Cable.loads_position- devuelve posicion a cargas puntuales
-Cable.reaction_loads- devuelve la reaccion en los apoyos
-Cable.remove_loads()- elimina cargas especificadas
-Cable.right_support- devuelve posicion de soporte derecho
-Cable.solve()- Este método resuelve las fuerzas de reacción en los soportes, la tensión desarrollada en el cable y actualiza la longitud del cable.
-Cable.soporta- Devuelve los soportes del cable junto con su Posiciones.
-Cable.tensión- Devuelve la tensión desarrollada en el cable debido a las cargas aplicado.
-Cable.tension_at()- Devuelve la tensión a un valor dado de x desarrollado debido a carga distribuida
""")

st.write("""
Los cables son estructuras de ingeniería que soportan las cargas transversales aplicadas a través de la tracción resistencia desarrollada en sus miembros.

Los cables son ampliamente utilizados en puentes colgantes, tensión Tramo de plataformas marinas, líneas de transmisión y hallazgo uso en varias otras aplicaciones de ingeniería.

""")

st.markdown("### Ejemplo")
st.text("Se admite un cable en (0, 10) y (10, 10). Dos cargas puntuales actuando verticalmente hacia abajo actúan sobre el cable, uno con magnitud 3 kN y actuando a 2 metros del apoyo izquierdo y 3 metros por debajo del mismo, mientras el otro con magnitud 2 kN está a 6 metros del soporte izquierdo y 6 metros por debajo de ella.")
st.code('''
from sympy.physics.continuum_mechanics.cable import Cable
c = Cable(('A', 0, 10), ('B', 10, 10))
c.apply_load(-1, ('P', 2, 7, 3, 270))
c.apply_load(-1, ('Q', 6, 4, 2, 270))
c.loads
c.loads_position
''')


c = Cable(('A', 0, 10), ('B', 10, 10))
c.apply_load(-1, ('P', 2, 7, 3, 270))
c.apply_load(-1, ('Q', 6, 4, 2, 270))
c.loads
c.loads_position
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
