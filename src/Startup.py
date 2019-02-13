from main import Main
from update import Updater

if __name__ == '__main__':
    Updater.update()
    main = Main()
    main.running = True
    main.main()