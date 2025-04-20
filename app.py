import streamlit as st
import pandas as pd
import os

# ✅ THIS MUST BE FIRST Streamlit command
st.set_page_config(page_title="DelivaHire", page_icon="🚛", layout="wide")

# Show Logo & Title
st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/delivahire_logo.png", width=180)
st.markdown("<h1 style='margin-top: -20px;'>DelivaHire</h1>", unsafe_allow_html=True)
st.caption("Where Talent Meets the Road")

# Sidebar Navigation
st.sidebar.title("DelivaHire")
menu = st.sidebar.radio("Navigate", ["Home", "About Us", "Partner Network", "Apply Now", "Contact Us"])

# ---------------- HOME ----------------
if menu == "Home":
    st.title("🚛 Welcome to DelivaHire")
    st.subheader("Where Talent Meets the Road")
    st.write("We connect skilled delivery agents with India's top delivery partners. Join us for flexible work and steady income.")

# ---------------- ABOUT US ----------------
elif menu == "About Us":
    st.header("ℹ️ About DelivaHire")
    st.write("""
    **DelivaHire** is a delivery staffing solution dedicated to empowering delivery agents and streamlining last-mile logistics.
    
    We believe in creating win-win partnerships — empowering gig workers while helping companies scale delivery operations with ease.
    
    Our team brings years of experience in logistics, operations, and talent onboarding.
    """)

# ---------------- PARTNER NETWORK ----------------
elif menu == "Partner Network":
    st.header("🤝 Our Channel Partners")
    st.write("We are proud to collaborate with the following delivery platforms:")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/swiggy.png", width=130)
        st.caption("Swiggy ✅")

        st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/zomato.png", width=130)
        st.caption("Zomato ✅")

    with col2:
        st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/blinkit.png", width=130)
        st.caption("Blinkit ✅")

        st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/bigbasket.png", width=130)
        st.caption("BigBasket ✅")

# ---------------- APPLY NOW ----------------
elif menu == "Apply Now":
    st.header("📋 Apply as a Delivery Agent")
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
            st.warning("Please fill in all required fields.")

# ---------------- CONTACT US ----------------
elif menu == "Contact Us":
    st.header("📞 Get in Touch")
    st.write("📧 Email: delivahire.team@gmail.com")
    st.write("📱 Phone: +91-9876543210")
    st.write("💬 [Chat on WhatsApp](https://wa.me/919876543210)")
    st.write("📍 Based in: New Delhi, India")
