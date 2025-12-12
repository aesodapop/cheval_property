import streamlit as st
import streamlit.components.v1 as components

st.title("Stonewall, Texas")
st.write("Located between Fredricksburg and Johnson City.")

#Google Maps Embed (Stonewall, TX)
google_map_iframe = """
<iframe 
    width="100%" 
    height="600" 
    frameborder="0" style="border:0"
    src="https://www.google.com/maps/embed/v1/place?key=GOOGLE_MAPS_API_KEY&q=Stonewall,TX" 
    allowfullscreen>
</iframe>
"""

google_map_iframe = """
<iframe 
    width="100%" 
    height="600" 
    frameborder="0" style="border:0"
    src="https://www.google.com/maps/embed/v1/search?key=GOOGLE_MAPS_API_KEY&q=wineries+near+Stonewall+TX" 
    allowfullscreen>
</iframe>
"""

src="https://www.google.com/maps/embed/v1/search?key=GOOGLE_MAPS_API_KEY&q=distilleries+near+Stonewall+TX"

components.html(google_map_iframe, height=600)
