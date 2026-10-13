import streamlit as st
import math
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import pandas as pd
import numpy as np
import heapq

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
.mcd-box {
    background-color: #0d1b2a;
    border: 2px solid #f1c40f;
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    margin-bottom: 15px;
}
.mcd-title {
    color: #00e5ff;
    font-size: 0.9rem;
    font-weight: bold;
    text-transform: uppercase;
}
.mcd-value {
    color: #f1c40f;
    font-size: 2.2rem;
    font-weight: bold;
}
.method-card {
    background-color: #0a1118;
    border: 1px solid #00e5ff;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
}
.method-header {
    color: #00e5ff;
    font-weight: bold;
    font-size: 1.1rem;
    margin-bottom: 12px;
}
div.stButton > button:first-child {
    background: linear-gradient(90deg, #8B0000 0%, #C0392B 100%) !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.25rem !important;
    border-radius: 12px !important;
    border: none !important;
    width: 100% !important;
    height: 55px !important;
    box-shadow: 0 4px 12px rgba(139,0,0,0.5) !important;
    transition: all 0.3s ease !important;
}
div.stButton > button:first-child:hover {
    background: linear-gradient(90deg, #C0392B 0%, #E74C3C 100%) !important;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# Enlace directo al logo subido en tu repositorio de GitHub (logo.png)
LOGO_UMG_URL = "https://raw.githubusercontent.com/Guixxe123/Tarea-Matediscreta/main/logo.png"

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
# APLICACIÓN PRINCIPAL (MENÚ DE NAVEGACIÓN)
# ---------------------------------------------------------
else:
    st.sidebar.markdown("### 🎓 UMG Discretas")
    st.sidebar.write("**Universidad Mariano Gálvez**")

    opcion = st.sidebar.radio(
        "Selecciona el módulo:",
        ["📋 Portada / Carátula", 
         "1. Combinaciones y Permutaciones", 
         "2. Producto Cartesiano", 
         "3. Valores de Áreas (Diagrama de Venn)",
         "4. Estimación de Ruta (Matriz de Pesos)",
         "5. Cálculo de MCD y MCM"]
    )

    st.sidebar.markdown("---")
    if st.sidebar.button("⬅️ Salir al Inicio"):
        st.session_state.ingresado = False
        st.rerun()

    # ---------------------------------------------------------
    # MÓDULO: PORTADA / CARÁTULA
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # MÓDULO 1: COMBINACIONES Y PERMUTACIONES
    # ---------------------------------------------------------
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
                    res_p = math.perm(n, r)
                    res_c = math.comb(n, r)
                    fact_r = math.factorial(r)
                    st.latex(r"C(n, r) = \frac{P(n, r)}{r!}")
                    st.latex(rf"C({n}, {r}) = \frac{{{res_p}}}{{{r}!}} = \frac{{{res_p}}}{{{fact_r}}} = {res_c}")
                    st.success(f"**Resultado:** Existen **{res_c}** combinaciones posibles.")
                else:
                    res_p = math.perm(n, r)
                    fact_n = math.factorial(n)
                    fact_nr = math.factorial(n - r)
                    st.latex(r"P(n, r) = \frac{n!}{(n-r)!}")
                    st.latex(rf"P({n}, {r}) = \frac{{{n}!}}{{({n}-{r})!}} = \frac{{{fact_n}}}{{{fact_nr}}} = {res_p}")
                    st.success(f"**Resultado:** Existen **{res_p}** permutaciones posibles.")

    # ---------------------------------------------------------
    # MÓDULO 2: PRODUCTO CARTESIANO
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # MÓDULO 3: DIAGRAMAS DE VENN
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # MÓDULO 4: ESTIMACIÓN DE RUTA (MATRIZ DE PESOS)
    # ---------------------------------------------------------
    elif opcion == "4. Estimación de Ruta (Matriz de Pesos)":
        st.title("🗺️ Algoritmo de Estimación de Ruta (Grafo y Matriz)")
        st.write("Establece las relaciones y pesos de la gráfica mediante una **matriz de adyacencia** para calcular la ruta más corta o más larga.")

        tipo_estimacion = st.radio("Selecciona el tipo de estimación de ruta:", ["La más corta (Mínima)", "La más larga (Máxima)"], horizontal=True)

        num_nodos = st.slider("Cantidad de vértices (nodos):", min_value=3, max_value=25, value=6)

        # Generador dinámico de nombres de nodos (a, b, c... z, v27, v28...)
        def get_nombre_nodo(i):
            if i < 26:
                return chr(97 + i)
            return f"v{i+1}"

        nombres = [get_nombre_nodo(i) for i in range(num_nodos)]

        # Matriz por defecto de tamaño dinámico según num_nodos
        matriz_defecto = np.zeros((num_nodos, num_nodos), dtype=int)
        if num_nodos >= 6:
            ejemplo_aristas = [
                (0, 1, 2), (0, 3, 1), # a->b (2), a->d (1)
                (1, 2, 3), (1, 4, 1), # b->c (3), b->e (1)
                (3, 4, 1),           # d->e (1)
                (2, 5, 2),           # c->z (2)
                (4, 5, 2)            # e->z (2)
            ]
            for u, v, w in ejemplo_aristas:
                if u < num_nodos and v < num_nodos:
                    matriz_defecto[u][v] = w
                    matriz_defecto[v][u] = w

        df_matriz = pd.DataFrame(matriz_defecto, index=nombres, columns=nombres)

        st.subheader("📋 Matriz de Pesos / Distancias (0 representa sin conexión):")
        matriz_editada = st.data_editor(df_matriz, use_container_width=True)

        col_orig, col_dest = st.columns(2)
        with col_orig:
            vert_inicio = st.selectbox("Vértice Inicial:", nombres, index=0)
        with col_dest:
            vert_fin = st.selectbox("Vértice Final:", nombres, index=len(nombres)-1)

        if st.button("Calcula y Dibuja la Ruta"):
            st.markdown("---")
            st.subheader("📊 Presentación de Resultados")

            idx_inicio = nombres.index(vert_inicio)
            idx_fin = nombres.index(vert_fin)
            matrix_vals = matriz_editada.values

            # Algoritmo de Dijkstra para la Ruta Más Corta
            def dijkstra_corto(matrix, start, end):
                dist = {i: float('inf') for i in range(num_nodos)}
                prev = {i: None for i in range(num_nodos)}
                dist[start] = 0
                pq = [(0, start)]
                while pq:
                    d, u = heapq.heappop(pq)
                    if d > dist[u]:
                        continue
                    if u == end:
                        break
                    for v in range(num_nodos):
                        w = matrix[u][v]
                        if w > 0:
                            if dist[u] + w < dist[v]:
                                dist[v] = dist[u] + w
                                prev[v] = u
                                heapq.heappush(pq, (dist[v], v))
                if dist[end] == float('inf'):
                    return None, float('inf')
                path = []
                curr = end
                while curr is not None:
                    path.append(curr)
                    curr = prev[curr]
                path.reverse()
                return path, dist[end]

            # Búsqueda DFS para la Ruta Más Larga
            def dfs_largo(matrix, start, end):
                best_path = None
                max_w = -1
                count_evaluated = [0]

                def search(curr, target, visited, weight_acc, path_acc):
                    nonlocal best_path, max_w
                    if count_evaluated[0] > 15000: # Límite de seguridad
                        return
                    if curr == target:
                        count_evaluated[0] += 1
                        if weight_acc > max_w:
                            max_w = weight_acc
                            best_path = list(path_acc)
                        return
                    for neighbor in range(num_nodos):
                        w = matrix[curr][neighbor]
                        if w > 0 and neighbor not in visited:
                            visited.add(neighbor)
                            path_acc.append(neighbor)
                            search(neighbor, target, visited, weight_acc + w, path_acc)
                            path_acc.pop()
                            visited.remove(neighbor)

                search(start, end, {start}, 0, [start])
                return best_path, max_w

            if "corta" in tipo_estimacion.lower():
                mejor_ruta, mejor_peso = dijkstra_corto(matrix_vals, idx_inicio, idx_fin)
                titulo_res = "Ruta Más Corta"
            else:
                mejor_ruta, mejor_peso = dfs_largo(matrix_vals, idx_inicio, idx_fin)
                titulo_res = "Ruta Más Larga"

            if not mejor_ruta or mejor_peso == float('inf') or mejor_peso == -1:
                st.error(f"No existe ninguna ruta conectada entre el vértice '{vert_inicio}' y el vértice '{vert_fin}'.")
            else:
                nombres_mejor_ruta = [nombres[i] for i in mejor_ruta]
                str_ruta = " ➡️ ".join(nombres_mejor_ruta)

                st.success(f"**{titulo_res} encontrada:** {str_ruta} | **Peso Total / Distancia:** {mejor_peso}")

                # Dibujo del Grafo en 2D con Matplotlib
                fig, ax = plt.subplots(figsize=(9, 6))

                # Posiciones de los nodos
                if num_nodos == 6:
                    pos = {0: (-2, 0), 1: (-1, 1), 2: (1, 1), 3: (-1, -1), 4: (1, -1), 5: (2, 0)}
                else:
                    angles = np.linspace(0, 2*np.pi, num_nodos, endpoint=False)
                    pos = {i: (np.cos(a), np.sin(a)) for i, a in enumerate(angles)}

                aristas_mejor = set(zip(mejor_ruta[:-1], mejor_ruta[1:]))

                # Tamaño adaptativo de nodos y fuentes
                node_size = max(250, 900 - num_nodos * 22)
                font_size = max(7, 12 - num_nodos // 5)

                # Dibujar aristas
                for i in range(num_nodos):
                    for j in range(i+1, num_nodos):
                        w = matrix_vals[i][j]
                        if w > 0:
                            p1, p2 = pos[i], pos[j]
                            es_parte_mejor = (i, j) in aristas_mejor or (j, i) in aristas_mejor
                            color_linea = "#E74C3C" if es_parte_mejor else "#7F8C8D"
                            ancho_linea = 3.5 if es_parte_mejor else 1.0
                            style = "-" if es_parte_mejor else "--"

                            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color_linea, linewidth=ancho_linea, linestyle=style, zorder=1)
                            
                            # Etiqueta de peso
                            mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
                            ax.text(mx, my, str(w), fontsize=font_size, fontweight='bold', color='#F1C40F',
                                    bbox=dict(boxstyle='round,pad=0.15', facecolor='#1E1E2E', edgecolor='none'), zorder=3)

                # Dibujar nodos
                for i in range(num_nodos):
                    x, y = pos[i]
                    es_nodo_ruta = i in mejor_ruta
                    color_nodo = "#2ECC71" if es_nodo_ruta else "#3498DB"
                    ax.scatter(x, y, s=node_size, color=color_nodo, edgecolors='white', linewidth=1.5, zorder=4)
                    ax.text(x, y, nombres[i], fontsize=font_size, fontweight='bold', color='white', ha='center', va='center', zorder=5)

                ax.set_title(f"Gráfica Ponderada - {titulo_res}: {str_ruta}", fontsize=13, color='white')
                ax.axis('off')
                fig.patch.set_facecolor('#0d1b2a')
                ax.set_facecolor('#0d1b2a')
                st.pyplot(fig)

    # ---------------------------------------------------------
    # MÓDULO 5: CÁLCULO DE MCD Y MCM
    # ---------------------------------------------------------
    elif opcion == "5. Cálculo de MCD y MCM":
        st.markdown("<h2 style='text-align: center; color: #00e5ff;'>✦ PROGRAMA DE RESOLUCIÓN DE MCD Y MCM ✦</h2>", unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        with col_a:
            num_a = st.number_input("Primer número (a):", min_value=1, value=22, step=1)
        with col_b:
            num_b = st.number_input("Segundo número (b):", min_value=1, value=4, step=1)

        if st.button("⚡ CALCULAR Y PROCESAR"):
            st.markdown("---")

            # Cálculos de MCD y MCM
            mcd_val = math.gcd(num_a, num_b)
            mcm_val = (num_a * num_b) // mcd_val

            # Despliegue de tarjetas de resumen superior
            c_mcd, c_mcm = st.columns(2)
            with c_mcd:
                st.markdown(f"""
                <div class="mcd-box">
                    <div class="mcd-title">MÁXIMO COMÚN DIVISOR (MCD)</div>
                    <div class="mcd-value">{mcd_val}</div>
                </div>
                """, unsafe_allow_html=True)
            with c_mcm:
                st.markdown(f"""
                <div class="mcd-box">
                    <div class="mcd-title">MÍNIMO COMÚN MÚLTIPLO (mcm)</div>
                    <div class="mcd-value">{mcm_val}</div>
                </div>
                """, unsafe_allow_html=True)

            # Funciones auxiliares para factorización y Euclides
            def factorize(n):
                factors = []
                d = 2
                temp = n
                counts = {}
                while temp > 1:
                    while temp % d == 0:
                        factors.append((temp, d))
                        counts[d] = counts.get(d, 0) + 1
                        temp //= d
                    d += 1
                    if d * d > temp and temp > 1:
                        factors.append((temp, temp))
                        counts[temp] = counts.get(temp, 0) + 1
                        temp = 1
                factors.append((1, ""))
                return factors, counts

            facts_a, count_a = factorize(num_a)
            facts_b, count_b = factorize(num_b)

            col_met1, col_met2 = st.columns(2)

            # MÉTODO 1: DESCOMPOSICIÓN EN FACTORES PRIMOS
            with col_met1:
                st.markdown("""
                <div class="method-card">
                    <div class="method-header">🧩 MÉTODO 1: DESCOMPOSICIÓN EN FACTORES</div>
                </div>
                """, unsafe_allow_html=True)

                f_col1, f_col2 = st.columns(2)
                with f_col1:
                    st.write(f"**Factorización de {num_a}:**")
                    df_a = pd.DataFrame(facts_a, columns=["Número", "Factor"])
                    st.dataframe(df_a, hide_index=True)

                with f_col2:
                    st.write(f"**Factorización de {num_b}:**")
                    df_b = pd.DataFrame(facts_b, columns=["Número", "Factor"])
                    st.dataframe(df_b, hide_index=True)

                str_pow_a = " · ".join([f"{k}^{v}" if v > 1 else f"{k}" for k, v in count_a.items()])
                str_pow_b = " · ".join([f"{k}^{v}" if v > 1 else f"{k}" for k, v in count_b.items()])

                st.write("* **Expresión en potencias:**")
                st.write(f"* {num_a} = {str_pow_a}")
                st.write(f"* {num_b} = {str_pow_b}")
                st.info(f"**MCD:** {mcd_val} | **MCM:** {mcm_val}")

            # MÉTODO 2: ALGORITMO DE EUCLIDES
            with col_met2:
                st.markdown("""
                <div class="method-card">
                    <div class="method-header">⚡ MÉTODO 2: ALGORITMO DE EUCLIDES</div>
                </div>
                """, unsafe_allow_html=True)

                pasos_euclides = []
                x, y = max(num_a, num_b), min(num_a, num_b)
                while y != 0:
                    c = x // y
                    r = x % y
                    pasos_euclides.append({"a": x, "b": y, "c": c, "d": y, "r": r})
                    x, y = y, r

                df_euc = pd.DataFrame(pasos_euclides)
                st.dataframe(df_euc, hide_index=True, use_container_width=True)
                st.success(f"**Resultado Final:** MCD = **{mcd_val}**")

            # FÓRMULA Y RESULTADO DEL MÍNIMO COMÚN MÚLTIPLO
            st.markdown("---")
            st.markdown("<h4 style='text-align: center; color: #00e5ff;'>FÓRMULA Y RESULTADO DEL MÍNIMO COMÚN MÚLTIPLO</h4>", unsafe_allow_html=True)
            st.latex(rf"\text{{mcm}} = \frac{{{num_a} \times {num_b}}}{{\text{{MCD}}}} = \frac{{{num_a * num_b}}}{{{mcd_val}}} = {mcm_val}")
