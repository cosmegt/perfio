# main.py
#things that have to happen:                                     Code moves this direction
        #Check if packages are installed                -- pacman class         |
        #Begin user interface                           -- gui class            |
        #Use user input to generate a file              -- generator class      |
        #Feed file to FIO/etc                           -- feeder class         |
        #Parse FIO/etc... results to some html file     -- visualizer class     v
# See LICENSE
from machine.pacman import Pacman
from gui.gui import Gui

def main(): 
        #define all classes
        pacman  = Pacman()
        gui     = Gui()
        #OS sanity check
        pacman.sanity()

        #Start GUI
        gui.start()


if __name__ == "__main__":
    main()