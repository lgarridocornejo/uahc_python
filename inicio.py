import streamlit as st
import pandas as pd
import datetime
import os

# Diccionario solo de códigos válidos
codigos_validos = {
    "d6364414": "pruebas/prueba_d6364414.ipynb",
    "de2913d7": "pruebas/prueba_de2913d7.ipynb",
    "424459e2": "pruebas/prueba_424459e2.ipynb",
    "6d31e673": "pruebas/prueba_6d31e673.ipynb",
    "2471d43d": "pruebas/prueba_2471d43d.ipynb",
    "9bfefeb0": "pruebas/prueba_9bfefeb0.ipynb",
    "a74c8c3a": "pruebas/prueba_a74c8c3a.ipynb",
    "ad8a01b6": "pruebas/prueba_ad8a01b6.ipynb",
    "617fbf7e": "pruebas/prueba_617fbf7e.ipynb",
    "e9f4b916": "pruebas/prueba_e9f4b916.ipynb",
    "cd917754": "pruebas/proyecto_cd917754.ipynb",
    "9a668548": "pruebas/proyecto_9a668548.ipynb",
    "0b9cf1ec": "pruebas/proyecto_0b9cf1ec.ipynb",
    "acd71a71": "pruebas/proyecto_acd71a71.ipynb",
    "f4f9bf9f": "pruebas/proyecto_f4f9bf9f.ipynb",
    "6b558034": "pruebas/proyecto_6b558034.ipynb",
    "0d5dfc8d": "pruebas/proyecto_0d5dfc8d.ipynb",
    "1bbad4bf": "pruebas/proyecto_1bbad4bf.ipynb"
}

# Crear archivo de registro si no existe
registro_file = "registro_descargas.csv"
if not os.path.isfile(registro_file):
    df_registro = pd.DataFrame(columns=["codigo", "nombre", "evento", "fecha_hora"])
    df_registro.to_csv(registro_file, index=False)

# Función para registrar eventos
def registrar_evento(codigo, nombre, evento):
    df = pd.read_csv(registro_file)
    nuevo_registro = {
        "codigo": codigo,
        "nombre": nombre,
        "evento": evento,
        "fecha_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
    df.to_csv(registro_file, index=False)

# Interfaz de Streamlit
st.title("📚 Portal de Pruebas y Proyectos de Python")
st.subheader("Bienvenido al sistema de entrega de pruebas y proyectos")

codigo_ingresado = st.text_input("🔑 Ingrese su código de acceso:").lower()
nombre_ingresado = st.text_input("👤 Ingrese nombre:")

if codigo_ingresado and nombre_ingresado:
    if codigo_ingresado in codigos_validos:
        st.success(f"¡Bienvenido {nombre_ingresado}! 🎓")

        archivo_path = codigos_validos[codigo_ingresado]
        
        # Botón para descargar la prueba
        with open(archivo_path, "rb") as f:
            contenido = f.read()

        if st.download_button(
            label="📥 Descargar tu archivo",
            data=contenido,
            file_name=os.path.basename(archivo_path),
            mime="application/json"
        ):
            registrar_evento(codigo_ingresado, nombre_ingresado, "Descarga prueba")
            st.info("Recuerda trabajar en tu archivo y enviarlo por el medio indicado (correo o Moodle).")
    else:
        st.error("❌ Código inválido. Intente nuevamente.")
