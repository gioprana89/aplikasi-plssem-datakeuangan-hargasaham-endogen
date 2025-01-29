import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px



st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)






st.write('''<br><br><br><center><font color = "#0000ff" size = 5>KUMPULAN ARTIKEL (JURNAL & PROSIDING): APLIKASI PARTIAL LEAST SQUARES STRUCTURAL EQUATION MODELING (PLS-SEM)<br> DENGAN VARIABEL HARGA SAHAM SEBAGAI VARIABEL ENDOGEN<br><font color = 'red'>Artikel Terkumpul Sebanyak 10 Artikel</font></font></center>



             ''', unsafe_allow_html = True)


col1, col2, col3, col4, col5 = st.columns([3,3,3,3,3])

with col1:
    st.write("") 

with col2:
    st.write("") 

with col3:
    st.image("ugi3.jpg", width = 300)

with col4:
    st.write("")

with col5:
    st.write("")




st.markdown(
    """<center><a href="https://galeri-web-app-python-2025.streamlit.app/" target = "_blank">Galeri Aplikasi Python-Streamlit</a> | <a href="https://statkomat.com/download_tulisan.php" target = "_blank">STATKOMAT</a> | <a href="https://www.youtube.com/@STATKOMAT" target = "_blank">Youtube</a> | <a href="https://share-your-shiny-app.id/" target = "_blank">Shiny</a></center>""",
    unsafe_allow_html=True)






dataku = pd.read_excel("data excel.xlsx")



dataku = pd.DataFrame(dataku)


st.write('''<br><br>



             ''', unsafe_allow_html = True)







col11, col21, col31 = st.columns([4,4,4])

with col11:
    pilih_tahun = st.multiselect(
"Pilih Tahun",
[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
max_selections = 10,
default = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
)

with col21:
    pilih_jurnal_prosiding = st.multiselect(
"Pilih Jurnal/Prosiding",
["Jurnal", "Prosiding"],
max_selections = 2,
default = ["Jurnal","Prosiding"],
)

with col31:
    st.write("") 










pilih_data1 = dataku[dataku['Tahun Artikel'].isin(pilih_tahun)]

pilih_data2 = dataku[pilih_data1['Jurnal/Prosiding'].isin(pilih_jurnal_prosiding)]




dataku = pilih_data2


st.data_editor(
    dataku,
    column_config={

        "Link Artikel": st.column_config.LinkColumn(
            "Link Artikel", display_text="Alamat Website"
        ),

        "Sinta": st.column_config.LinkColumn(
            "Sinta", display_text="Alamat Website"
        ),


            "Link Gambar Kerangka": st.column_config.LinkColumn(
            "Link Gambar Kerangka", display_text="Alamat Website"
        ),

    },
    hide_index=True,
)


