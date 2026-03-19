# -*- coding: utf-8 -*-
import re
import unicodedata

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Guía Técnica Biomédica",
    layout="wide",
)


st.markdown(
    """
<style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(0, 104, 55, 0.12), transparent 28%),
            linear-gradient(180deg, #f4f8f4 0%, #eef4ef 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1250px;
    }

    .header-panel {
        background: linear-gradient(135deg, #006837 0%, #0b8f4a 100%);
        padding: 28px 32px;
        border-radius: 22px;
        color: white;
        box-shadow: 0 18px 40px rgba(0, 104, 55, 0.18);
        margin-bottom: 24px;
    }

    .header-kicker {
        text-transform: uppercase;
        letter-spacing: 0.18em;
        font-size: 0.8rem;
        font-weight: 700;
        opacity: 0.85;
        margin-bottom: 12px;
    }

    .header-title {
        font-size: 2.2rem;
        line-height: 1.2;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .header-subtitle {
        font-size: 1rem;
        opacity: 0.95;
        max-width: 780px;
    }

    .selector-card {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid rgba(0, 104, 55, 0.12);
        border-radius: 20px;
        padding: 22px 22px 10px 22px;
        box-shadow: 0 14px 34px rgba(24, 39, 75, 0.08);
        margin: 10px 0 22px 0;
        backdrop-filter: blur(6px);
    }

    .selector-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0d4728;
        margin-bottom: 6px;
    }

    .selector-help {
        font-size: 0.95rem;
        color: #527060;
        margin-bottom: 14px;
    }

    div[data-baseweb="select"] > div {
        border-radius: 14px !important;
        border: 1px solid rgba(0, 104, 55, 0.18) !important;
        min-height: 54px !important;
        box-shadow: none !important;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: #0b8f4a !important;
    }

    .equipo-hero {
        background: linear-gradient(135deg, #ffffff 0%, #f7fbf8 100%);
        border-radius: 24px;
        padding: 26px 30px;
        border: 1px solid rgba(0, 104, 55, 0.10);
        box-shadow: 0 18px 38px rgba(20, 33, 61, 0.09);
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
    }

    .equipo-hero::after {
        content: "";
        position: absolute;
        inset: auto -40px -40px auto;
        width: 170px;
        height: 170px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(0, 104, 55, 0.14), rgba(0, 104, 55, 0));
    }

    .equipo-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.18em;
        color: #5c7668;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .equipo-title {
        font-size: 2rem;
        line-height: 1.2;
        font-weight: 800;
        color: #073b22;
        margin-bottom: 8px;
    }

    .equipo-caption {
        font-size: 1rem;
        color: #587061;
        max-width: 750px;
    }

    .card {
        background: rgba(255, 255, 255, 0.94);
        padding: 18px 20px;
        border-radius: 16px;
        border: 1px solid rgba(0, 104, 55, 0.09);
        box-shadow: 0 10px 28px rgba(24, 39, 75, 0.07);
        margin-bottom: 15px;
    }

    .card-title {
        font-weight: 700;
        font-size: 1rem;
        color: #006837;
        margin-bottom: 8px;
    }

    .bullet-list {
        margin: 0;
        padding-left: 1.35rem;
    }

    .bullet-list li {
        margin-bottom: 0.5rem;
        line-height: 1.55;
        color: #24352c;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 999px;
        padding: 10px 16px;
        background: rgba(255, 255, 255, 0.7);
    }
</style>
""",
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="header-panel">
        <div class="header-kicker">Secretaría de Salud e inlcusión Social de Antioquia</div>
        <div class="header-title">Guía Interactiva de Especificaciones Técnicas de Equipos Biomédicos</div>
        <div class="header-subtitle">
            Consulta para revisar la información técnica, operativa y normativa
            de dispositivos biomédicos desde una sola interfaz.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


def limpiar(texto):
    texto = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode("ascii")
    texto = texto.lower().strip()
    texto = re.sub(r"[^a-z0-9]+", "_", texto)
    return texto


def formatear_lista(texto):
    if pd.isna(texto):
        return ""

    lineas = str(texto).split("\n")
    items = []

    for linea in lineas:
        linea = linea.strip()
        linea = re.sub(r"^\d+\.\s*", "", linea)
        if linea:
            items.append(f"<li>{linea}</li>")

    if not items:
        return ""

    return f'<ul class="bullet-list">{"".join(items)}</ul>'


def formatear_normas(texto):
    if pd.isna(texto):
        return ""

    texto = str(texto)
    partes = texto.split("*")
    intro = partes[0].strip()
    bullets = []

    for p in partes[1:]:
        p = p.strip().replace("\n", " ")
        if p:
            bullets.append(f"- {p}")

    if bullets:
        return intro + "\n\n" + "\n".join(bullets)
    return intro


def formatear_servicios(texto):
    if pd.isna(texto):
        return ""

    partes = str(texto).split(",")
    intro = partes[0].strip()
    bullets = []

    for p in partes[1:]:
        p = p.strip()
        if p:
            bullets.append(f"- {p}")

    if bullets:
        return intro + "\n\n" + "\n".join(bullets)
    return intro


@st.cache_data(ttl=60)
def cargar_datos():
    url = "https://docs.google.com/spreadsheets/d/1Hav7p3RYY0FjdN3ztwo-4mWa382xPzpqZDHpwZGmXok/export?format=csv"
    df = pd.read_csv(url, engine="python")
    df.columns = [limpiar(col) for col in df.columns]
    return df


df = cargar_datos()


st.markdown(
    """
    <div class="selector-card">
        <div class="selector-title">Buscar equipo biomédico</div>
        <div class="selector-help">
            Escribe o selecciona un equipo para ver su ficha técnica, gestión hospitalaria y marco normativo.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

equipo = st.selectbox(
    "Comience a escribir el nombre del equipo",
    sorted(df["nombre"].dropna().unique()),
    index=None,
    placeholder="Ej: Centrifuga, Agitador, Balanza...",
    label_visibility="collapsed",
)

if equipo is None:
    st.info("Selecciona un equipo para visualizar su informacion.")
    st.stop()

ficha = df[df["nombre"] == equipo].iloc[0]


st.markdown(
    f"""
    <div class="equipo-hero">
        <div class="equipo-label">Equipo</div>
        <div class="equipo-title">{equipo}</div>
        <div class="equipo-caption">
            Visualización de especificaciones, requerimientos y documentación técnica del equipo.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


tabs = st.tabs(
    [
        "Información general",
        "Requisitos técnicos",
        "Gestión hospitalaria",
        "Información normativa",
    ]
)


with tabs[0]:
    if "codigo_gmdn" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Código GMDN</div>{ficha["codigo_gmdn"]}</div>',
            unsafe_allow_html=True,
        )

    if "definicion" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Definición</div>{ficha["definicion"]}</div>',
            unsafe_allow_html=True,
        )

    if "finalidad_clinica" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Finalidad clinica</div>{ficha["finalidad_clinica"]}</div>',
            unsafe_allow_html=True,
        )

    if "servicios" in ficha:
        servicios = formatear_servicios(ficha["servicios"])
        st.markdown(
            f'<div class="card"><div class="card-title">Servicios</div>{servicios}</div>',
            unsafe_allow_html=True,
        )


