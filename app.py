import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# 1. CONFIGURE PAGE (this must be the FIRST Streamlit command)
st.set_page_config(page_title="DelivaHire", page_icon="🚛", layout="wide")

# 2. LOAD GOOGLE SHEETS CONNECTION
scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("dhcreds.json", scopes=scope)
client = gspread.authorize(creds)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1fbI5EEOYmd2hTK4y7u-tMCCYQf-fTDg7dO-h4diTRxM/edit")
worksheet = sheet.sheet1

# 3. PAGE HEADER
st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/Delivahire%20logo.png", width=180)
st.markdown("<h1 style='margin-top: -20px;'>DelivaHire</h1>", unsafe_allow_html=True)
st.caption("Where Talent Meets the Road")

# 4. TABS FOR NAVIGATION
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Apply Now", "About Us", "Partner Network", "Contact Us"])

# 5. HOME TAB
with tab1:
    st.subheader("Welcome to DelivaHire")
    st.write("Connecting reliable delivery agents with the fastest growing platforms in India.")

# 6. APPLY NOW TAB
with tab2:
    st.subheader("📋 Apply as a Delivery Agent")
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    area = st.text_input("Preferred Delivery Area")
    experience = st.selectbox("Do you have previous delivery experience?", ["Yes", "No"])

    if st.button("Submit"):
        if name and phone and area:
            worksheet.append_row([name, phone, area, experience])
            st.success(f"Thank you, {name}! Your application has been submitted.")
        else:
            st.warning("⚠️ Please fill in all required fields.")

# 7. ABOUT US TAB
with tab3:
    st.subheader("About DelivaHire")
    st.write("""
        DelivaHire is a dedicated staffing solution focused on connecting hardworking individuals with high-demand delivery platforms in India. 
        We understand the dynamic nature of gig-based logistics and aim to be the trusted bridge between talent and opportunity.
        
        From onboarding to deployment, we support our delivery agents every step of the way. Whether it’s groceries, food, or e-commerce packages—our partners trust us to provide reliable manpower, on time.
    """)

# 8. PARTNER NETWORK TAB
with tab4:
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

# 9. CONTACT US TAB
with tab5:
    st.subheader("📞 Contact Us")
    st.write("Have questions? Reach out at:")
    st.markdown("**Email:** contact@delivahire.in")
    st.markdown("**Phone:** +91-9876543210")
