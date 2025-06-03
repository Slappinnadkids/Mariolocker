import subprocess
import random
import time
import tkinter as tk
import threading
import os
import webbrowser
from random import randint
import sys

# Global flag to track if the user presses ESC to exit
exit_flag = False

# Zalgo Text Function
def zalgo_text(text):
    zalgo_chars = [
        "̴", "̸", "͏", "̜", "̛", "͠", "͡", "̨", "̴", "͟", "͞", "̸", "͞", "̛", "͡", "̢"
    ]
    result = ''.join([char + random.choice(zalgo_chars) for char in text])
    return result

# Function to show the Zalgo message with a popup
def show_zalgo_message(message, delay=0):
    root = tk.Tk()
    root.title("Zalgo Text")
    
    # Check for Esc key press in the background
    root.bind("<Escape>", exit_program)
    
    label = tk.Label(root, text=zalgo_text(message), font=("Helvetica", 20), bg="black", fg="white", pady=10, padx=10)
    label.pack()
    root.after(delay * 1000, root.destroy)  # Close after 'delay' seconds
    root.mainloop()

# Function to trigger a fake BSOD (Blue Screen of Death)
def trigger_fake_bsod():
    bsod_message = """
    *** STOP: 0x0000007B (0xFFFFF880009A9928, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000)
    KERNEL DATA INPAGE ERROR
    """
    root = tk.Tk()
    root.title("Error")
    
    # Check for Esc key press in the background
    root.bind("<Escape>", exit_program)
    
    label = tk.Label(root, text=bsod_message, font=("Courier New", 16), bg="blue", fg="white", pady=20, padx=20)
    label.pack()
    root.geometry("800x600")
    root.mainloop()

# Function to play Mario's Yahoo! sound and pipe warp sound
def play_mario_sounds():
    subprocess.run(['powershell', '-c', 'Add-Type -TypeDefinition "using System.Media; public class Sound { public static void Play(string path) { SoundPlayer player = new SoundPlayer(path); player.PlaySync(); } }"; Sound::Play("path_to_your_mario_yahoo.wav")'])
    time.sleep(1)
    subprocess.run(['powershell', '-c', 'Add-Type -TypeDefinition "using System.Media; public class Sound { public static void Play(string path) { SoundPlayer player = new SoundPlayer(path); player.PlaySync(); } }"; Sound::Play("path_to_your_pipe_warp.wav")'])

# Function to open file explorer and simulate file search
def open_file_explorer_and_search(file_name="Im OnLY HeRE To PlaY"):
    subprocess.run("explorer", shell=True)
    time.sleep(1)  # Allow the File Explorer to open

    file_found = False
    timer_start = time.time()
    
    while time.time() - timer_start < 120:  # 2-minute timer
        if file_name in os.listdir():
            file_found = True
            break
        time.sleep(1)

    return file_found

# Function to simulate Mario 1986 (1st Level)
def start_mario_game():
    url = "https://www.mariogame.com"  # Replace with Mario game link
    subprocess.run(["start", url], shell=True)

# Function to return to desktop
def return_to_desktop():
    subprocess.run("explorer", shell=True)

# Function to start Minesweeper game
def start_minesweeper_game():
    url = "https://minesweeperonline.com"
    subprocess.run(["start", url], shell=True)

# Function to handle exit via Esc key
def exit_program(event=None):
    global exit_flag
    exit_flag = True
    print("Exiting...")
    sys.exit()

# Complete sequence function
def run_sequence():
    global exit_flag
    # Step 1: Play Mario Sounds
    play_mario_sounds()

    # Step 2: Show Zalgo Message "I'M HeRE"
    if exit_flag: return
    show_zalgo_message("I'M HeRE", 2)
    time.sleep(2)

    # Step 3: Mario Image pops up
    subprocess.run(['powershell', '-c', 'Add-Type -TypeDefinition "using System.Media; public class Sound { public static void Play(string path) { SoundPlayer player = new SoundPlayer(path); player.PlaySync(); } }"; Sound::Play("path_to_your_mario_image.png")'])
    time.sleep(2)

    # Step 4: Zalgo Message "I HaVE YOUr COmpUTEr"
    if exit_flag: return
    show_zalgo_message("I HaVE YOUr COmpUTEr", 3)
    time.sleep(3)

    # Step 5: Ask user to find file
    if exit_flag: return
    file_found = open_file_explorer_and_search()

    if not file_found:
        # If file is not found, trigger BSOD
        if exit_flag: return
        trigger_fake_bsod()
        show_zalgo_message("I KneW YoU WeRENt GoOD EnOUgH", 2)
    else:
        # If file found, proceed to Mario Game
        if exit_flag: return
        show_zalgo_message("BeAT Me", 1)
        start_mario_game()

        # Step 6: Run Minesweeper with Zalgo Message
        if exit_flag: return
        show_zalgo_message("DoNT BloW UP", 1)
        start_minesweeper_game()

        time.sleep(30)  # Simulate Minesweeper time

        # If they die, show BSOD
        if exit_flag: return
        trigger_fake_bsod()
        show_zalgo_message("I KneW YoU WeRENt GoOD EnOUgH", 2)

    # Final Step: Show peace message and return to desktop
    if exit_flag: return
    show_zalgo_message("FinALLY PEaCE", 2)
    time.sleep(2)
    return_to_desktop()

# Start the prank in a new thread to not block the main thread
threading.Thread(target=run_sequence).start()
