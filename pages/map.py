import streamlit as st
import streamlit.components.v1 as components

api_key = st.secrets["GOOGLE_MAPS_API_KEY"]

st.title("Stonewall, Texas")
st.write("Map shows wineries along Highway 290 in-between Fredricksburg and Johnson City.")

#Google Maps Embed (Stonewall, TX)
google_map_iframe = f"""
<iframe 
    width="100%" 
    height="600" 
    frameborder="0" style="border:0"
    src="https://www.google.com/maps/embed/v1/place?key={api_key}&q=Stonewall,TX" 
    allowfullscreen>
</iframe>
"""

google_map_iframe = f"""
<iframe 
    width="100%" 
    height="600" 
    frameborder="0" style="border:0"
    src="https://www.google.com/maps/embed/v1/search?key={api_key}&q=wineries+near+Stonewall+TX" 
    allowfullscreen>
</iframe>
"""

components.html(google_map_iframe, height=600)
