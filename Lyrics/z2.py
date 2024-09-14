import time
from threading import Thread, Lock
import sys
import pygame 

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)


def sing_song():
    lyrics = [
        ("Ah", 0.1),
        ("Aku sangat menyukainya", 0.040),
        ("\nApakah aku benar benar berfikir", 0.020),
        ("Bahwa orang seperti dia akan tertarik kepadaku?", 0.030),
        ("\nAku sangat bodoh", 0.018),
        ("Sungguh bodoh", 0.050),
        ("Menyedihkan", 0.021),
        
    ]
    delays = [0.3, 1.8, 4.0, 5.3, 9.1, 10.4, 13.22, 14.2]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()
pygame.init()
sound = pygame.mixer.Sound('123.wav')
sound.play()
pygame.time.wait(int(sound.get_length() * 1))

if __name__ == "__main__":
    sing_song()