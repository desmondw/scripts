import keyboard

class TorchlightScripter():
    def __init__(self, hotkey='\\'):
        self.scriptRunning = True
        self.running = False

        keyboard.add_hotkey(hotkey, self.toggleScript)
        keyboard.add_hotkey('esc', self.killScript)

    def killScript(self):
        self.scriptRunning = False

    def toggleScript(self):
        self.running = not self.running

    def run(self):
        while self.scriptRunning:
            if (self.running):
                self.update()

    def update(self):
        raise Exception('not implemented')

def run(fn):
    script = TorchlightScripter('\\')

    def update():
        fn()

    script.update = update
    script.run()