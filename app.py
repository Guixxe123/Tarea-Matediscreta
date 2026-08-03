import streamlit as st
import math
import itertools
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

# Configuración general de página
st.set_page_config(page_title="Matemáticas Discretas - App", layout="wide")

# =========================================================
# PANTALLA 1: SELECCIÓN DE OPCIÓN (MENÚ LATERAL)
# =========================================================
st.sidebar.title("🧮 Matemáticas Discretas")
opcion_menu = st.sidebar.radio(
    "Selecciona el módulo:",
    [
        "1. Combinaciones y Permutaciones",
        "2. Producto Cartesiano",
        "3. Valores de Áreas (Diagrama de Venn)"
    ]
)

# =========================================================
# PANTALLA 2 & 5: COMBINACIONES Y PERMUTACIONES
# =========================================================
if opcion_menu == "1. Combinaciones y Permutaciones":
    st.title("🔢 Combinaciones y Permutaciones")
    
    col1, col2 = st.columns(2)
    with col1:
        tipo_op = st.selectbox("Selecciona el tipo de operación:", ["Combinación (C)", "Permutación (P)"])
    with col2:
        n = st.number_input("Ingresa el valor de n (Total de elementos):", min_value=0, value=5, step=1)
        r = st.number_input("Ingresa el valor de r (Elementos seleccionados):", min_value=0, value=3, step=1)

    if st.button("Calcular Operación", type="primary"):
        st.divider()
        # --- PANTALLA 5: PRESENTACIÓN DE RESULTADOS ---
        st.subheader("📊 Pantalla 5: Presentación de Resultados")
        
        if r > n:
            st.error("⚠️ Error: El valor de 'r' no puede ser mayor que 'n'.")
        else:
            if "Combinación" in tipo_op:
                res = math.comb(n, r)
                st.latex(f"C({n}, {r}) = \\binom{{{n}}}{{{r}}} = \\frac{{{n}!}}{{{r}!({n}-{r})!}} = {res}")
                st.success(f"**Resultado:** Existen **{res}** combinaciones posibles (el orden no importa).")
            else:
                res = math.perm(n, r)
                st.latex(f"P({n}, {r}) = \\frac{{{n}!}}{{({n}-{r})!}} = {res}")
                st.success(f"**Resultado:** Existen **{res}** permutaciones posibles (el orden importa).")

# =========================================================
# PANTALLA 3 & 5: PRODUCTO CARTESIANO
# =========================================================
elif opcion_menu == "2. Producto Cartesiano":
    st.title("✖️ Producto Cartesiano")
    
    cant_conjuntos = st.number_input("Cantidad de conjuntos a relacionar:", min_value=2, max_value=5, value=2)
    
    conjuntos = []
    nombres_conjuntos = [chr(65 + i) for i in range(cant_conjuntos)] # A, B, C...
    
    st.write("### Ingresa los elementos de cada conjunto (separados por coma):")
    for nombre in nombres_conjuntos:
        elem_str = st.text_input(f"Conjunto {nombre}:", value="1, 2" if nombre == "A" else "x, y")
        # Limpiamos espacios en blanco
        elementos = [e.strip() for e in elem_str.split(",") if e.strip() != ""]
        conjuntos.append(elementos)
    
    # Orden del producto cartesiano
    orden_op = st.multiselect(
        "Especifica el orden del producto cartesiano:",
        options=nombres_conjuntos,
        default=nombres_conjuntos
    )

    if st.button("Generar Producto Cartesiano", type="primary"):
        st.divider()
        # --- PANTALLA 5: PRESENTACIÓN DE RESULTADOS ---
        st.subheader("📊 Pantalla 5: Presentación de Resultados")
        
        if not orden_op:
            st.warning("Por favor selecciona al menos dos conjuntos para operar.")
        else:
            # Filtramos los conjuntos en el orden seleccionado
            indices = [nombres_conjuntos.index(c) for c in orden_op]
            conjuntos_a_operar = [conjuntos[i] for i in indices]
            
            # Cálculo del producto cartesiano
            producto = list(itertools.product(*conjuntos_a_operar))
            
            str_orden = " × ".join(orden_op)
            st.write(f"**Operación solicitada:** ${str_orden}$")
            st.write(f"**Total de pares/tuplas generadas:** `{len(producto)}`")
            
            # Formato en notación de conjuntos
            notacion = "{" + ", ".join([str(tupla) for tupla in producto]) + "}"
            st.code(f"{str_orden} = {notacion}", language="text")
            
            # Vista tabular
            st.write("#### Vista detallada de las relaciones:")
            st.table([{"#": idx+1, "Relación": str(item)} for idx, item in enumerate(producto)])

