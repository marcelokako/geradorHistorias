import streamlit as st
import google.generativeai as genai

# Configura a API key do Gemini corretamente para a versão instalada
api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

def gerar_resposta_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

if "historia" not in st.session_state:
    st.session_state.historia = ""
if "finalizada" not in st.session_state:
    st.session_state.finalizada = False
if "prompt_base" not in st.session_state:
    st.session_state.prompt_base = ""

st.title("Gerador de História")

nome_protagonista = st.text_input("Nome do Protagonista")

genero = st.selectbox(
    "Escolha o Gênero Literário",
    ["Fantasia", "Ficção Científica", "Mistério", "Aventura"]
)

local_inicial = st.radio(
    "Selecione o Local Inicial",
    ["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado", "Uma nave espacial à deriva"]
)

frase_desafio = st.text_area("Frase de Efeito ou Desafio Inicial")

if st.button("Gerar História"):
    if nome_protagonista and frase_desafio and local_inicial and genero:
        prompt = (
            f"Crie o início de uma história de '{genero}' com o protagonista chamado '{nome_protagonista}'. "
            f"A história começa em '{local_inicial}'. Considere a frase ou desafio no início: '{frase_desafio}'. "
            f"A história deve ter um ou dois parágrafos no estilo envolvente e narrativo."
        )
        with st.spinner("Gerando história..."):
            resposta = gerar_resposta_gemini(prompt)
            st.session_state.historia = f"**{frase_desafio}**\n\n{resposta}"
            st.session_state.finalizada = False
            st.session_state.prompt_base = prompt
            st.rerun()

    else:
        st.warning("Por favor, selecione preencha todos os campos.")

if st.session_state.historia:
    st.markdown("### História Gerada:")
    st.markdown(st.session_state.historia)

    if not st.session_state.finalizada:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Continuar História"):
                with st.spinner("Gerando continuação..."):
                    novo_trecho = gerar_resposta_gemini("Continue a história a partir do último parágrafo, adicionando somente mais um parágrafo.")
                    st.session_state.historia += f"\n\n{novo_trecho}"
                    st.rerun()

        with col2:
            if st.button("Finalizar História"):
                with st.spinner("Finalizando..."):
                    final = gerar_resposta_gemini("Finalize a história em um único parágrafo, baseado no dercorrer da história completa.")
                    st.session_state.historia += f"\n\n{final}"
                    st.session_state.finalizada = True
                    st.rerun()
