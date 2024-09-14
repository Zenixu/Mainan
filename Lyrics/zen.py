import pygame
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
        ("Itsudatte tonari ni ite", 0.18),
        ("Watashi dake o mitsumetekureta nee", 0.14),
        ("\n""Suki yo", 0.09),
        ("Ima anata ni omoi nosete", 0.12),
        ("Hora, sunao ni naru no watashi", 0.18),
        ("Kono saki motto soba ni ite mo ii ka na?", 0.13),
        ("Koi to koi ga kasanatte", 0.14),
        ("\n""Suki yo", 0.11),
        ("Ima anata ni omoi todoke", 0.14),
        ("Nee, kizuitekuremasen ka?", 0.2),
        ("Doushiyou mo nai kurai", 0.18),
        ("Kokoro made suki ni natteiku", 0.16),
    ]
    delays = [0.3, 1.9, 11.0, 12.3, 14.3, 14.9, 15.0, 16.3, 17.3, 21.0, 25.3, 30.5]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()
pygame.init()
sound = pygame.mixer.Sound('koiro.wav')
sound.play()
pygame.time.wait(int(sound.get_length() * 1))

if __name__ == "__main__":
    sing_song()