# =========================================================
# PANTALLA 4 & 5: VALORES DE ÁREAS (DIAGRAMA DE VENN)
# =========================================================
elif opcion_menu == "3. Valores de Áreas (Diagrama de Venn)":
    st.title("⚪ Valores de Áreas de Diagrama de Venn")
    
    cant_v = st.radio("¿Cuántos conjuntos deseas relacionar?", [2, 3], horizontal=True)
    
    st.markdown("### Selecciona cuál será el área de incógnita (solo 1 incógnita):")
    
    if cant_v == 2:
        incognita = st.selectbox(
            "Variable incógnita (?):",
            [
                "Total del Universo (U)",
                "Total del Conjunto A",
                "Total del Conjunto B",
                "Intersección entre todos (A ∩ B)",
                "Fuera de los conjuntos"
            ]
        )
        
        col1, col2 = st.columns(2)
        with col1:
            val_U = st.number_input("Cantidad Total (U):", value=100, disabled=(incognita == "Total del Universo (U)"))
            val_A = st.number_input("Cantidad Total del Conjunto A:", value=50, disabled=(incognita == "Total del Conjunto A"))
            val_B = st.number_input("Cantidad Total del Conjunto B:", value=40, disabled=(incognita == "Total del Conjunto B"))
        with col2:
            val_inter = st.number_input("Cantidad repetida entre todos (A ∩ B):", value=15, disabled=(incognita == "Intersección entre todos (A ∩ B)"))
            val_fuera = st.number_input("Cantidad fuera de los conjuntos:", value=25, disabled=(incognita == "Fuera de los conjuntos"))

        if st.button("Resolver Incógnita y Graficar", type="primary"):
            st.divider()
            # --- PANTALLA 5: PRESENTACIÓN DE RESULTADOS ---
            st.subheader("📊 Pantalla 5: Presentación de Resultados")
            
            # Despeje de la fórmula: U = A + B - inter + fuera
            if incognita == "Total del Universo (U)":
                val_U = val_A + val_B - val_inter + val_fuera
            elif incognita == "Total del Conjunto A":
                val_A = val_U - val_B + val_inter - val_fuera
            elif incognita == "Total del Conjunto B":
                val_B = val_U - val_A + val_inter - val_fuera
            elif incognita == "Intersección entre todos (A ∩ B)":
                val_inter = val_A + val_B + val_fuera - val_U
            elif incognita == "Fuera de los conjuntos":
                val_fuera = val_U - (val_A + val_B - val_inter)

            # Cálculo de áreas individuales exclusivas para el gráfico
            solo_A = val_A - val_inter
            solo_B = val_B - val_inter
            union_AB = solo_A + solo_B + val_inter
            
            col_res1, col_res2 = st.columns([1, 1])
            with col_res1:
                st.success(f"**Valor calculado para '{incognita}':**")
                st.write(f"### 🎯 Resultado: `{val_U if 'Universo' in incognita else val_A if 'Conjunto A' in incognita else val_B if 'Conjunto B' in incognita else val_inter if 'Intersección' in incognita else val_fuera}`")
                
                st.markdown("#### Desglose por región:")
                st.write(f"- **Solo Conjunto A:** {solo_A}")
                st.write(f"- **Solo Conjunto B:** {solo_B}")
                st.write(f"- **Intersección (A ∩ B):** {val_inter}")
                st.write(f"- **Total Unión (A ∪ B):** {union_AB}")
                st.write(f"- **Fuera de todos:** {val_fuera}")
                st.write(f"- **Total Universo:** {val_U}")

            with col_res2:
                # Dibujar diagrama de Venn
                fig, ax = plt.subplots(figsize=(5, 5))
                venn_diagram = venn2(
                    subsets=(solo_A, solo_B, val_inter),
                    set_labels=('Conjunto A', 'Conjunto B'),
                    ax=ax
                )
                plt.title(f"Diagrama de Venn 2 Conjuntos\n(Fuera de los conjuntos = {val_fuera})")
                st.pyplot(fig)

    else:
        st.info("💡 Para 3 conjuntos, el principio de inclusión-exclusión añade las intersecciones en pares (A∩B, A∩C, B∩C) y suma la intersección triple (A∩B∩C).")
        st.write("Puedes ampliar este bloque usando la función `venn3()` incluida en el código.")