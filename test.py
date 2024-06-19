import keyboard

key1 = "z"
key2 = "x"

firstPressedKey = None


def onKeyPress(event):
    global firstPressedKey
    if event.name == key1 or event.name == key2:
        if firstPressedKey is None:
            firstPressedKey = event.name
        elif firstPressedKey != event.name:
            keyboard.release(firstPressedKey)
            firstPressedKey = event.name


def onKeyRelease(event):
    global firstPressedKey
    if event.name == firstPressedKey:
        firstPressedKey = None


keyboard.on_press(onKeyPress)
keyboard.on_release(onKeyRelease)

keyboard.wait()

