import openai
# openai.organization = "org-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"
openai.api_key = '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'
audio_file= open("output_audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

with open("transcript.txt", "w") as transcript_file:
    transcript_file.write(transcript.text)