import streamlit as st

# modificar titulo de la aplicacion #
st.set_page_config(page_title="Mecanica de fluidos", page_icon="💧", layout="wide")

#titulo de la pagina
st.title("Mecánica de Fluidos: La Ciencia Detrás del Movimiento y Comportamiento de Líquidos y Gases")

#introduccion
st.text("La mecánica de fluidos es una rama de la física que se encarga del estudio del comportamiento de los fluidos (líquidos y gases) y las fuerzas que actúan sobre ellos. Es una disciplina fundamental en la ingeniería, ya que permite entender y modelar fenómenos naturales, así como diseñar sistemas y dispositivos tecnológicos que interactúan con fluidos. Los fluidos se caracterizan por su capacidad para fluir y adaptarse a la forma de los recipientes que los contienen, a diferencia de los sólidos que mantienen su forma. El estudio de los fluidos se divide en dos áreas principales:")
st.write("""
Dinámica de fluidos: estudia los fluidos en movimiento y los efectos de fuerzas externas sobre ellos, incluyendo conceptos como el flujo, la viscosidad y la turbulencia.
Estática de fluidos: analiza los fluidos en reposo y las fuerzas que ejercen, como la presión.         
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

st.image('C:/Users/andre/Downloads/imagen1.jpg')

st.markdown("### importancia de mecanica de fluidos")
st.write("""
Importancia de la Mecánica de Fluidos
La mecánica de fluidos es esencial en múltiples campos, como:

Ingeniería civil e hidráulica: para el diseño de presas, canales y sistemas de distribución de agua.
Ingeniería mecánica: en el diseño de turbinas, bombas y sistemas de refrigeración.
Aeronáutica: para entender el flujo de aire alrededor de aeronaves y optimizar su diseño.
Medicina: en el estudio del flujo sanguíneo en el cuerpo humano y el desarrollo de dispositivos médicos como válvulas cardíacas artificiales.
Climatología: para modelar la circulación atmosférica y los patrones climáticos.
""")


st.markdown("### Conceptos fundamentales")
st.write("""

Presión: es la fuerza ejercida por un fluido sobre una superficie por unidad de área. En un fluido en reposo, la presión aumenta con la profundidad debido al peso del fluido sobre él.

Densidad: representa la masa del fluido por unidad de volumen. Es un parámetro clave para calcular el comportamiento de los fluidos.

Viscosidad: mide la resistencia de un fluido a fluir, es decir, su fricción interna. Un fluido con alta viscosidad (como la miel) fluye más lentamente que uno con baja viscosidad (como el agua).

Ecuación de Bernoulli: una de las herramientas principales en la dinámica de fluidos, relaciona la presión, la velocidad y la altura de un fluido en movimiento, siendo fundamental para comprender fenómenos como el vuelo de un avión o el flujo en tuberías.

Número de Reynolds: un parámetro adimensional que determina si un flujo es laminar (suave y ordenado) o turbulento (caótico y desordenado).
         """)

st.image("C:/Users/andre/Downloads/OIP.jpg")

st.markdown("### aplicaciones practicas")
st.write("""
         
La mecánica de fluidos tiene un impacto directo en la vida diaria y en la tecnología moderna. Algunos ejemplos son:

El diseño de sistemas de aire acondicionado.
La predicción del clima.
El desarrollo de vehículos terrestres, marítimos y aéreos más eficientes.
La generación de energía hidroeléctrica y eólica.
""")

st.text("a la izquiera encontraras la barra lateral, con la tabla de contenidos.")

