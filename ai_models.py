from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Função para configurar o modelo da Langchain com a chave da API
def configure_model(api_key, model_choice):
    if model_choice == "GPT (OpenAI)":
        # Utilizando ChatOpenAI para modelos de chat
        return ChatOpenAI(model="gpt-4o-mini", temperature=0.4, openai_api_key=api_key)
    elif model_choice == "Gemini (Google)":
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.4, google_api_key=api_key)
    else:
        raise ValueError("Modelo inválido. Escolha GPT (OpenAI) ou Gemini (Google).")

# Template de prompt para revisão
review_template = """
Você receberá páginas de um livro contendo texto parcial ou completo. Sua tarefa é revisar exclusivamente a **gramática**, **ortografia** e **semântica** do texto, garantindo a coesão e correção do conteúdo. 

**Não altere**:
1. Nomes próprios
2. O estilo ou tom do autor
3. O sentido original do texto
4. Palavras ou frases sem necessidade clara

Faça apenas correções pontuais, usando **somente** as marcações HTML `<mark>` para destacar as correções feitas. **Evite reescrever frases inteiras, exceto em casos de necessidade para correção gramatical ou de sentido**.

Para marcações de correção:
- Destaque erros gramaticais, ortográficos e de coesão entre as tags `<mark>`.
- Não substitua palavras ou reescreva frases sem razão evidente e necessária.
- Se o texto iniciar com um número de página, remova-o por ser irrelevante.
- Dê sugestões e revisões ao fim de cada página, separando por duas quebras de linha.

Específicos:
- Não corrija interrupções de frases no final da página; preserve a integridade do texto.
- Quebras de linha ou espaços duplos não precisam de correção.

**Exemplo de revisão**:

Texto original:  
"26 Ela foçou o vestido e comessou a caminhas lentamente."  
Texto revisado (correção em HTML):  
"Ela <mark>fechou</mark> o vestido e <mark>começou</mark> a <mark>caminhar</mark> lentamente.

<mark>Sugestão:</mark> Melhore tal e tal coisa; a frase '...' não ficou clara."

Agora revise o seguinte trecho:

{page_text}

Texto revisado:
"""


# Criando o PromptTemplate
review_prompt = PromptTemplate(
    input_variables=["page_text"],
    template=review_template
)

# Função para revisar páginas usando LangChain
def review_pages(model, text_list, model_choice):
    revised_text_list = []
    
    # Criando a cadeia LLM
    chain = LLMChain(llm=model, prompt=review_prompt)
    
    for page_text in text_list:
        response = chain.run(page_text=page_text)
        revised_text_list.append(response)

    return revised_text_list
