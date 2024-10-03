# IA Revisora de Livros com LangChain e GPT

Este projeto cria uma ferramenta de revisão de livros em formato PDF usando Streamlit e LangChain com a API GPT. Ele processa PDFs e gera resumos, insights e correções.

## Funcionalidades
- Upload de arquivos PDF
- Processamento automático com GPT via LangChain
- Interface simples com Streamlit
- Resultados em tempo real

## Requisitos

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com)
- API GPT da OpenAI

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv langchain_env
   source langchain_env/bin/activate  # Para Windows, use `.\langchain_env\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode o aplicativo:
   ```bash
   streamlit run app.py
   ```

## Como Usar
1. Suba um arquivo PDF para análise.
2. A ferramenta processará o arquivo e apresentará um resumo e insights baseados no GPT.

## Contribuição
Sinta-se à vontade para enviar pull requests ou abrir issues para melhorias.

## Licença
Este projeto está licenciado sob a [MIT License](./LICENSE).
```

### 3. **`LICENSE` (MIT License)**  
A licença MIT é uma das mais comuns e permite que outros usem seu código, com poucas restrições. Aqui está um modelo:

```markdown
MIT License

Copyright (c) 2024 Alexandre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
