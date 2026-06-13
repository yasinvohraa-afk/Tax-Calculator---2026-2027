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
    .main-header { font-size:28px !important; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 2px; }
    .sub-header { font-size:16px !important; text-align: center; color: #4B5563; margin-bottom: 25px; }
    .metric-box { background-color: #F3F4F6; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 2px 4px rgba(0,0,0,0.05); }
    .tax-box { background-color: #FEE2E2; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 2px 4px rgba(0,0,0,0.05); border-left: 5px solid #EF4444; }
    .takehome-box { background-color: #D1FAE5; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0px 2px 4px rgba(0,0,0,0.05); border-left: 5px solid #10B981; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>FBR Pakistan Salary Tax Calculator</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Based on the Updated Budget 2026–27 (Finance Bill 2026) Tax Slabs</div>", unsafe_allow_html=True)

# User Entry Panel
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

st.write("---")

# Display Reference Slabs Informational Expander
with st.expander("🔍 View Official FY 2026–27 Tax Slabs Reference Table"):
    st.table({
        "Annual Salary Bracket": [
            "Up to Rs. 600,000", "Rs. 600,000 to Rs. 1.2M", "Rs. 1.2M to Rs. 2.2M", 
            "Rs. 2.2M to Rs. 3.2M", "Rs. 3.2M to Rs. 4.1M", "Rs. 4.1M to Rs. 5.6M", 
            "Rs. 5.6M to Rs. 7.0M", "Above Rs. 7,000,000"
        ],
        "Tax Rate Applied": [
            "0% (Tax-Free)", "1% over 600k", "Rs. 6,000 + 11% over 1.2M", 
            "Rs. 116,000 + 20% over 2.2M", "Rs. 316,000 + 25% over 3.2M", "Rs. 541,000 + 29% over 4.1M", 
            "Rs. 976,000 + 32% over 5.6M", "Rs. 1,424,000 + 35% over 7M"
        ]
    })
