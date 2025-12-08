import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="Cheval Hill Country Hideaway",
    layout="wide"
)

# --- HEADER ---
st.title("Cheval Hill Country Hideaway")
st.subheader("In the Heart of Wine Country – Stonewall, Texas")
st.markdown("---")

# --- ABOUT SECTION ---
st.markdown("## Welcome to Your Hill Country Getaway")

st.write("""
Escape to our charming **3-bedroom, 2-bath retreat** nestled in the rolling hills of
Stonewall—right in the center of Texas Wine Country. Whether you’re planning a
weekend getaway or a relaxed country escape, this cozy home offers comfort, serenity,
and unbeatable access to the area’s best attractions.

Just minutes from award-winning **wineries, distilleries, and tasting rooms**, you’ll
have your choice of memorable Hill Country experiences. Spend the day exploring local
vineyards, sipping spirits, or strolling the historic towns of **Fredericksburg** and
**Johnson City**.

After a day out, unwind on the large **front porch**, complete with classic rocking
chairs—perfect for sunsets and slow mornings.
""")

st.markdown("---")

# --- INSIDE THE HOME ---
st.markdown("## Inside the Home")

st.write("""
- Three comfortable bedrooms ideal for families or small groups  
- Two full bathrooms stocked with essentials  
- A welcoming living space and fully equipped kitchen  

Whether you're here for wine tours, a peaceful retreat, or to explore the natural
beauty of the Hill Country, our Stonewall home is the perfect base for your adventure.

**No pets and no smokers please.**
""")

st.markdown("---")

# --- SLEEPING ARRANGEMENTS ---
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("## Sleeping Arrangements")
    st.write("""
    - **Bedroom 1:** King Bed  
    - **Bedroom 2:** Queen Bed  
    - **Bedroom 3:** Queen Bed  
    """)

with col2:
    st.markdown("## Bathroom Details")
    st.write("""
    - **Bathroom 1:** Shower and soaking tub (fits 2)  
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