with tabs[1]:
    if "especificaciones_tecnicas" in ficha:
        texto = formatear_lista(ficha["especificaciones_tecnicas"])
        st.markdown(
            f'<div class="card"><div class="card-title">Especificaciones técnicas</div>{texto}</div>',
            unsafe_allow_html=True,
        )

    if "preinstalacion" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Preinstalación</div>{ficha["preinstalacion"]}</div>',
            unsafe_allow_html=True,
        )

    if "accesorios_consumibles_y_repuestos" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Accesorios, consumibles y repuestos</div>{ficha["accesorios_consumibles_y_repuestos"]}</div>',
            unsafe_allow_html=True,
        )


with tabs[2]:
    if "entrenamiento" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Entrenamiento</div>{ficha["entrenamiento"]}</div>',
            unsafe_allow_html=True,
        )

    if "garantia" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Garantía</div>{ficha["garantia"]}</div>',
            unsafe_allow_html=True,
        )

    if "mantenimiento" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Mantenimiento</div>{ficha["mantenimiento"]}</div>',
            unsafe_allow_html=True,
        )


with tabs[3]:
    if "documentacion" in ficha:
        texto = formatear_normas(ficha["documentacion"])
        st.markdown(
            f'<div class="card"><div class="card-title">Documentación</div>{texto}</div>',
            unsafe_allow_html=True,
        )

    if "normas_para_el_fabricante" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Normas para el fabricante</div>{ficha["normas_para_el_fabricante"]}</div>',
            unsafe_allow_html=True,
        )

    if "normas_para_el_producto" in ficha:
        texto = formatear_normas(ficha["normas_para_el_producto"])
        st.markdown(
            f'<div class="card"><div class="card-title">Normas para el producto</div>{texto}</div>',
            unsafe_allow_html=True,
        )

    if "normas_sobre_la_validacion_clinica" in ficha:
        st.markdown(
            f'<div class="card"><div class="card-title">Validacion clinica</div>{ficha["normas_sobre_la_validacion_clinica"]}</div>',
            unsafe_allow_html=True,
        )