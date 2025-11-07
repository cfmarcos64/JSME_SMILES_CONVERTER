import streamlit.components.v1 as components
import os

# Determina la ruta absoluta del directorio donde se encuentra este archivo.
_ROOT = os.path.dirname(os.path.abspath(__file__))

# Concatena con 'frontend' para encontrar la carpeta que contiene el index.html.
_FRONTEND_DIR = os.path.join(_ROOT, "frontend")

# Nombre interno del componente
_COMPONENT_NAME = "jsme_editor"

# Define el modo de ejecución (True para cargar desde archivos locales, False para URL de desarrollo)
_RELEASE = True 

if _RELEASE:
    # En modo release, Streamlit carga los archivos desde el directorio especificado.
    _jsme_component = components.declare_component(
        _COMPONENT_NAME, 
        path=_FRONTEND_DIR
    )
else:
    # Este es el modo de desarrollo (normalmente localhost:3001 si usas npm start).
    _jsme_component = components.declare_component(
        _COMPONENT_NAME,
        url="http://localhost:5173"
    )


def jsme_editor(smiles: str = "", height: int = 400, key=None) -> str:
    """
    Muestra el editor JSME de dibujo de estructuras químicas.
    
    :param smiles: El SMILES inicial (canónico) de la molécula a cargar.
    :param height: La altura del editor JSME en píxeles.
    :param key: Clave única para el componente Streamlit.
    :return: El SMILES no canónico de la estructura actualmente dibujada, 
             actualizado en tiempo real por el usuario.
    """
    
    # Llama a la función del componente de Streamlit, pasando los argumentos (props)
    # al frontend de JavaScript. El valor de retorno es lo que JS nos devuelve.
    component_value = _jsme_component(
        smiles=smiles, 
        height=height, 
        key=key, 
        # El valor por defecto se usa para la inicialización del estado del componente
        default=smiles 
    )

    return component_value