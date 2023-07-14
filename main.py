import platform
import subprocess

import playsound
import pyautogui as pag
import pygame

pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

try:
    joystick = joysticks[0]
except IndexError:
    raise Exception("You must have a controller connected!")


pag.FAILSAFE = True
SPEED = 100
# pag.PAUSE = 1

coordinate = [pag.size()[0] / 2, pag.size()[1] / 2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEREMOVED:
            print("Removed Joystick.")
        if event.type == pygame.JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            joystick = joysticks[0]
            print("Added Joystick!")

    # Get both axes of the right stick
    axis = joystick.get_axis(3)
    axis2 = joystick.get_axis(4)

    if axis > .2:
        coordinate[0] += axis * SPEED
        if coordinate[0] > pag.size()[0]:
            coordinate[0] = pag.size()[0] - 5
    elif axis < -.2:
        coordinate[0] += axis * SPEED
        if coordinate[0] < 0:
            coordinate[0] = 5

    if axis2 > .2:
        coordinate[1] += axis2 * SPEED
        if coordinate[1] > pag.size()[1]:
            coordinate[1] = pag.size()[1] - 5
    elif axis2 < -.2:
        coordinate[1] += axis2 * SPEED
        if coordinate[1] < 0:
            coordinate[1] = 5

    if joystick.get_button(15):  # Left arrow
        pag.click()

    if joystick.get_button(4):  # L1
        SPEED -= 20
        pass
    if joystick.get_button(5):  # R1
        SPEED += 20
        pass

    if joystick.get_button(13):  # Up
        pag.scroll(3)
    if joystick.get_button(14):  # Down
        pag.scroll(-3)

    if joystick.get_button(0):  # Cross
        raise SystemExit(0)

    if joystick.get_button(16):  # Right
        pag.typewrite("f")
    if joystick.get_button(9):  # Start
        pag.hotkey("ctrl", "t")
        pag.typewrite("youtube.com")
        pag.keyDown("enter")
        pag.keyUp("enter")
    if joystick.get_button(10):  # PS
        pag.hotkey("ctrl", "r")
    if joystick.get_button(8):  # Select
        pag.hotkey("win", "2")

    if joystick.get_button(6):  # Left trigger
        pag.press("volumedown")
    if joystick.get_button(7):  # Right trigger
        pag.press("volumeup")

    pag.moveTo(coordinate)
