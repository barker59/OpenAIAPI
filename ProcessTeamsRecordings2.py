from pytube import YouTube
from moviepy.editor import *
import openai
from pydub import *
openai.api_key = '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'

def extract_audio_to_mp3(video_file, output_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(output_file, codec='mp3')

def download_youtube_video(url, output_path="."):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    return video.download(output_path)

# # Replace with the YouTube video URL you want to download
# youtube_video_url = "https://youtu.be/0FFS2iSeNqY"
# # Replace with the desired output path (default is the current directory)
# output_path = "."
#
# video_file = download_youtube_video(youtube_video_url, output_path)
#
# # Extract audio from the downloaded video and save it as an MP3 file
# output_audio = "output_audio2.mp3"
# extract_audio_to_mp3(video_file, output_audio)

# Load the original audio file
AudioSegment.ffmpeg = r"C:\Users\Aaron\Desktop\Code\ffmpeg-6.0-essentials_build"
audio_file = AudioSegment.from_file(file=r"C:\Users\Aaron\Desktop\Code\OpenAiApi2\output_audio3.mp3", format="mp3")

# Set the start and end time for the 25-minute segment
start_time = 0  # in milliseconds
end_time = 25 * 60 * 1000  # 25 minutes in milliseconds

# Trim the audio file to the 25-minute segment
segment = audio_file[start_time:end_time]

# Export the trimmed segment as a new mp3 file
segment.export("25_minute_audio.mp3", format="mp3")

audio_file= open("25_minute_audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
transcript_name = "Transcript_{}.txt".format("Aggregates.mp4")

with open(transcript_name, "w") as transcript_file:
    transcript_file.write(transcript.text)

def ask_question(context, question):
    prompt = f"{context}\n\nQuestion: {question}\nAnswer:"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

def ask_question_chat(context, question):
    messages = [
        {"role": "system", "content": "You’re a kind helpful assistant"}
    ]
    prompt = f"{context}\n\nQuestion: {question}\nAnswer:"
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=250,
        messages=messages
    )

    chat_response = response.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    return chat_response

# Replace this with your translated text or any context you want to provide
context = transcript.text

# Replace this with the question you want to ask
question = "What services could I offer this person as a consultant?"

# "Summarize the key discussion points and decisions made in the meeting."
# "Identify the main action items and assigned responsibilities from the meeting."
# "Highlight any challenges or obstacles discussed and proposed solutions."
# "List the key milestones or deadlines mentioned in the meeting."
# "Determine any patterns or recurring themes across multiple meetings."
# "Compare progress on action items from previous meetings to the current meeting."
# "Assess the overall sentiment and engagement level of meeting participants."
# "Identify any instances of miscommunication or areas where clarification may be needed."
# "Analyze the effectiveness of the meeting's agenda and format, and suggest improvements for future meetings."
# "Extract any valuable insights or ideas shared by participants during the meeting."
response = ask_question_chat(context, question)

print(f"Question: {question}")
print(f"Response: {response}")

