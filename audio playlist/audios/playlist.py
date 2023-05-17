import random
import pygame

# List of audio files
audio_files = [
"1.mp3",
"2.mp3",
"3.mp3",
"4.mp3",
"5.mp3",
"6.mp3",
"7.mp3",
"8.mp3",
"9.mp3",
"10.mp3",
"11.mp3",
"12.mp3",
"13.mp3",
"14.mp3",
"15.mp3",
"16.mp3",
"17.mp3",
"18.mp3",
"19.mp3",
"20.mp3"

]

# Initializing
pygame.mixer.init()

# Create a copy of audio files list
unplayed_audios = audio_files.copy()

# playing an audio randomly without repetition within a cycle
while unplayed_audios:
    audio_file = random.choice(unplayed_audios)
    unplayed_audios.remove(audio_file)

    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    #waiting for the audio to finish playing
    while pygame.mixer.music.get_busy():
        continue

# Clean up resources
pygame.mixer.quit()








