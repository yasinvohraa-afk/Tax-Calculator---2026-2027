import streamlit as st

# Configure the web application page
st.set_page_config(
    page_title="FBR Pakistan Salary Tax Calculator FY 2026-27",
    page_icon="📊",
    layout="centered"
)

# App Custom Styling
st.markdown("""
    <style>
    .main-header { font-size:32px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 2px; }
    .sub-header { font-size:16px !important; text-align: center; color: #4B5563; margin-bottom: 25px; }
    .section-header { font-size:22px !important; font-weight: bold; color: #1E3A8A; margin-top: 30px; margin-bottom: 15px; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; }
    .metric-box { background-color: #F3F4F6; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 2px 4px rgba(0,0,0,0.05); }
    .tax-box { background-color: #FEE2E2; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 2px 4px rgba(0,0,0,0.05); border-left: 5px solid #EF4444; }
    .takehome-box { background-color: #D1FAE5; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 2px 4px rgba(0,0,0,0.05); border-left: 5px solid #10B981; }
    .service-card { background-color: #FFFFFF; padding: 20px; border-radius: 8px; border: 1px solid #E5E7EB; box-shadow: 0px 4px 6px rgba(0,0,0,0.02); height: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<div class='main-header'>FBR Pakistan Salary Tax Calculator</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Based on Updated Budget 2026–27 Tax Slabs (Finance Bill 2026)</div>", unsafe_allow_html=True)

# --- CORE CALCULATOR SECTION ---
monthly_salary = st.number_input(
    "Enter Your Gross Monthly Salary (Rs.):", 
    min_value=0.0, 
    value=250000.0, 
    step=5000.0,
    help="Input your gross monthly taxable salary before deductions."
)

# Core Calculation Logic
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

st.write("---")

# Layout Response Cards
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<div class='tax-box'><b>Monthly Income Tax</b><br><span style='font-size:22px; font-weight:bold; color:#B91C1C;'>Rs. {monthly_tax:,.0f}</span></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='takehome-box'><b>Net Monthly Take-Home</b><br><span style='font-size:22px; font-weight:bold; color:#065F46;'>Rs. {net_takehome:,.0f}</span></div>", unsafe_allow_html=True)

st.write(" ")

col3, col4, col5 = st.columns(3)
with col3:
    st.markdown(f"<div class='metric-box'><b>Annual Salary</b><br><span style='font-weight:bold;'>Rs. {annual_salary:,.0f}</span></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='metric-box'><b>Annual Tax Liabilities</b><br><span style='font-weight:bold;'>Rs. {annual_tax:,.0f}</span></div>", unsafe_allow_html=True)
with col5:
    st.markdown(f"<div class='metric-box'><b>Effective Tax Rate</b><br><span style='font-weight:bold;'>{effective_rate:.2f}%</span></div>", unsafe_allow_html=True)


# --- MARKETING SECTORS SECTION ---
st.markdown("<div class='section-header'>💼 Our Professional Financial Services</div>", unsafe_allow_html=True)

m_col1, m_col2, m_col3 = st.columns(3)

with m_col1:
    st.markdown("""
    <div class='service-card'>
        <h4>🔒 NTN & Business Registration</h4>
        <p style='font-size: 14px; color: #4B5563;'>Avoid heavy withholding taxes! Get registered smoothly with the FBR.</p>
        <ul style='font-size: 13px; color: #4B5563; padding-left:20px;'>
            <li>Individual NTN Setup</li>
            <li>AOP / Partnership</li>
            <li>SEC Company Reg.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with m_col2:
    st.markdown("""
    <div class='service-card'>
        <h4>📈 Tax Return Filing</h4>
        <p style='font-size: 14px; color: #4B5563;'>Secure your Active Taxpayer List (ATL) status and unlock strategic wealth justifications.</p>
        <ul style='font-size: 13px; color: #4B5563; padding-left:20px;'>
            <li>Salaried & Business Returns</li>
            <li>Wealth Statements</li>
            <li>Foreign Income Reporting</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with m_col3:
    st.markdown("""
    <div class='service-card'>
        <h4>🛡️ Corporate Compliance</h4>
        <p style='font-size: 14px; color: #4B5563;'>Protect your business entity from heavy penalties, FBR legal notices, and audits.</p>
        <ul style='font-size: 13px; color: #4B5563; padding-left:20px;'>
            <li>Monthly Sales Tax</li>
            <li>Withholding Statements</li>
            <li>SEC Compliance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.write(" ")

# --- CALL TO ACTION LEAD CAPTURE FORM ---
st.markdown("<div class='section-header'>📞 Need Expert Assistance? Request a Free Consultation</div>", unsafe_allow_html=True)

with st.form("consultation_form", clear_on_submit=True):
    c_col1, c_col2 = st.columns(2)
    with c_col1:
        full_name = st.text_input("Full Name *", placeholder="Enter your full name")
        email = st.text_input("Email Address *", placeholder="name@example.com")
    with c_col2:
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
            # Displays success note directly to user on screen
            st.success(f"✔️ Thank you, {full_name}! Your request for '{service_needed}' has been recorded. Our corporate tax consultant will reach out to you on {phone} within 24 hours.")
