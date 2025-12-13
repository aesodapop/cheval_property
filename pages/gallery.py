import streamlit as st
import os

st.info("📱 On mobile: tap >> in top-left to navigate pages.")

st.title("Cheval Hill Country Hideaway")


# col1, col2, col3 = st.columns(3)
# with col1:
#     if st.button("About"):
#         st.switch_page("about.py")
# with col2:
#     if st.button("Gallery"):
#         st.switch_page("pages/gallery.py")
# with col3:
#     if st.button("Map"):
#         st.switch_page("pages/map.py")


# Directory containing your images
IMAGE_DIR = "images"  # Folder containing your images

custom_images = [
    {"file": "01_Entryway.jpg",        "name": "Entryway"},
    {"file": "02_Living Room.jpg",  "name": "Living Room"},
    {"file": "03_Living Room.jpg",      "name": "Living Room"},    
    {"file": "04_Kitchen.jpg",     "name": "Kitchen"},
    {"file": "5_Kitchen.jpg",     "name": "Kitchen"},
    {"file": "5.5_Master.jpg",     "name": "Bedroom 1"},
    {"file": "06_Master.jpg",     "name": "Bedroom 1"},
    {"file": "07_Master Bath.jpg",     "name": "Bathroom 1"},
    {"file": "08_Guest Room.jpg",     "name": "Bedroom 2"},
    {"file": "10_Guest 2.jpg",     "name": "Bedroom "},
    {"file": "09_Guest Bath.jpg",     "name": "Bathroom 2"},
    {"file": "11_Exterior.jpg",     "name": "Exterior"},
    {"file": "12_View.jpg",     "name": "View from Porch"},
    {"file": "13_Exterior.jpg",     "name": "Exterior"},
    {"file": "111_Wine.jpg",     "name": ""}
    ]

# ---------------------------------------------------------
# Load and validate images
# ---------------------------------------------------------
if not os.path.exists(IMAGE_DIR):
    st.error(f"Image directory '{IMAGE_DIR}' not found. Please create it and add images.")
else:

    available_files = [
        f for f in os.listdir(IMAGE_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    ]

    # Filter only the custom images that exist
    valid_images = [img for img in custom_images if img["file"] in available_files]

    # Warn if missing files
    missing = [img["file"] for img in custom_images if img["file"] not in available_files]
    if missing:
        st.warning(f"These images were not found: {missing}")

    if not valid_images:
        st.warning("No valid images found in the directory.")
    else:
        cols = st.columns(2)
        for idx, img in enumerate(valid_images):
            img_path = os.path.join(IMAGE_DIR, img["file"])
            with cols[idx % 2]:
                st.image(img_path, caption=img["name"])
