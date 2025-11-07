import os
import streamlit.components.v1 as components

# Determina si estamos en modo de desarrollo o producción
# _RELEASE = True activa el modo de producción.
_RELEASE = True

if not _RELEASE:
    # Si estamos en desarrollo, apuntamos al servidor local de Vite (no usamos este modo aquí, pero se mantiene la estructura)
    _component_func = components.declare_component(
        "st_jsme_editor",
        url="http://localhost:3001",
    )
else:
    # Modo de Producción (Deployment):
    # La ruta apunta directamente a la carpeta 'frontend' que contiene el index.html final.
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    _FRONTEND_DIR = os.path.join(parent_dir, "frontend")
    
    _component_func = components.declare_component(
        "st_jsme_editor",
        path=_FRONTEND_DIR
    )

def st_jsme_editor(smiles: str = "", height: int = 400, key=None):
    """
    Componente Streamlit para el editor molecular JSME.

    :param smiles: El SMILES inicial a cargar en el editor.
    :param height: La altura del lienzo del editor en píxeles.
    :param key: Clave única del componente para Streamlit.
    :return: El SMILES actual editado por el usuario.
    """
    component_value = _component_func(smiles=smiles, height=height, key=key, default=smiles)
    return component_value

if not _RELEASE:
    # Bloque para probar la funcionalidad localmente (solo en modo desarrollo)
    # Importar solo si no está en release para evitar errores de importación en el ambiente de producción
    import streamlit as st
    st.set_page_config(layout="centered")
    
    st.title("Prueba Local del Componente JSME")
    
    initial_smiles = "CC(=O)Nc1ccc(O)cc1" # Paracetamol
    
    value = st_jsme_editor(smiles=initial_smiles, height=400, key="local_jsme")
    
    st.write(f"SMILES retornado: {value}")
