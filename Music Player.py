#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pygame
from tkinter import Tk, filedialog
from tkinter import Button, Label

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Initialize pygame
        pygame.init()

        # Initialize variables
        self.playing = False
        self.paused = False
        self.current_song = None

        # Custom colors
        window_bg_color = "#34495E"  # Dark background color for the window
        button_color = "#3498DB"  # Blue button color
        text_color = "#FFFFFF"  # White text color

        # Set window properties
        self.root.geometry("400x150")
        self.root.resizable(False, False)  # Make window non-changeable

        # Set window background color
        self.root.configure(bg=window_bg_color)

        # Create UI elements with custom colors
        button_size = 5
        self.play_button = Button(root, text="Play", command=self.play_music, height=button_size, width=button_size * 2, bg=button_color, fg=text_color)
        self.pause_button = Button(root, text="Pause", command=self.pause_music, height=button_size, width=button_size * 2, bg=button_color, fg=text_color)
        self.stop_button = Button(root, text="Stop", command=self.stop_music, height=button_size, width=button_size * 2, bg=button_color, fg=text_color)
        self.open_button = Button(root, text="Open", command=self.open_file, height=button_size, width=button_size * 2, bg=button_color, fg=text_color)
        self.status_label = Label(root, text="No file selected", bg=window_bg_color, fg=text_color)

        # Arrange UI elements in a line
        self.open_button.grid(row=0, column=0, padx=10, pady=10)
        self.play_button.grid(row=0, column=1, padx=10, pady=10)
        self.pause_button.grid(row=0, column=2, padx=10, pady=10)
        self.stop_button.grid(row=0, column=3, padx=10, pady=10)
        self.status_label.grid(row=1, columnspan=4, pady=10, sticky="w")

    def play_music(self):
        if self.current_song:
            if not self.playing:
                pygame.mixer.music.load(self.current_song)
                pygame.mixer.music.play()
                self.playing = True
                self.paused = False
                self.status_label.config(text=f"Playing: {self.current_song}")
            elif self.paused:
                pygame.mixer.music.unpause()
                self.paused = False

    def pause_music(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            self.status_label.config(text="Paused")

    def stop_music(self):
        if self.playing or self.paused:
            pygame.mixer.music.stop()
            self.playing = False
            self.paused = False
            self.status_label.config(text="Music Stopped")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.current_song = file_path
            self.status_label.config(text=f"Selected: {file_path}")

# Create the Tkinter window
root = Tk()

# Create an instance of the MusicPlayer class
music_player = MusicPlayer(root)

# Run the Tkinter event loop
root.mainloop()


# In[ ]:




