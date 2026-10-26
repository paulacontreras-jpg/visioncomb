import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Visión por Computador",
    page_icon="👁️",
    layout="wide",
)

# Estilos personalizados
st.markdown(
    """
    <style>
    .hero {
        padding: 2.5rem 2rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(37, 117, 252, 0.3);
    }
    .hero h1 { font-size: 3rem; margin-bottom: 0.3rem; color: white; }
    .hero p  { font-size: 1.2rem; opacity: 0.9; margin: 0; }

    .card {
        padding: 1.5rem;
        border-radius: 16px;
        background: rgba(128, 128, 128, 0.08);
        border: 1px solid rgba(128, 128, 128, 0.25);
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18);
    }
    .card .icon { font-size: 3rem; }
    .card h3 { margin: 0.5rem 0; }
    .card p  { opacity: 0.85; }
    .tag {
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        font-size: 0.8rem;
        background: #2575fc22;
        color: #2575fc;
        margin-right: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Encabezado
st.markdown(
    """
    <div class="hero">
        <h1>👁️ Visión por Computador</h1>
        <p>Clasifica imágenes y detecta objetos con inteligencia artificial</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Elige una app en el menú lateral 👈")

# Tarjetas
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="icon">🧠</div>
            <h3>Teachable Machine</h3>
            <p>Clasificación de imágenes con tu propio modelo entrenado.</p>
            <span class="tag">Clasificación</span>
            <span class="tag">Modelo propio</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="icon">🎯</div>
            <h3>YOLO</h3>
            <p>Detección de objetos en tiempo real sobre tus imágenes.</p>
            <span class="tag">Detección</span>
            <span class="tag">Tiempo real</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# Cómo usarla
st.info("💡 **Cómo empezar:** abre el menú lateral, elige una app y sube una imagen o usa tu cámara.")

# Barra lateral
with st.sidebar:
    st.header("🧭 Navegación")
    st.caption("Selecciona una página para comenzar.")
    st.markdown("---")
    st.caption("Hecho con ❤️ usando Streamlit")
