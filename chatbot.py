import streamlit as st

# Daftar buku di perpustakaan
buku_list = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata"},
    {"judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer"},
    {"judul": "Negeri 5 Menara", "penulis": "A. Fuadi"},
    {"judul": "Dilan 1990", "penulis": "Pidi Baiq"},
    {"judul": "Ayat-Ayat Cinta", "penulis": "Habiburrahman El Shirazy"},
]

st.title("Chatbot Perpustakaan Sederhana")

st.write("Selamat datang di chatbot perpustakaan! Silakan ketik pertanyaan Anda.")

user_input = st.text_input("Anda:", "")

def chatbot_response(text):
    text = text.lower()
    if "daftar buku" in text or "list buku" in text:
        response = "Berikut daftar buku di perpustakaan:\n"
        for idx, buku in enumerate(buku_list, 1):
            response += f"{idx}. {buku['judul']} oleh {buku['penulis']}\n"
        return response
    elif "siapa penulis" in text:
        for buku in buku_list:
            if buku["judul"].lower() in text:
                return f"Penulis '{buku['judul']}' adalah {buku['penulis']}."
        return "Maaf, saya tidak menemukan buku tersebut."
    elif "halo" in text or "hai" in text:
        return "Halo! Ada yang bisa saya bantu?"
    else:
        return "Maaf, saya hanya bisa membantu tentang daftar buku dan penulisnya."

if user_input:
    st.write("Chatbot:", chatbot_response(user_input))