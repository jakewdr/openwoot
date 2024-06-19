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

def unpackCfg(cfgFile: str) -> dict[str, str]:  # This is gonna assume that the the headers of the table are vertical
    with open(cfgFile) as cfgContents:
        return dict([line.split("=", 1) for line in [line.strip("\n") for line in cfgContents if "=" in line.strip()]])  # The if is needed due to a bug where the process would fail due to an empty line in the config

if __name__ == "__main__":
    print("Running, edit config in settings.cfg and close the window to stop the program")
    cfg = unpackCfg("settings.cfg")
    
    key1 = cfg.get("key1")
    key2 = cfg.get("key2")
    if cfg.get("rappySnappy").lower() == "true":
        keyboard.on_press(onKeyPress)
        keyboard.on_release(onKeyRelease)
        keyboard.wait()
