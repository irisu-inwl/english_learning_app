from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

def transform_text_to_speech(text: str):
    # TODO: 生成AIで問題を溜めて活用できる方針にするのであれば、音声合成した結果も保存して参照できるようにする
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    # TODO: 発話者属性を可変にする
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response.audio_content


