import config

try:
    f = open('config.ini')

except FileNotFoundError:
    config.init()


