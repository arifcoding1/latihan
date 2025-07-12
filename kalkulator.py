import streamlit as st

st.title("Kalkulator Sederhana")

num1 = st.number_input("Masukkan angka pertama", value=0.0)
num2 = st.number_input("Masukkan angka kedua", value=0.0)
operation = st.selectbox("Pilih operasi", ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"])

if st.button("Hitung"):
    if operation == "Tambah (+)":
        result = num1 + num2
    elif operation == "Kurang (-)":
        result = num1 - num2
    elif operation == "Kali (×)":
        result = num1 * num2
    elif operation == "Bagi (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Pembagi tidak boleh nol"
    st.success(f"Hasil: {result}")