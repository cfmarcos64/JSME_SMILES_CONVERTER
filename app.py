import streamlit as st

# Importamos el componente personalizado que definimos en st_jsme_editor/__init__.py
# Asume que este archivo (app.py) se ejecuta un nivel por encima del directorio st_jsme_editor
from st_jsme_editor import jsme_editor

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Editor JSME en Streamlit", 
    layout="wide"
)

st.title("🧪 Editor Molecular JSME Integrado")
st.markdown(
    """
    Este es un componente personalizado que utiliza el editor JSME para dibujar 
    estructuras químicas. El SMILES canónico de entrada se carga en el editor, 
    y el SMILES no canónico modificado se envía de vuelta a Python en tiempo real.
    """
)

st.sidebar.header("Opciones de Entrada")
# Campo de entrada para proporcionar un SMILES inicial (ejemplo: Paracetamol)
canonical_smiles_input = st.sidebar.text_area(
    "Introduce el SMILES Canónico Inicial:",
    "CC(=O)Nc1ccc(O)cc1",
    height=150,
    help="Introduce un SMILES válido para cargarlo en el editor."
)

editor_height = st.sidebar.slider(
    "Altura del Editor (píxeles):",
    min_value=300,
    max_value=800,
    value=450,
    step=50
)

st.markdown("---")

# --- Renderizado del Componente JSME ---
st.header("1. Área de Dibujo Molecular")
# Llamamos a nuestra función de componente personalizada
# El valor de retorno es el SMILES no canónico enviado por el JS/Frontend
jsme_smiles_output = jsme_editor(
    smiles=canonical_smiles_input.strip(), 
    height=editor_height,
    key="jsme_component" # Clave obligatoria para componentes
)

# --- Visualización del Resultado ---
st.header("2. Resultado en Streamlit")

if jsme_smiles_output:
    st.success("¡Estructura recibida de JSME!")
    st.subheader("SMILES JSME (No Canónico):")
    st.code(jsme_smiles_output, language='text')
    
    # Muestra el valor de entrada original para comparación
    st.caption(f"El SMILES de entrada (Canónico) fue: **{canonical_smiles_input.strip()}**")
else:
    st.info("Dibuja una estructura en el editor JSME para ver el SMILES no canónico aquí.")

st.markdown("---")
st.markdown("*(Nota: La diferencia entre SMILES canónico y no canónico se debe a que JSME genera el SMILES en función de cómo se dibujó la molécula).*")