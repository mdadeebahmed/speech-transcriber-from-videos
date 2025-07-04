"""
Install below libraries
-----------------------
pip install moviepy==1.0.3
pip install SpeechRecognition



Run below file
--------------
py extract_text_from_video_multiple_files.py

"""

print("Step 1: Importing the libraries")

import os
import glob
import moviepy.editor as mp
import speech_recognition as sr








print(" Step 2: Loading the video/mp4 file")

def load_video(folder):
    files = os.path.join(folder, "*.mp4")
    mp4_files = glob.glob(files)
    return mp4_files





print("Step 3: Extract audio from video/mp4 file")

def audio_from_video(file_list):
    video = mp.VideoFileClip(file_list)  # Load video
    audio_file = video.audio  # Get the audio
    audio_path = f"./audio/{os.path.basename(file_list)}.wav"  # Save path
    audio_file.write_audiofile(audio_path)  # Save the audio as WAV file
    return audio_path  # Return audio file path







print("Step 4: Loading audio file, extract text from audio file using speech recognition")

def extract_text_from_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        data = r.record(source)  # Record audio data
    try:
        text = r.recognize_google(data)  # Use Google Web Speech API to recognize speech
    except sr.UnknownValueError:
        text = "Audio is unclear, could not extract text."
    except sr.RequestError:
        text = "Could not request results from Google Speech Recognition service."
    return text






# Folder containing video files

f = "./videos"
mp4_file_list = load_video(f)




# Create a dictionary to store video names and their corresponding extracted text

video_text_dict = {}

# Loop through each video file in the folder
for video_path in mp4_file_list:
    print(f"Processing video: {video_path}")
    
    # Extract audio from the video file
    audio_path = audio_from_video(video_path)
    
    # Extract text from the audio
    extracted_text = extract_text_from_audio(audio_path)
    
    # Add the extracted text to the dictionary with the video name as the key
    video_name = os.path.basename(video_path)
    video_text_dict[video_name] = extracted_text



# Print the results

print("\nExtracted Text from Videos:\n")

# print(video_text_dict)

for i in video_text_dict:
    print(i, video_text_dict[i])