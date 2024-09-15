import time
from threading import Thread, Lock
import sys

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
        ("Tampar aku di pipi", 0.16),
        ("Biar sadar dan ku mengerti", 0.17),
        ("\n""Hujan samarkan derasnya", 0.14),
        ("Tutup air mata", 0.15),
        ("Temani kecewa ku yang tlah lama", 0.15),
        ("Berdosakah ku berdoa", 0.14),
        
    ]
    delays = [0.3, 5.8, 10.8, 12.5, 17.4, 22.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()