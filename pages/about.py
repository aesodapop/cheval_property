import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="Cheval Hill Country Hideaway",
    layout="wide"
)

# --- HEADER ---
st.title("Cheval Hill Country Hideaway")
st.subheader("In the Heart of Wine Country – Stonewall, Texas")
#st.markdown("---")

# --- ABOUT SECTION ---

st.write("""
Experience the perfect Hill Country escape at our cozy 3-bedroom, 2-bath hideaway located right in the 
center of Texas Wine Country. 
Relax on the spacious front porch, explore local wineries and distilleries, or wander the historic 
streets of Fredericksburg and Johnson City—all just minutes away.
""")

st.markdown("---")

# --- INSIDE THE HOME ---
st.markdown("## Inside the Home")

st.write("""
Three comfortable bedrooms ideal for families or small groups  
- **Bedroom 1:** King Bed  
    - **Bedroom 2:** Queen Bed  
    - **Bedroom 3:** Queen Bed  
- Two full bathrooms stocked with essentials  
    - **Bathroom 1:** Shower + soaking tub (fits 2)  
    - **Bathroom 2:** Shower/tub combo  
- A welcoming living space
    - Wifi
    - Smart TV
- A fully equipped kitchen  
    - Stove  
    - Refrigerator  
    - Keurig (coffee pods provided)  
    - Microwave  
    - Cooking essentials  

**No pets or smoking please.**

""")

st.markdown("---")

# --- SLEEPING ARRANGEMENTS & BATHROOMS ---
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("## Sleeping Arrangements")
    st.markdown("""
- **Bedroom 1:** King Bed  
- **Bedroom 2:** Queen Bed  
- **Bedroom 3:** Queen Bed  
""")

with col2:
    st.markdown("## Bathroom Details")
    st.markdown("""
- **Bathroom 1:** Shower + soaking tub (fits 2)  
- **Bathroom 2:** Shower/tub combo  
""")

st.markdown("---")


# --- KITCHEN AMENITIES ---
st.markdown("## Kitchen Amenities")

st.write("""
- Stove  
- Refrigerator  
- Keurig (coffee pods provided)  
- Microwave  
- Cooking essentials  
""")

st.markdown("---")

# --- GUEST ACCESS ---
st.markdown("## Guest Access")

st.write("""
On the **day of check-in**, you will receive an **Access Code Email at 4:00 PM**, which includes:

- Property address  
- Door code and entry instructions  
- **24-hour on-call phone number** for assistance during your stay  
""")

st.markdown("---")
