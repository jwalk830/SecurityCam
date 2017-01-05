import LCD1602


class LCD:
    def __init__(self):
        LCD1602.init(0x27, 1)   # init(slave address, background light)
        LCD1602.write(0, 0, 'Security Cam')
        LCD1602.write(1, 1, 'Secure Up')

    def clear(self):
        LCD1602.clear()

    def write(self, line, message):
        LCD1602.write(line, line, message)
