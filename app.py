import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="FBR Pakistan Salary Tax Calculator FY 2026-27",
    page_icon="📊",
    layout="centered"
)

# --- HEADER ---
st.markdown("<h1 style='text-align:center;color:#1E3A8A;'>FBR Pakistan Salary Tax Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#4B5563;'>Based on Updated Budget 2026–27 Tax Slabs (Finance Bill 2026)</p>", unsafe_allow_html=True)

# --- TAX CALCULATOR ---
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

# --- GOOGLE FORM LINK ---
st.markdown("## 📞 Need Expert Assistance? Request a Free Consultation")

# Replace this with your actual Google Form link
google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSe-x4irjrk5xdrTLy_aYNxE_vZsGXr-9QjIHGmhdfgIp8v5pw/viewform?usp=header"

st.markdown(
    f"""
    👉 [Click here to submit your query via Google Form]({https://docs.google.com/forms/d/e/1FAIpQLSe-x4irjrk5xdrTLy_aYNxE_vZsGXr-9QjIHGmhdfgIp8v5pw/viewform?usp=header})
    
    *Your query will be securely collected in Google Sheets, and you’ll receive confirmation via email if notifications are enabled.*
    """)
