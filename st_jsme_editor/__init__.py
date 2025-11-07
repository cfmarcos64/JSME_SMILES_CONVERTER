# -*- coding: utf-8 -*-
import streamlit.components.v1 as components
import os

# Determina si estamos en modo de desarrollo local o en modo de producción (release)
# Cambia a True para Streamlit Cloud
_RELEASE = False 

# Configuración de rutas
_ROOT = os.path.dirname(os.path.abspath(__file__))
_FRONTEND_DIR = os.path.join(_ROOT, "frontend")

if not _RELEASE:
    # MODO DESARROLLO: Carga el componente desde el servidor de desarrollo (Vite)
    # AJUSTADO AL PUERTO 5173
    _component_func = components.declare_component(
        "jsme_editor",
        url="http://localhost:5173", 
    )
else:
    # MODO PRODUCCIÓN: Carga los assets estáticos compilados en el subdirectorio 'frontend'
    _component_func = components.declare_component("jsme_editor", path=_FRONTEND_DIR)


def jsme_editor(smiles: str, key=None, height: int = 400):
    """
    Muestra el editor JSME y devuelve el SMILES no canónico de la estructura.

    Args:
        smiles (str): El SMILES canónico inicial que se cargará en el editor.
        key (str, optional): La clave única del componente para Streamlit. Defaults to None.
        height (int, optional): Altura del editor en píxeles. Defaults to 400.

    Returns:
        str: El SMILES JSME no canónico de la estructura actual.
    """
    component_value = _component_func(
        smiles=smiles, 
        height=height, 
        key=key, 
        # El valor por defecto debe ser el SMILES inicial o una cadena vacía
        default=smiles or ""
    )
    return component_value
