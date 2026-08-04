import streamlit as st
import math
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

# Configuración inicial de la página
st.set_page_config(
    page_title="Matemáticas Discretas - UMG", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Control de estado para la pantalla de bienvenida / ingreso
if 'ingresado' not in st.session_state:
    st.session_state.ingresado = False

def ingresar():
    st.session_state.ingresado = True

# Estilos CSS personalizados (Colores Institucionales UMG: Azul Marino, Rojo y Dorado)
st.markdown("""
    <style>
    .umg-header {
        background: linear-gradient(135deg, #002147 0%, #8B0000 100%);
        padding: 35px 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        margin-bottom: 25px;
    }
    .umg-header h1 {
        color: #FFFFFF !important;
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .umg-header h3 {
        color: #F1C40F !important;
        font-size: 1.4rem !important;
        margin-top: 0 !important;
        font-weight: 600 !important;
    }
    .student-card {
        background-color: #1E1E2E;
        border-left: 6px solid #8B0000;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.3);
    }
    .student-name {
        font-weight: bold;
        font-size: 1.15rem;
        color: #FFFFFF;
    }
    .student-carnet {
        color: #F1C40F;
        font-weight: 600;
        font-size: 1rem;
        margin-top: 4px;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #8B0000 0%, #C0392B 100%) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 1.25rem !important;
        border-radius: 12px !important;
        border: none !important;
        width: 100% !important;
        height: 60px !important;
        box-shadow: 0 4px 12px rgba(139,0,0,0.5) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #C0392B 0%, #E74C3C 100%) !important;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# URL pública confiable del Logo UMG
LOGO_UMG_URL = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Logo-UMG.png"

# ---------------------------------------------------------
# PANTALLA 1: PORTADA / BIENVENIDA (ANTES DE INGRESAR)
# ---------------------------------------------------------
if not st.session_state.ingresado:
    st.markdown(f"""
        <div class="umg-header">
            <img src="{LOGO_UMG_URL}" width="120" style="margin-bottom: 15px; filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.5));">
            <h1>UNIVERSIDAD MARIANO GÁLVEZ DE GUATEMALA</h1>
            <h3>Facultad de Ingeniería en Sistemas de Información y Ciencias de la Computación</h3>
            <p style="font-size: 1.15rem; color: #E0E0E0; margin-top: 10px;">
                <b>Curso:</b> Matemáticas Discretas &nbsp;|&nbsp; <b>Proyecto Final:</b> Aplicación Interactiva de Algoritmos
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 👥 Integrantes del Equipo de Trabajo")
    st.write("Estudiantes encargados del desarrollo de esta plataforma:")
    
    students = [
        ("Anderson Geovany Lima Martínez", "5990 - 25 - 5819"),
        ("Ananda Saraí Samayoa", "5990 - 26 - 6172"),
        ("Alexandra Rosibel García Najarro", "5990 - 26 - 5430"),
        ("Caterin Alejandra Carrillo Hernandez", "5990 - 26 - 1630"),
        ("Guillermo Alexander Morales Figueroa", "5990 - 26 - 15032")
    ]
    
    col1, col2 = st.columns(2)
    for idx, (name, carnet) in enumerate(students):
        target_col = col1 if idx % 2 == 0 else col2
        with target_col:
            st.markdown(f"""
                <div class="student-card">
                    <div class="student-name">👤 {name}</div>
                    <div class="student-carnet">💳 Carnet: {carnet}</div>
                </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.button("🚀 INGRESAR A LA APLICACIÓN", on_click=ingresar)

# ---------------------------------------------------------
# APLICACIÓN PRINCIPAL (UNA VEZ SE PRESIONA INGRESAR)
# ---------------------------------------------------------
else:
    st.sidebar.markdown("### 🎓 UMG Discretas")
    st.sidebar.write("**Universidad Mariano Gálvez**")
    
    opcion = st.sidebar.radio(
        "Selecciona el módulo:",
        ["📋 Portada / Carátula", 
         "1. Combinaciones y Permutaciones", 
         "2. Producto Cartesiano", 
         "3. Valores de Áreas (Diagrama de Venn)"]
    )

    st.sidebar.markdown("---")
    if st.sidebar.button("⬅️ Salir al Inicio"):
        st.session_state.ingresado = False
        st.rerun()

    if opcion == "📋 Portada / Carátula":
        st.markdown(f"""
            <div class="umg-header">
                <img src="{LOGO_UMG_URL}" width="100" style="margin-bottom: 10px;">
                <h1>UNIVERSIDAD MARIANO GÁLVEZ DE GUATEMALA</h1>
                <h3>Facultad de Ingeniería en Sistemas</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.subheader("👥 Integrantes del Grupo")
        students = [
            ("Anderson Geovany Lima Martínez", "5990 - 25 - 5819"),
            ("Ananda Saraí Samayoa", "5990 - 26 - 6172"),
            ("Alexandra Rosibel García Najarro", "5990 - 26 - 5430"),
            ("Caterin Alejandra Carrillo Hernandez", "5990 - 26 - 1630"),
            ("Guillermo Alexander Morales Figueroa", "5990 - 26 - 15032")
        ]
        for name, carnet in students:
            st.write(f"* **{name}** — *Carnet: {carnet}*")

    elif opcion == "1. Combinaciones y Permutaciones":
        st.title("🔢 Combinaciones y Permutaciones")
        
        col1, col2 = st.columns(2)
        with col1:
            tipo = st.selectbox("Selecciona el tipo de operación:", ["Combinación (C)", "Permutación (P)"])
        with col2:
            n = st.number_input("Ingresa el valor de n (Total de elementos):", min_value=0, value=5)
            r = st.number_input("Ingresa el valor de r (Elementos seleccionados):", min_value=0, value=3)
            
        if st.button("Calcular Operación"):
            if r > n:
                st.error("Error: el valor de r no puede ser mayor que n.")
            else:
                st.markdown("---")
                st.subheader("📊 Presentación de Resultados")
                if tipo == "Combinación (C)":
                    res = math.comb(n, r)
                    st.latex(r"C(n, r) = \frac{n!}{r!(n-r)!}")
                    st.latex(rf"C({n}, {r}) = \frac{{{n}!}}{{{r}!({n}-{r})!}} = {res}")
                    st.success(f"**Resultado:** Existen **{res}** formas posibles de combinar los elementos.")
                else:
                    res = math.perm(n, r)
                    st.latex(r"P(n, r) = \frac{n!}{(n-r)!}")
                    st.latex(rf"P({n}, {r}) = \frac{{{n}!}}{{({n}-{r})!}} = {res}")
                    st.success(f"**Resultado:** Existen **{res}** formas posibles de permutar los elementos.")

    elif opcion == "2. Producto Cartesiano":
        st.title("✖️ Producto Cartesiano")
        
        cant_conjuntos = st.radio("Cantidad de conjuntos:", [2, 3], horizontal=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            txt_a = st.text_input("Conjunto A (separado por comas):", "1, 2")
        with col2:
            txt_b = st.text_input("Conjunto B (separado por comas):", "a, b")
        with col3:
            if cant_conjuntos == 3:
                txt_c = st.text_input("Conjunto C (separado por comas):", "x, y")
                
        if st.button("Calcular Producto Cartesiano"):
            st.markdown("---")
            st.subheader("📊 Presentación de Resultados")
            set_a = [x.strip() for x in txt_a.split(",") if x.strip()]
            set_b = [x.strip() for x in txt_b.split(",") if x.strip()]
            
            if cant_conjuntos == 2:
                prod = [(a, b) for a in set_a for b in set_b]
                st.latex(r"A \times B = \{(a, b) \mid a \in A \land b \in B\}")
                st.write(f"**Resultado ({len(prod)} elementos):**")
                st.code(f"A × B = {prod}")
            else:
                set_c = [x.strip() for x in txt_c.split(",") if x.strip()]
                prod = [(a, b, c) for a in set_a for b in set_b for c in set_c]
                st.latex(r"A \times B \times C = \{(a, b, c) \mid a \in A \land b \in B \land c \in C\}")
                st.write(f"**Resultado ({len(prod)} elementos):**")
                st.code(f"A × B × C = {prod}")

    elif opcion == "3. Valores de Áreas (Diagrama de Venn)":
        st.title("⚪ Valores de Áreas de Diagrama de Venn")
        
        cant_conjuntos = st.radio("¿Cuántos conjuntos deseas relacionar?", [2, 3], horizontal=True)
        
        if cant_conjuntos == 2:
            st.subheader("Selecciona el valor a calcular (Incógnita):")
            incognita = st.selectbox("Variable incógnita (?):", [
                "Total del Universo (U)", 
                "Conjunto A", 
                "Conjunto B", 
                "Intersección (A ∩ B)", 
                "Fuera de los conjuntos"
            ])
            
            col1, col2 = st.columns(2)
            with col1:
                u_val = st.number_input("Total Universo (U):", min_value=0, value=100, disabled=(incognita=="Total del Universo (U)"))
                a_val = st.number_input("Total Conjunto A:", min_value=0, value=50, disabled=(incognita=="Conjunto A"))
                b_val = st.number_input("Total Conjunto B:", min_value=0, value=40, disabled=(incognita=="Conjunto B"))
            with col2:
                ab_val = st.number_input("Intersección (A ∩ B):", min_value=0, value=15, disabled=(incognita=="Intersección (A ∩ B)"))
                out_val = st.number_input("Fuera de conjuntos:", min_value=0, value=25, disabled=(incognita=="Fuera de los conjuntos"))
                
            if st.button("Resolver Incógnita y Graficar"):
                st.markdown("---")
                st.subheader("📊 Presentación de Resultados")
                st.latex(r"|U| = |A| + |B| - |A \cap B| + \text{Fuera}")
                
                if incognita == "Total del Universo (U)":
                    u_res = a_val + b_val - ab_val + out_val
                    st.success(f"**Resultado:** Universo (U) = **{u_res}**")
                    u_val = u_res
                elif incognita == "Conjunto A":
                    a_res = u_val - out_val - b_val + ab_val
                    st.success(f"**Resultado:** Conjunto A = **{a_res}**")
                    a_val = a_res
                elif incognita == "Conjunto B":
                    b_res = u_val - out_val - a_val + ab_val
                    st.success(f"**Resultado:** Conjunto B = **{b_res}**")
                    b_val = b_res
                elif incognita == "Intersección (A ∩ B)":
                    ab_res = a_val + b_val - (u_val - out_val)
                    st.success(f"**Resultado:** Intersección (A ∩ B) = **{ab_res}**")
                    ab_val = ab_res
                elif incognita == "Fuera de los conjuntos":
                    out_res = u_val - (a_val + b_val - ab_val)
                    st.success(f"**Resultado:** Fuera de los conjuntos = **{out_res}**")
                    out_val = out_res

                solo_a = max(0, a_val - ab_val)
                solo_b = max(0, b_val - ab_val)
                
                fig, ax = plt.subplots(figsize=(6, 4))
                v = venn2(subsets=(solo_a, solo_b, ab_val), set_labels=('Conjunto A', 'Conjunto B'), ax=ax)
                plt.title(f"Diagrama de Venn (Universo U = {u_val}, Fuera = {out_val})")
                st.pyplot(fig)

        else:
            st.subheader("Ingresa los valores del Diagrama de 3 Conjuntos:")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                solo_a = st.number_input("Solo A:", min_value=0, value=20)
                solo_b = st.number_input("Solo B:", min_value=0, value=15)
                solo_c = st.number_input("Solo C:", min_value=0, value=10)
            with col2:
                ab_only = st.number_input("Solo (A ∩ B):", min_value=0, value=5)
                ac_only = st.number_input("Solo (A ∩ C):", min_value=0, value=4)
                bc_only = st.number_input("Solo (B ∩ C):", min_value=0, value=3)
            with col3:
                abc_all = st.number_input("Intersección Triple (A ∩ B ∩ C):", min_value=0, value=2)
                fuera_3 = st.number_input("Fuera de todos los conjuntos:", min_value=0, value=10)

            if st.button("Calcular Totales y Graficar 3 Conjuntos"):
                st.markdown("---")
                st.subheader("📊 Presentación de Resultados")
                st.latex(r"|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|")
                
                tot_a = solo_a + ab_only + ac_only + abc_all
                tot_b = solo_b + ab_only + bc_only + abc_all
                tot_c = solo_c + ac_only + bc_only + abc_all
                union_total = solo_a + solo_b + solo_c + ab_only + ac_only + bc_only + abc_all
                universo_total = union_total + fuera_3
                
                st.write(f"* **Total Conjunto A:** {tot_a}")
                st.write(f"* **Total Conjunto B:** {tot_b}")
                st.write(f"* **Total Conjunto C:** {tot_c}")
                st.success(f"**Unión Total |A ∪ B ∪ C|:** {union_total} | **Total Universo |U|:** {universo_total}")
                
                fig, ax = plt.subplots(figsize=(7, 5))
                subsets = (solo_a, solo_b, ab_only, solo_c, ac_only, bc_only, abc_all)
                v = venn3(subsets=subsets, set_labels=('Conjunto A', 'Conjunto B', 'Conjunto C'), ax=ax)
                plt.title(f"Diagrama de Venn (Universo U = {universo_total}, Fuera = {fuera_3})")
                st.pyplot(fig)
