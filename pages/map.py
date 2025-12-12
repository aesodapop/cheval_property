import streamlit as st
import streamlit.components.v1 as components

api_key = st.secrets["GOOGLE_MAPS_API_KEY"]

st.title("Stonewall, Texas")
st.write("Located between Fredricksburg and Johnson City.")

#Google Maps Embed (Stonewall, TX)
google_map_iframe = """
<iframe 
    width="100%" 
    height="600" 
    frameborder="0" style="border:0"
    src="https://www.google.com/maps/embed/v1/place?key=api_key&q=Stonewall,TX" 
    allowfullscreen>
</iframe>
"""

google_map_iframe = """
<iframe 
    width="100%" 
    height="600" 
    frameborder="0" style="border:0"
    src="https://www.google.com/maps/embed/v1/search?key=api_key&q=wineries+near+Stonewall+TX" 
    allowfullscreen>
</iframe>
"""

components.html(google_map_iframe, height=600)


st.write("Key present in secrets:", "GOOGLE_MAPS_API_KEY" in st.secrets)
st.write("Length of key:", len(st.secrets["GOOGLE_MAPS_API_KEY"]))

