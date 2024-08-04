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
|____/ \___/ \__,_|_| |_|\__,_|_|   |_|\___/_/\_\  Made By Mr. Bilred 
                                                                For Fun Actually :) 
                                                                    Cuz I Was Feeling Some Boredom
                                                                        (Please Don't Commit Sins With This One ;))
                                                      
"""
print(Fore.CYAN + banner)
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
    #  To Ensure The Volume Level Is Between 0.0 and 1.0
    if 0.0 <= volume_level <= 1.0:
        pygame.mixer.music.set_volume(volume_level)
        print(f"Volume Set To {int(volume_level * 100)}% ")
    else:
        print(Fore.LIGHTRED_EX + f"Volume must be between 0.0 and 1.0")


if __name__ == "__main__":
    try:

        music_file = input(Fore.LIGHTMAGENTA_EX + "Enter the exact name of the audio file (e.g example.mp3): ").strip()
        load_music(music_file)
        play_music()

        while True:
            print(Fore.LIGHTMAGENTA_EX + "\nCommands: play, pause, unpause, stop, quit")
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
                    _, level_str = command.split()
                    volume_level = float(level_str)  # Converting the level_str (the level provided by the user)
                    # to float (because it's required by Pygame)
                    set_volume(volume_level)
                except ValueError:  # If the conversion from string to float fails
                    print(Fore.LIGHTRED_EX + "Hey, Provide a valid volume level (e.g volume 0.5)")
                except IndexError:  # If the split() method does not provide exactly two elements i.e volume 0.5
                    print(Fore.LIGHTRED_EX + "Oops, Specify a volume level e.g volume 0.5")

            elif command == "quit":
                break
            elif command == "help":
                print("Commands List: play, pause, unpause, stop, quit")
            else:
                print("Invalid Command")

    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Error Occured: {e}")
