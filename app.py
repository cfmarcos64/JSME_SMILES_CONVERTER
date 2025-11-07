import streamlit as st
from st_jsme_editor import st_jsme_editor # Importa el componente

st.set_page_config(layout="centered")

st.title("Componente JSME Editor con Streamlit")

# Valor inicial de SMILES (Paracetamol)
initial_smiles = "CC(=O)Nc1ccc(O)cc1"

st.header("1. Editor de Moléculas")

# Llama al componente personalizado
# La variable 'smiles_value' contendrá el SMILES actual del editor.
smiles_value = st_jsme_editor(
    smiles=initial_smiles,
    height=400, # Altura del lienzo
    key="jsme_input"
)

st.header("2. Valor Retornado")
st.code(smiles_value, language="text")

if smiles_value:
    st.success(f"SMILES actual en el editor: {smiles_value}")
else:
    st.info("Dibuja una molécula para obtener el SMILES.")

# Nota: Este código debe estar en la raíz de tu proyecto.
