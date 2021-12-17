import random


class TempSensor:
    index = 0

    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def update_index(self):
        self.index = random.randint(1, 110)
        self.notify_observers(self.index)


class TempMode:

    def __init__(self):
        self.strategy = NormalMode()

    def update(self, message):
        self.index = message
        self.setStrategy()

    def setStrategy(self):
        if self.index < 30:
            self.strategy = SafeMode()
        elif 30 <= self.index < 60:
            self.strategy = NormalMode()
        else:
            self.strategy = HardMode()

    def strategy_info(self):
        self.strategy.info()


class NormalMode:

    def info(self):
        print('Нормальный режим работы')


class SafeMode:

    def info(self):
        print('Сберегающий режим работы')


class HardMode:

    def info(self):
        print('Усиленный режим работы')


if __name__ == '__main__':
    mode = TempMode()
    app = TempSensor()
    app.register(mode)

    app.update_index()
    mode.setStrategy()
    mode.strategy_info()
