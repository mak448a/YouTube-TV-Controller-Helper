import subprocess
import pyautogui as pag
import os
import pygame

pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
os.system("ydotoold &")

try:
    joystick = joysticks[0]
    print(joysticks)
except IndexError:
    raise Exception("You must have a controller connected!")


pag.FAILSAFE = True
SPEED = 40
# pag.PAUSE = 1

coordinate = [pag.size()[0] / 2, pag.size()[1] / 2]
move_by = [0, 0]
start_joy_lockup = False

while True:
    pygame.time.Clock().tick(120)
    move_by = [0, 0]
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
        # subprocess.call(["ydotool", "mousemove", "-x", f"{axis * SPEED}", "-y", "0"])
        if coordinate[0] > pag.size()[0]:
            coordinate[0] = pag.size()[0] - 5
        move_by[0] = axis * SPEED
    elif axis < -.2:
        coordinate[0] += axis * SPEED

        # subprocess.call(["ydotool", "mousemove", "-x", f"{axis * SPEED}", "-y", "0"])
        if coordinate[0] < 0:
            coordinate[0] = 5
        move_by[0] = axis * SPEED

    if axis2 > .2:
        coordinate[1] += axis2 * SPEED
        if coordinate[1] > pag.size()[1]:
            coordinate[1] = pag.size()[1] - 5
        move_by[1] = axis2 * SPEED
        # subprocess.call(["ydotool", "mousemove", "-y", f"{axis2 * SPEED}", "-x", "0"])
    elif axis2 < -.2:
        coordinate[1] += axis2 * SPEED
        if coordinate[1] < 0:
            coordinate[1] = 5
        move_by[1] = axis2 * SPEED

        # subprocess.call(["ydotool", "mousemove", "-y", f"{axis2 * SPEED}", "-x", "0"])

    if joystick.get_button(15):  # Left arrow
        subprocess.call(["ydotool", "click", "0x00", "0x40"])

    else:
        subprocess.call(["ydotool", "click", "0x00", "0x80"])

    if joystick.get_button(4):  # L1
        SPEED -= 1
        if SPEED < 0:
            SPEED = 0
        pass
    if joystick.get_button(5):  # R1
        SPEED += 1
        pass
    print(SPEED)
    if joystick.get_button(13):  # Up
        pag.scroll(3)
        subprocess.call(["ydotool", "mousemove", "-w", "0", "1"])
    if joystick.get_button(14):  # Down
        print("test")
        subprocess.call(["ydotool", "mousemove", "-w", "--", "0", "-1"])
        # pag.scroll(-3)

    if joystick.get_button(0):  # Cross
        raise SystemExit(0)

    if joystick.get_button(16):  # Right
        pag.typewrite("f")
    if joystick.get_button(9):  # Start
        if not start_joy_lockup:
            start_joy_lockup = True
            # Ctrl t
            subprocess.call(["ydotool", "key", "29:1", "20:1", "20:0", "29:0"])
            subprocess.call(["ydotool", "type", "youtube.com"])
            # Enter
            subprocess.call(["ydotool", "key", "28:1", "28:0"])
    else:
        start_joy_lockup = False
    if joystick.get_button(10):  # PS
        pag.hotkey("ctrl", "r")
    if joystick.get_button(8):  # Select
        pag.hotkey("win", "2")

    if joystick.get_button(6):  # Left trigger
        pag.press("volumedown")
    if joystick.get_button(7):  # Right trigger
        pag.press("volumeup")

    subprocess.call(["ydotool", "mousemove", "-x", f"{move_by[0]}", "-y", f"{move_by[1]}"])
    # pag.moveTo(coordinate)
