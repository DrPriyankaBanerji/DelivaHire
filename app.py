import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(page_title="DelivaHire", page_icon="🚛", layout="wide")

# HEADER
st.image("https://raw.githubusercontent.com/drpriyankabanerji/delivahire/main/Delivahire%20logo.png", width=180)
st.markdown("<h1 style='margin-top: -20px;'>DelivaHire</h1>", unsafe_allow_html=True)
st.caption("Where Talent Meets the Road")

# TABS (Apply Now moved up before Contact Us)
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Apply Now", "About Us", "Partner Network", "Contact Us"])

# HOME
with tab1:
    st.subheader("Welcome to DelivaHire")
    st.write("Connecting reliable delivery agents with the fastest growing platforms in India.")

# APPLY NOW (Google Form)
with tab2:
    st.subheader("📋 Apply as a Delivery Agent")
    st.write("We’ve made it super easy to apply for delivery jobs with DelivaHire!")

    st.markdown("""
    Please click the button below to fill out our official application form.  
    Your information will be recorded securely, and our team will contact you shortly.
    """)

    if st.button("Apply via Google Form"):
        st.markdown("[**Click here to Apply Now**](https://docs.google.com/forms/d/e/1FAIpQLSdd2QvWzjihByIP3onJk1J5z3Srlz6XA05Iye5bVAfZa_B78A/viewform?usp=sharing)", unsafe_allow_html=True)

# ABOUT US (restored version)
with tab3:
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

# PARTNER NETWORK
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

# CONTACT US
with tab5:
    st.subheader("📞 Contact Us")
    st.write("Have questions? Reach out at:")
    st.markdown("**Email:** contact@delivahire.in")
    st.markdown("**Phone:** +91-9876543210")
