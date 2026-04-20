import streamlit as st
from gerador_de_dados.services.pipeline import run_pipeline

st.title("Gerador de Dados Financeiros")

qtd_linhas = st.number_input("Quantidade de registros:", min_value=1, max_value=50000, value=100)

if st.button("Gerar Dados"):
    csv_data = run_pipeline(qtd_linhas)

    st.session_state['csv_result'] = csv_data
    st.success(f"{qtd_linhas} registros gerados com sucesso!")

if 'csv_result' in st.session_state:
    st.download_button(
        label="Baixar arquivo CSV",
        data=st.session_state['csv_result'],
        file_name="dados_financeiros.csv",
        mime="text/csv"
    )