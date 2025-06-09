# Gerador de Histórias Interativas

Este é um aplicativo desenvolvido em **Streamlit** para criar o início de histórias interativas com base nas escolhas do usuário. Ele permite que você crie um personagem, escolha o gênero literário e o local inicial, e ainda defina uma frase de efeito ou desafio inicial. Após fornecer esses dados, o aplicativo gera uma introdução envolvente para a história, com a possibilidade de continuar ou finalizar a narrativa.

## Funcionalidades

- **Entrada do Usuário**: O usuário escolhe:
  - **Nome do protagonista**.
  - **Gênero literário** da história.
  - **Local inicial** para a trama.
  - **Frase de efeito ou desafio inicial** que será incorporada na introdução.

- **Geração da História**: O aplicativo usa essas informações para gerar o início da história de forma envolvente.

- **Botões de Interatividade**:
  - **"Continuar História"**: Ao clicar neste botão, a história é continuada com um novo parágrafo gerado com base no texto anterior.
  - **"Finalizar História"**: Ao clicar neste botão, a história é finalizada com um desfecho adequado e conclusivo.

## Como Funciona

1. **Entrada de Dados**:
   - O usuário insere o nome do protagonista, escolhe o gênero literário e o local inicial, e escreve uma frase de efeito ou desafio. Essas escolhas são usadas para criar um prompt que será enviado para uma IA (por exemplo, Gemini ou GPT-3/4) para gerar o início da história.

2. **Geração da História**:
   - O aplicativo usa o prompt gerado com as escolhas do usuário para solicitar à IA a criação de um início de história.
   - O início da história será exibido na interface do Streamlit.

3. **Continuação da História**:
   - O botão **"Continuar História"** permite que o usuário adicione mais um parágrafo à história. Ao clicar, o aplicativo gera um novo trecho baseado no último parágrafo gerado.
   
4. **Finalização da História**:
   - O botão **"Finalizar História"** encerra a história com um desfecho adequado. Uma vez que a história for finalizada, a opção de continuar desaparece.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- Streamlit (instale com: `pip install streamlit`)

### Rodando o aplicativo
1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/gerador-historias.git
```
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o Streamlit:

```bash
streamlit run app.py
```

O aplicativo abrirá em um navegador, onde você poderá inserir as informações e interagir com a geração da história.
