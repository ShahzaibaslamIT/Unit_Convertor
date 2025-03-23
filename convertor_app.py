import streamlit as st


# Apply custom styles
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #1e1e2f, #2c3e50);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: #FFD700;
    }
    .stButton > button {
        background: linear-gradient(45deg, #ff7e5f, #feb47b);
        color: white;
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 12px rgba(255, 126, 95, 0.4);
    }
    .stButton > button:hover {
        transform: scale(1.08);
        background: linear-gradient(45deg, #ff6a00, #ee0979);
        color: white;
    }
    .result-box {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-radius: 12px;
        background: linear-gradient(45deg, #4A148C, #E1BEE7);
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
        color: white;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 14px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<h1>🌟 Advanced Unit Converter 🌟</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of Length, Weight, Temperature, and Currency")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose conversion type", ["Length", "Weight", "Temperature", "Currency"])
value = st.number_input("Enter value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles", "Yards", "Inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
elif conversion_type == "Currency":
    with col1:
        from_unit = st.selectbox("From", ["USD", "EUR", "GBP", "PKR", "INR"])
    with col2:
        to_unit = st.selectbox("To", ["USD", "EUR", "GBP", "PKR", "INR"])

# Conversion logic
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Feet': 3.281, 'Miles': 0.000621371, 'Yards': 1.09361, 'Inches': 39.37
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {'Kilograms': 1, 'Grams': 1000, 'Pounds': 2.2046, 'Ounces': 35.274}
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value 
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9/5) + 32 if to_unit == "Fahrenheit" else value

def currency_converter(value, from_unit, to_unit):
    exchange_rates = {"USD": 1, "EUR": 0.91, "GBP": 0.76, "PKR": 278.5, "INR": 83.3}
    return (value / exchange_rates[from_unit]) * exchange_rates[to_unit]

# Conversion Button
if st.button("Convert 🔄"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    elif conversion_type == "Currency":
        result = currency_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>🚀 Created By Shahzaib</div>", unsafe_allow_html=True)