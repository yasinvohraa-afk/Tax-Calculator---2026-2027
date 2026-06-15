import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIG ---
SMTP_SERVER = "smtp-relay.brevo.com"
SMTP_PORT = 587
USERNAME = st.secrets["brevo_username"]
PASSWORD = st.secrets["brevo_password"]
RECEIVER_EMAIL = "your_inbox@example.com"   # Where you want to receive queries

st.set_page_config(
    page_title="FBR Pakistan Salary Tax Calculator FY 2026-27",
    page_icon="📊",
    layout="centered"
)

# --- HEADER SECTION ---
st.markdown("<h1 style='text-align:center;color:#1E3A8A;'>FBR Pakistan Salary Tax Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#4B5563;'>Based on Updated Budget 2026–27 Tax Slabs (Finance Bill 2026)</p>", unsafe_allow_html=True)

# --- CORE CALCULATOR SECTION ---
monthly_salary = st.number_input(
    "Enter Your Gross Monthly Salary (Rs.):", 
    min_value=0.0, 
    value=250000.0, 
    step=5000.0,
    help="Input your gross monthly taxable salary before deductions."
)

annual_salary = monthly_salary * 12
annual_tax = 0.0

if annual_salary <= 600000:
    annual_tax = 0.0
elif annual_salary <= 1200000:
    annual_tax = (annual_salary - 600000) * 0.01
elif annual_salary <= 2200000:
    annual_tax = 6000 + (annual_salary - 1200000) * 0.11
elif annual_salary <= 3200000:
    annual_tax = 116000 + (annual_salary - 2200000) * 0.20
elif annual_salary <= 4100000:
    annual_tax = 316000 + (annual_salary - 3200000) * 0.25
elif annual_salary <= 5600000:
    annual_tax = 541000 + (annual_salary - 4100000) * 0.29
elif annual_salary <= 7000000:
    annual_tax = 976000 + (annual_salary - 5600000) * 0.32
else:
    annual_tax = 1424000 + (annual_salary - 7000000) * 0.35

monthly_tax = annual_tax / 12
net_takehome = monthly_salary - monthly_tax
effective_rate = (annual_tax / annual_salary) * 100 if annual_salary > 0 else 0.0

col1, col2 = st.columns(2)
with col1:
    st.metric("Monthly Income Tax", f"Rs. {monthly_tax:,.0f}")
with col2:
    st.metric("Net Monthly Take-Home", f"Rs. {net_takehome:,.0f}")

col3, col4, col5 = st.columns(3)
with col3:
    st.metric("Annual Salary", f"Rs. {annual_salary:,.0f}")
with col4:
    st.metric("Annual Tax Liabilities", f"Rs. {annual_tax:,.0f}")
with col5:
    st.metric("Effective Tax Rate", f"{effective_rate:.2f}%")

st.write("---")

# --- CONSULTATION FORM (Brevo SMTP Integration) ---
st.markdown("## 📞 Need Expert Assistance? Request a Free Consultation")

with st.form("consultation_form", clear_on_submit=True):
    full_name = st.text_input("Full Name *", placeholder="Enter your full name")
    email = st.text_input("Email Address *", placeholder="name@example.com")
    phone = st.text_input("Phone / WhatsApp Number *", placeholder="e.g., 03001234567")
    service_needed = st.selectbox(
        "Service Required *",
        ["Select a service...", "NTN & Business Registration", "Income Tax Return Filing", "Corporate Compliance Outsourcing", "Other Tax Consultation"]
    )
    additional_notes = st.text_area("Briefly describe your tax situation or inquiry:", placeholder="Optional details...")
    
    submit_button = st.form_submit_button("Submit Request Now")
    
    if submit_button:
        if not full_name or not email or not phone or service_needed == "Select a service...":
            st.error("⚠️ Please fill in all required fields (*) before submitting.")
        else:
            try:
                subject = f"New Tax Consultation Request from {full_name}"
                body = f"""
                Name: {full_name}
                Email: {email}
                Phone: {phone}
                Service Needed: {service_needed}
                Notes: {additional_notes}
                """
                
                msg = MIMEMultipart()
                msg["From"] = USERNAME
                msg["To"] = RECEIVER_EMAIL
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain"))
                
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()
                server.login(USERNAME, PASSWORD)
                server.sendmail(USERNAME, RECEIVER_EMAIL, msg.as_string())
                server.quit()
                
                st.success(f"✔️ Thank you, {full_name}! Your request has been sent successfully. We will reach out to you soon.")
            except Exception as e:
                st.error(f"⚠️ Email sending failed: {e}")
