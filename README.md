# SoundFlex

SoundFlex is a lightweight command-line audio player built using Python and Pygame. It allows you to play, pause, unpause, stop, and adjust the volume of your audio files through simple commands. This tool was created for fun and is ideal for quick audio playback from the terminal.
Actually, I guess, I was feeling some kind of boredom, so I began to create this project :)

## Features
- **Play**: Start playing an audio file.
- **Pause**: Pause the currently playing audio.
- **Unpause**: Resume playback of the paused audio.
- **Stop**: Stop the audio playback.
- **Volume Control**: Adjust the volume of the audio.

## Version 1.1
- Basic Functionality: Allows you to load, play, pause, unpause, and stop audio files.
- Volume Control: Set volume levels directly, with checks for valid input ranges.
- Error Handling: Basic error handling for file operations and commands.

## What's New in Version 1.2
- Audio File Listing: Added functionality to list all audio files in the current directory, making it easier to find and select files.
- Volume Input Range: Adjusted volume input to accept values between 0 and 100 (converted to a range of 0.0 to 1.0 internally).
- Enhanced User Experience: Updated command options and improved error handling for volume and file operations.

![image](https://github.com/BilalAhmadKhanKhattak/SoundFlex/blob/main/Screenshot%20(10).png)


## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/bilalahmadkhankhattak/soundflex.git
    cd soundflex
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

    Ensure you have Python 3.x installed and the following Python packages:
    - `pygame`
    - `colorama`

    You can install them manually if needed:
    ```sh
    pip install pygame colorama
    ```

3. **Copy Your Audio Files**:
    - Place the audio files you want to play in the same directory.

## Usage

1. **Run the program**:
    ```sh
    python3 SoundFlex.py
    ```

2. **Enter the exact name of the audio file**:
    - Example: `example.mp3`
  
3. **Use the following commands**:
    - **play**: Play the audio file.
    - **pause**: Pause the playback.
    - **unpause**: Resume playback after pausing.
    - **stop**: Stop the playback.
    - **volume [level]**: Adjust the volume level (e.g., `volume 0.5`).
    - **quit**: Exit the program.

4. **Example Session**:
    ```
    Enter the exact name of the audio file (e.g., example.mp3): youraudiofile.mp3
    Loaded youraudiofile.mp3
    Playing...

    Commands: play, pause, unpause, stop, quit
    Enter Command: pause
    Paused

    Enter Command: volume 0.7
    Volume Set To 70%

    Enter Command: quit
    ```

## License

This project is licensed under the **Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. You may use, modify, and distribute this code for non-commercial purposes with appropriate credit. Commercial use is prohibited.

## Credits

Made by **Bilal Ahmad Khan Khattak** (also known as **Bilred**). 

---

### Notes:
- The program may require you to have the necessary audio drivers installed on your system to function correctly.
- This tool is for personal and educational purposes only. Please respect copyright laws when using audio files.

---

Enjoy using SoundFlex!

--- 
