import streamlit as st
import pandas as pd
import os

# Set page config (MUST be first)
st.set_page_config(page_title="DelivaHire", page_icon="🚛", layout="wide")

# Display logo and title
st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/Delivahire%20logo.png", width=180)
st.markdown("<h1 style='margin-top: -20px;'>DelivaHire</h1>", unsafe_allow_html=True)
st.caption("Where Talent Meets the Road")

# Top tabs
tabs = st.tabs(["Home", "Apply Now", "About Us", "Partner Network", "Contact Us"])

# --- Home ---
with tabs[0]:
    st.subheader("Welcome to DelivaHire")
    st.write("Connecting reliable delivery agents with the fastest growing platforms in India.")

# --- Apply Now ---
with tabs[1]:
    st.subheader("📋 Apply as a Delivery Agent")

    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    area = st.text_input("Preferred Delivery Area")
    experience = st.selectbox("Do you have previous delivery experience?", ["Yes", "No"])

    csv_file = "applications.csv"

    if st.button("Submit"):
        if name and phone and area:
            new_entry = pd.DataFrame({
                "Name": [name],
                "Phone": [phone],
                "Area": [area],
                "Experience": [experience]
            })

            if os.path.exists(csv_file):
                existing_data = pd.read_csv(csv_file)
                updated_data = pd.concat([existing_data, new_entry], ignore_index=True)
            else:
                updated_data = new_entry

            updated_data.to_csv(csv_file, index=False)
            st.success(f"Thank you, {name}! Your application has been submitted.")
        else:
            st.warning("⚠️ Please fill in all required fields.")

# --- About Us ---
with tabs[2]:
    st.subheader("About DelivaHire")
    st.write("We are a growing staffing agency specializing in recruiting delivery agents for India’s top logistics and grocery platforms.")

# --- Partner Network ---
with tabs[3]:
    st.header("🤝 Our Channel Partners")
    st.write("We are proud to collaborate with the following delivery platforms:")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/Swiggy.png", width=130)
        st.caption("Swiggy ✅")

        st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/Zomato.png", width=130)
        st.caption("Zomato ✅")

    with col2:
        st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/Blinkit.png", width=130)
        st.caption("Blinkit ✅")

        st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/Big%20basket.png", width=130)
        st.caption("BigBasket ✅")

# --- Contact Us ---
with tabs[4]:
    st.subheader("📞 Contact Us")
    st.write("Have questions? Reach out at:")
    st.markdown("**Email:** contact@delivahire.in")
    st.markdown("**Phone:** +91-9876543210")
