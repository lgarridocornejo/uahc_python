
import streamlit as st
import yagmail
import pandas as pd
import datetime
import os

# Configura tu correo
EMAIL_EMISOR = "tucorreo@gmail.com"
CONTRASENA_APP = "tu_contrasena_app"
EMAIL_RECEPTOR = "tucorreo@gmail.com"  # Puedes ser el mismo

# Inicializar yagmail
yag = yagmail.SMTP(EMAIL_EMISOR, CONTRASENA_APP)

# Diccionario de códigos y nombres
codigos = {
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
}

st.title("📚 Portal de Entrega de Pruebas de Python")

codigo_ingresado = st.text_input("🔑 Ingrese su código de acceso:")
nombre_ingresado = st.text_input("✏️ Ingrese su nombre completo:")

if codigo_ingresado and nombre_ingresado:
    if codigo_ingresado in codigos and codigos[codigo_ingresado]["nombre"].lower() == nombre_ingresado.lower():
        alumno = codigos[codigo_ingresado]
        st.success(f"¡Bienvenido {alumno['nombre']}! 🎓")

        archivo_path = alumno["archivo"]

        with open(archivo_path, "rb") as f:
            contenido = f.read()

        if st.download_button(
            label="📥 Descargar tu prueba",
            data=contenido,
            file_name=os.path.basename(archivo_path),
            mime="application/json"
        ):
            st.info("Recuerda guardar tu archivo antes de enviarlo de vuelta.")

        st.markdown("---")
        st.subheader("📤 Subir prueba resuelta")

        archivo_subido = st.file_uploader("Selecciona tu archivo resuelto:", type=["ipynb"])

        if archivo_subido:
            st.success("✅ Archivo recibido. Enviando por correo electrónico...")

            # Guardar archivo temporalmente
            temp_file_path = f"temp_{archivo_subido.name}"
            with open(temp_file_path, "wb") as f:
                f.write(archivo_subido.read())

            # Enviar correo
            yag.send(
                to=EMAIL_RECEPTOR,
                subject=f"Prueba resuelta de {alumno['nombre']}",
                contents=f"Adjunto archivo de la prueba enviada por {alumno['nombre']}.",
                attachments=temp_file_path
            )

            st.success("📬 ¡Archivo enviado exitosamente!")

            # Borrar archivo temporal
            os.remove(temp_file_path)

    else:
        st.error("❌ Código o nombre incorrecto. Intente nuevamente.")

