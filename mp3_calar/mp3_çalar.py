import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Python MP3 Player")
        self.root.geometry("400x400")
        self.root.config(bg="#2c3e50") # Dark theme

        # Initialize Pygame Mixer
        pygame.mixer.init()

        self.current_file = None
        self.is_paused = False

        # --- UI Elements ---
        self.label = tk.Label(root, text="No File Selected", font=("Helvetica", 12), 
                              fg="white", bg="#2c3e50", wraplength=350)
        self.label.pack(pady=30)

        # Button Style
        btn_style = {"width": 15, "font": ("Helvetica", 10, "bold"), "bd": 0, "cursor": "hand2"}

        self.open_button = tk.Button(root, text="Select Track", command=self.load_music, 
                                     bg="#3498db", fg="white", **btn_style)
        self.open_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_music, 
                                     bg="#2ecc71", fg="white", **btn_style)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause/Resume", command=self.pause_music, 
                                      bg="#f1c40f", fg="black", **btn_style)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music, 
                                     bg="#e74c3c", fg="white", **btn_style)
        self.stop_button.pack(pady=10)

        # Volume Slider
        self.volume_label = tk.Label(root, text="Volume", fg="white", bg="#2c3e50")
        self.volume_label.pack(pady=(20, 0))
        self.volume_slider = tk.Scale(root, from_=0, to=1, resolution=0.1, 
                                      orient=tk.HORIZONTAL, command=self.set_volume,
                                      bg="#2c3e50", fg="white", highlightthickness=0)
        self.volume_slider.set(0.5) # Default 50% volume
        self.volume_slider.pack()

    def load_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            try:
                self.current_file = file_path
                pygame.mixer.music.load(self.current_file)
                self.label.config(text=f"Oynatılıyor: {os.path.basename(self.current_file)}")
                self.play_music() # Yüklenirse otomatik başlat
            except pygame.error as e:
                # Dosya bozuksa kullanıcıya uyarı ver
                messagebox.showerror("Hata", f"Müzik dosyası açılamadı!\nDetay: {e}")
                self.current_file = None
                self.label.config(text="Dosya hatası!")

    def play_music(self):
        # Eğer dosya başarıyla yüklendiyse oynat
        if self.current_file and pygame.mixer.music.get_busy() == False:
            try:
                pygame.mixer.music.play()
                self.is_paused = False
            except pygame.error:
                messagebox.showwarning("Uyarı", "Müzik çalınamıyor. Lütfen dosyayı kontrol edin.")

    def pause_music(self):
        if not self.current_file:
            return
            
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            pygame.mixer.music.pause()
            self.is_paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_paused = False

    def set_volume(self, val):
        volume = float(val)
        pygame.mixer.music.set_volume(volume)

if __name__ == "__main__":
    root = tk.Tk()
    app = MP3Player(root)
    root.mainloop()