#!/usr/bin/env python
__author__ = "liuhui"
import pygame as py
from pygame.locals import *


# init
py.init()
title = "Super Mario"
py.display.set_caption(title)
scr_size = (200, 200)
scr = py.display.set_mode(scr_size, 0, 32)
mario_jump_path = "resources/graphics/mariojump2.gif"
mario_jump = py.image.load(mario_jump_path).convert_alpha()


def main():
    while True:
        for event in py.event.get():
            if event.type == QUIT:
                quit(1)
        scr.blit(mario_jump, (0, 0))
        py.display.update()
    pass


if __name__ == "__main__":
    main()
