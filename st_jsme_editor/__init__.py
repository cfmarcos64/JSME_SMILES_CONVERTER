# -*- coding: utf-8 -*-
import streamlit.components.v1 as components
import os

# Determina si estamos en modo de desarrollo local o en modo de producción (release)
# ESTO DEBE SER TRUE PARA EL DESPLIEGUE EN STREAMLIT CLOUD
_RELEASE = True 

# Configuración de rutas
_ROOT = os.path.dirname(os.path.abspath(__file__))
_FRONTEND_DIR = os.path.join(_ROOT, "frontend")

# CORRECCIÓN CRÍTICA: La ruta de los assets compilados es frontend/dist/
_FRONTEND_DIST_DIR = os.path.join(_ROOT, "frontend", "dist")

if not _RELEASE:
    # MODO DESARROLLO (SOLO PARA PRUEBAS LOCALES): Carga el componente desde el servidor Vite
    _component_func = components.declare_component(
        "jsme_editor",
        url="http://localhost:5173", 
    )
else:
    # MODO PRODUCCIÓN: Carga los assets estáticos compilados desde la carpeta 'dist'
    # Esta es la ruta que Streamlit Cloud DEBE usar.
    _component_func = components.declare_component("jsme_editor", path=_FRONTEND_DIST_DIR)


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
