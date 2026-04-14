import whisper
from gtts import gTTS

# Configuração
language = "pt"

# Carregar modelo
model = whisper.load_model("small")

# Arquivo de áudio
arquivo_audio = "Assistente_de_voz_IA.mp4.aac"

# Transcrição
resultado = model.transcribe(arquivo_audio, language=language)
texto = resultado["text"]

print("Você disse:", texto)

# Resposta simulada
resposta = f"Entendi o que você disse: {texto}. Este é um exemplo de resposta com inteligência artificial."

print("Resposta:", resposta)

# Converter resposta em áudio
tts = gTTS(text=resposta, lang=language)
tts.save("resposta.mp3")
