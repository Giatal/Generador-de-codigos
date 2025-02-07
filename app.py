import streamlit as st

# Título de la aplicación
st.title("Generador de Páginas Dinámicas con Streamlit")

# Cuadro de texto donde el usuario ingresa el nombre de la página
pagina = st.text_input("Ingresa el nombre de la página que deseas ver:")

# Función para generar contenido basado en el nombre de la página
def generar_contenido(pagina):
    if pagina == "Inicio":
        st.header("Bienvenido a la Página de Inicio")
        st.write("Esta es la página principal donde puedes ver información general.")
        st.write("Puedes navegar a otras páginas escribiendo el nombre en el cuadro de arriba.")
    elif pagina == "Acerca de":
        st.header("Acerca de Nosotros")
        st.write("Esta es la página de información sobre el proyecto. Aquí puedes ver detalles sobre el propósito y los creadores.")
    elif pagina == "Servicios":
        st.header("Nuestros Servicios")
        st.write("En esta página, ofrecemos detalles sobre los servicios que brindamos. ¿Estás interesado en algo?")
    elif pagina == "Contacto":
        st.header("Contáctanos")
        st.write("En esta página puedes encontrar la información para ponerte en contacto con nosotros.")
        st.write("Teléfono: 123-456-7890")
        st.write("Correo: contacto@example.com")
    else:
        st.warning("Por favor, ingresa un nombre de página válido (Inicio, Acerca de, Servicios, Contacto).")

# Llamar a la función para generar contenido
if pagina:
    generar_contenido(pagina)
