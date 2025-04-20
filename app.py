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
    
    st.write("""
    **DelivaHire** is a dynamic and purpose-driven staffing agency committed to bridging the gap between skilled delivery agents and India’s fastest-growing delivery platforms. We are not just recruiters—we are enablers of opportunity, focused on unlocking livelihoods and ensuring seamless last-mile delivery services.

    Our mission is to empower individuals by offering them reliable and dignified employment while helping companies scale efficiently with trusted manpower.

    ### 🌟 What We Do:
    - Recruit and onboard delivery professionals for e-commerce, grocery, and logistics companies.
    - Train and prepare candidates for real-world field expectations.
    - Maintain a transparent and efficient hiring process that works for both the agent and the company.

    ### 🧭 Our Vision:
    To be India’s most dependable staffing partner in the delivery ecosystem, known for ethical hiring practices, operational excellence, and a commitment to social upliftment.

    Whether you're a job seeker or a delivery platform looking to expand, **DelivaHire** is here to drive your journey forward.
    """)

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
