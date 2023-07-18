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
in_action = False
pygame.time.set_timer(pygame.USEREVENT, 500)
# pag.PAUSE = 1
left, right, up, down = 0, 0, 0, 0
increment = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEREMOVED:
            print("Removed Joystick.")
        if event.type == pygame.JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            joystick = joysticks[0]
            print("Added Joystick!")
        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
            if event.button == 0:
                pag.press("enter")
            if event.button == 1:
                pag.press("escape")
            if event.button == 13:
                pag.press("up")
                up = 1
                increment = True
            if event.button == 14:
                pag.press("down")
                down = 1
                increment = True
            if event.button == 15:
                pag.press("left")
                left = 1
                increment = True
                print(increment, "Yay")
            if event.button == 16:
                pag.press("right")
                right = 1
                increment = True
        if event.type == pygame.JOYBUTTONUP:
            up, down, left, right = 0, 0, 0, 0
            increment = False

        if event.type == pygame.USEREVENT:
            in_action = False

        if event.type == pygame.JOYAXISMOTION:
            if in_action:
                continue
            if event.axis == 0:
                if event.value > 0.5:
                    pag.press("right")
                    in_action = True
                if event.value < -0.5:
                    pag.press("left")
                    in_action = True
            elif event.axis == 1:
                if event.value > 0.5:
                    pag.press("down")
                    in_action = True
                if event.value < -0.5:
                    pag.press("up")
                    in_action = True
    if left > 0:
        left += 1
    if right > 0:
        right += 1
    if up > 0:
        up += 1
    if down > 0:
        down += 1
    pygame.time.Clock().tick(120)

    if left > 30:
        pag.press("left")
    if right > 30:
        pag.press("right")
    if up > 30:
        pag.press("up")
    if down > 30:
        pag.press("down")

    # Get both axes of the right stick
    # axis = joystick.get_axis(3)
    # axis2 = joystick.get_axis(4)
    # #
    # # if axis > .2:
    # #     coordinate[0] += axis * SPEED
    # #     if coordinate[0] > pag.size()[0]:
    # #         coordinate[0] = pag.size()[0] - 5
    # # elif axis < -.2:
    # #     coordinate[0] += axis * SPEED
    # #     if coordinate[0] < 0:
    # #         coordinate[0] = 5
    # #
    # # if axis2 > .2:
    # #     coordinate[1] += axis2 * SPEED
    # #     if coordinate[1] > pag.size()[1]:
    # #         coordinate[1] = pag.size()[1] - 5
    # # elif axis2 < -.2:
    # #     coordinate[1] += axis2 * SPEED
    # #     if coordinate[1] < 0:
    # #         coordinate[1] = 5
    #
    # if joystick.get_button(15):  # Left arrow
    #     pag.click()
    #
    # if joystick.get_button(4):  # L1
    #     pass
    # if joystick.get_button(5):  # R1
    #     pass
    #
    # if joystick.get_button(13):  # Up
    #     pag.press("up")
    # if joystick.get_button(14):  # Down
    #     pag.press("down")
    #
    # if joystick.get_button(0):  # Cross
    #     raise SystemExit(0)
    #
    # if joystick.get_button(16):  # Right
    #     pag.typewrite("f")
    # if joystick.get_button(9):  # Start
    #     pag.hotkey("ctrl", "t")
    #     pag.typewrite("youtube.com")
    #     pag.keyDown("enter")
    #     pag.keyUp("enter")
    # if joystick.get_button(10):  # PS
    #     pag.hotkey("ctrl", "r")
    # if joystick.get_button(8):  # Select
    #     pag.hotkey("win", "2")
    #
    # if joystick.get_button(6):  # Left trigger
    #     pag.press("volumedown")
    # if joystick.get_button(7):  # Right trigger
    #     pag.press("volumeup")
    if joystick.get_button(6):  # Left trigger
        subprocess.call(["pactl", "set-sink-volume", "0", "-5%"])
        playsound.playsound("/usr/share/sounds/freedesktop/stereo/audio-volume-change.oga")
    if joystick.get_button(7):  # Right trigger
        subprocess.call(["pactl", "set-sink-volume", "0", "+5%"])
        playsound.playsound("/usr/share/sounds/freedesktop/stereo/audio-volume-change.oga")
