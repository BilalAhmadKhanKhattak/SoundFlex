import colorama
import pygame
import os
from colorama import Fore

colorama.init(autoreset=True)
pygame.mixer.init()

banner = """
 ____                        _ _____ _           
/ ___|  ___  _   _ _ __   __| |  ___| | _____  __
\___ \ / _ \| | | | '_ \ / _` | |_  | |/ _ \ \/ /
 ___) | (_) | |_| | | | | (_| |  _| | |  __/>  < 
|____/ \___/ \__,_|_| |_|\__,_|_|   |_|\___/_/\_\  Version 1.3  
                                                        Made By Mr. Bilred 
                                                            For Fun Actually :) 
                                                            Cuz I Was Feeling Some Boredom
                                                            (Please Don't Commit Sins With This One ;))
Github: github.com/Bilalahmadkhankhattak/SoundFlex                                                      
"""
print(Fore.CYAN + banner)


#  I don't think the following functions would be somehow hard to understand :)
def load_music(file_path):  # Load The File, If it really exists
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        print(Fore.LIGHTBLUE_EX + f"Loaded {file_path}")

    else:
        print(Fore.LIGHTRED_EX + f"File {file_path} not found")


def play_music():
    pygame.mixer.music.play()
    print(Fore.LIGHTBLUE_EX + "Playing...")


def pause_music():
    pygame.mixer.music.pause()
    print(Fore.LIGHTBLUE_EX + "Paused")


def unpause_music():
    pygame.mixer.music.unpause()
    print(Fore.LIGHTBLUE_EX + "Unpaused")


def stop_music():
    pygame.mixer.music.stop()
    print(Fore.LIGHTYELLOW_EX + "Stopped")


def set_volume(volume_level):
    volume_level = volume_level / 100  # This converts the volume level from 0-100 to 0.0-1.0
    if 0.0 <= volume_level <= 1.0:  # Ensure the volume level is between 0.0 to 1.0
        pygame.mixer.music.set_volume(volume_level)
        print(f"Volume Set To {(volume_level * 100)}% ")
    else:
        print(Fore.LIGHTRED_EX + f"Volume must be between 0 and 100")


def audio_files_listing():  # This Function is to list the audio files in the current directory (SoundFlex V 1.2)
    audio_extensions = {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'}  # Common Audio File Extensions
    files = os.listdir()  # This basically list all the contents in dir
    audio_files = [file for file in files if os.path.splitext(file)[1].lower() in audio_extensions]  # creates a new
    # list of 'file' where each 'file' comes from the 'files' but only include 'file', if condition after 'if' is
    # true, Confusing, Right?
    print(f"Audio Files in the Current Folder: ")
    for i, file in enumerate(audio_files, start=1):
        print(f"{i}. {file}")
    return audio_files


if __name__ == "__main__":
    try:
        audio_files = audio_files_listing()

        # Ask user to select a file by number
        while True:
            try:
                choice = int(
                    input(Fore.LIGHTMAGENTA_EX + "Enter the number of the audio file you want to play: ").strip())
                if 1 <= choice <= len(audio_files):
                    music_file = audio_files[choice - 1]
                    break
                else:
                    print(Fore.LIGHTRED_EX + "Invalid choice. Please enter a number corresponding to the listed files.")
            except ValueError:
                print(Fore.LIGHTRED_EX + "Invalid input. Please enter a valid number.")
        load_music(music_file)
        play_music()
        while True:
            print(Fore.LIGHTMAGENTA_EX + "\nCommands: play, pause, unpause, stop, quit, volume <value>")
            command = input("Enter Command: ").strip().lower()

            if command == "play":
                play_music()
            elif command == "pause":
                pause_music()
            elif command == "unpause":
                unpause_music()
            elif command == "stop":
                stop_music()
            elif command.startswith("volume"):
                try:
                    _, level_str = command.split()  # here, this method splits the command, ignores the first part(
                    # which is _ and the second part is level_str
                    volume_level = float(level_str)  # Converting the level_str (the level provided by the user)
                    # to float (because it's required by Pygame)
                    set_volume(volume_level)
                except ValueError:  # If the conversion from string to float fails
                    print(Fore.LIGHTRED_EX + "Hey, Provide a valid volume level e.g volume 50")
                except IndexError:  # If the split() method does not provide exactly two elements i.e volume 0.5
                    print(Fore.LIGHTRED_EX + "Oops, Specify The Volume Level like this, volume 50")

            elif command == "quit" or "quit":
                break
            elif command == "help":
                print("Commands List: play, pause, unpause, stop, quit")
            else:
                print(Fore.LIGHTRED_EX + "Invalid Command")

    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error Occured: {e}")
