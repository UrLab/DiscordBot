import time

ansi_codes = {
    "warning": "\33[41;30m",
    "start": "\33[105;30m",
    "command": "\33[44;30m",
    "reset": "\33[0m"
}


def log(type, message, *args):
    current_time = time.gmtime()
    print(f"{ansi_codes[type]}[{time.strftime('%H:%M:%S', current_time)}]{ansi_codes['reset']} {message}", *args)
