import streamlit as st
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio

st.title("Conversor de Texto para Fala")

# Insere o texto
texto = st.text_area("Digite o texto que deseja converter para fala:")

# Configurações da língua e velocidade
lingua = st.selectbox("Selecione a língua:", ["pt", "en"])
velocidade = st.slider("Selecione a velocidade:", 0.1, 2.0, 1.0, 0.1)

# Verifica se o botão foi pressionado
if st.button("Converter para Fala"):
    # Cria o objeto gTTS com o texto e língua selecionados
    tts = gTTS(texto, lang=lingua)

    # Cria o buffer para armazenar o áudio gerado
    fp = BytesIO()
    tts.write_to_fp(fp)

    # Cria um objeto de áudio
    audio = Audio(fp.getvalue(), autoplay=True)

    # Extrai os dados de áudio do objeto Audio
    audio_data = audio.data

    # Exibe o áudio no Streamlit
    st.audio(audio_data, format='audio/mp3', start_time=0)
