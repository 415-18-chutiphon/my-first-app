import streamlit as st

st.title("🧾 แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%")

price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

vat = price * 0.07

net_price = price - vat

st.write("นายชุติพนธ์ กุศล เลขที่ 18 ม.4/15")

st.divider()

st.header(f"ราคาสุทธิ: {net_price:.2f} บาท")

st.header(f"จำนวนภาษี (VAT 7%): {vat:.2f} บาท")
