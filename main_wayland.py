import subprocess
import pyautogui as pag
import os
import pygame

pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]


try:
    joystick = joysticks[0]
except IndexError:
    raise Exception("You must have a controller connected!")


pag.FAILSAFE = True
SPEED = 10
# pag.PAUSE = 1

coordinate = [pag.size()[0] / 2, pag.size()[1] / 2]
move_by = [0, 0]
start_joy_lockup = False
mouse_down = False


while True:
    pygame.time.Clock().tick(60)
    move_by = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEREMOVED:
            print("Removed Joystick.")
        if event.type == pygame.JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            joystick = joysticks[0]
            print("Added Joystick!")

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 6:  # Left trigger
                subprocess.call(["ydotool", "key", "114:1", "114:0"])
            if event.button == 7:  # Right trigger
                subprocess.call(["ydotool", "key", "115:1", "115:0"])

            if event.button == 13:  # Up
                # pag.scroll(3)
                subprocess.call(["ydotool", "mousemove", "-w", "0", "2"])
            if event.button == 14:  # Down
                subprocess.call(["ydotool", "mousemove", "-w", "--", "0", "-2"])
                # pag.scroll(-3)

            if event.button == 16:  # Right
                subprocess.call(["ydotool", "type", "f"])
                pag.typewrite("f")
            if event.button == 9:  # Start
                # Ctrl t
                subprocess.call(["ydotool", "key", "29:1", "20:1", "20:0", "29:0"])
                subprocess.call(["ydotool", "type", "youtube.com"])
                # Enter
                subprocess.call(["ydotool", "key", "28:1", "28:0"])
            if event.button == 8:  # Select
                # pag.hotkey("ctrl", "r")
                subprocess.call(["ydotool", "key", "29:1", "19:1", "19:0", "29:0"])

    # Get both axes of the right stick
    axis = joystick.get_axis(3)
    axis2 = joystick.get_axis(4)

    if axis > .2:
        coordinate[0] += axis * SPEED
        if coordinate[0] > pag.size()[0]:
            coordinate[0] = pag.size()[0] - 5
        move_by[0] = axis * SPEED
    elif axis < -.2:
        coordinate[0] += axis * SPEED
        if coordinate[0] < 0:
            coordinate[0] = 5
        move_by[0] = axis * SPEED

    if axis2 > .2:
        coordinate[1] += axis2 * SPEED
        if coordinate[1] > pag.size()[1]:
            coordinate[1] = pag.size()[1] - 5
        move_by[1] = axis2 * SPEED
    elif axis2 < -.2:
        coordinate[1] += axis2 * SPEED
        if coordinate[1] < 0:
            coordinate[1] = 5
        move_by[1] = axis2 * SPEED

    if joystick.get_button(15):  # Left arrow
        if not mouse_down:
            subprocess.call(["ydotool", "click", "0x00", "0x40"])
            mouse_down = True
    else:
        if mouse_down:
            subprocess.call(["ydotool", "click", "0x00", "0x80"])
            mouse_down = False

    if joystick.get_button(4):  # L1
        SPEED -= 1
        if SPEED < 0:
            SPEED = 0

    if joystick.get_button(5):  # R1
        SPEED += 1

    if joystick.get_button(0):  # Cross
        raise SystemExit(0)

    # if joystick.get_button(10):  # PS
    #       pass

    subprocess.call(["ydotool", "mousemove", "-x", f"{move_by[0]}", "-y", f"{move_by[1]}"])
