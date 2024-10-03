import streamlit as st
from book_process import extract_text_from_pdf, save_as_word
from ai_models import configure_model, review_pages

# Interface com Streamlit
def main():
    st.title("Revisor de Livro com IA")

    # Upload do arquivo PDF
    pdf_file = st.file_uploader("Faça upload do arquivo PDF", type=["pdf"])
    
    # Escolha do modelo de IA
    model_choice = st.selectbox("Escolha o modelo de IA", ["GPT (OpenAI)"])#, "Gemini (Google)"])
    
    # Entrada da chave API
    api_key = st.text_input(f"Insira sua chave da API para {model_choice}", type="password")

    # Seleção das páginas a serem revisadas
    start_page = st.number_input("Página inicial", min_value=1, step=1)
    end_page = st.number_input("Página final", min_value=start_page, step=1)

    if st.button("Iniciar revisão"):
        if not pdf_file or not api_key:
            st.error("Por favor, faça upload do PDF e insira a chave API.")
        else:
            model = configure_model(api_key, model_choice)
            text_list = extract_text_from_pdf(pdf_file, start_page, end_page)

            st.write("Revisando as páginas...")
            revised_text_list = review_pages(model, text_list, model_choice)

            # Salvar como Markdown
            word_file_path  = save_as_word(revised_text_list, start_page)
            st.success("Revisão concluída!")
            st.download_button("Baixar revisão em Word", data=open(word_file_path, "rb"),
                               file_name=f"revisão_{pdf_file.file_id}.docx", 
                               mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

if __name__ == "__main__":
    main()
