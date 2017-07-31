from ConfigParser import SafeConfigParser

config = SafeConfigParser()

def init():
    config.read('config.ini')
    config.add_section('main')
    config.set('main','problem','0')

    with open('config.ini','w') as f:
        config.write(f)
    return

def read():
    config.read('config.ini')
    config.get('main','problem')