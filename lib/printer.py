'''
Simplify colorized terminal output
'''


class MyPrint:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def print_wrn(self, text):
        print(self.WARNING + text + self.ENDC)

    def print_ok(self, text):
        print(self.OKGREEN + text + self.ENDC)

    def print_crit(self, text):
        print(self.FAIL + text + self.ENDC)

    def print_plain(self, text):
        print(text)

    def print_blue(self, text):
        print(self.OKBLUE + text + self.ENDC)
