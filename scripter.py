import keyboard

class Scripter():
    def __init__(self, hotkey='\\', init=None):
        self.scriptRunning = True
        self.running = False
        self.init = init

        keyboard.add_hotkey(hotkey, self.toggleScript)
        keyboard.add_hotkey('`', self.killScript)

    def killScript(self):
        self.scriptRunning = False

    def toggleScript(self):
        if self.init and not self.running:
            self.init()
        self.running = not self.running

    def run(self):
        while self.scriptRunning:
            if (self.running):
                self.update()

    def update(self):
        raise Exception('not implemented')

def run(fn, init=None):
    script = Scripter('\\', init)

    def update():
        fn()

    script.update = update
    script.run()