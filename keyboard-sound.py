#!/usr/bin/python3
from pynput.keyboard import Listener
from pygame import mixer

def play():
    mixer.init()
    mixer.music.load('test.mp3')
    mixer.music.play()

def on_press(key):
    try:
        if key.char == 'p':
            play()
        print(key.char)
    except AssertionError:
        pass

with Listener(on_press = on_press) as l:
    l.join()