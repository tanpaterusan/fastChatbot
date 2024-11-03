# fastChatbot

Chatbot AI untuk Meningkatkan Pelayanan Contact Center HAI-DJPb di Direktorat Jenderal Perbendaharaan Kementerian Keuangan.

## Project Demo

belum tersedia.

## Project Description

Bismillah.
Ini adalah project pembuatan chatbot sederhana untuk meningkatkan Pelayanan Contact Center HAI-DJPb. Dibuat menggunakan Python 3, Open AI, Langchain, dan Streamlit dengan sumber data dari dataset tiket HAI SAKTI Modul Pelaporan selama Tahun 2023-2024. Saat ini chatbot belum bisa didemokan karena masih error di library python dan limitasi API_keys dari openai.

## Features

- Data sumber ditaruh di folder content, format harus csv. Ke depan aplikasi dapat disambungkan dengan database untuk sumber yang lebih besar.
- Chatbot bisa menjawab pertanyaan yang relevan dengan data sumber tersebut.

## Additional Information:

1. Jika view file .csv pada vscode masih tercampur dengan tags html, agar dibersihkan dahulu menggunakan script remove_html.py
2. Jika nanti error library sudah solve, silakan menjalankan script dengan menginputkan api_key sendiri dari openai.

## Technologies Used

- Open AI
- Langchain
- Streamlit
- Python

## Daftar Pustaka

Project ini menyadur referensi source-code dari github berikut (dengan modifikasi):

1. https://github.com/asad-ullah-khan1/CSVChatBot;
2. https://github.com/manghat/python-remove-html-from-csv.
