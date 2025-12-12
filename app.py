import streamlit as st

about = st.Page("pages/about.py", title="About", icon=":material/info:", default=True)
gallery = st.Page("pages/gallery.py", title="Gallery", icon=":material/photo:")
map = st.Page("pages/map.py", title="Map", icon=":material/map:")

pg = st.navigation({"Cheval": [about, gallery]})

pg.run()
