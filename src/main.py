# main.py
#things that have to happen:                                     Code moves this direction
        #Check if FIO/etc is installed & save to memory -- alien class          |
        #Begin user interface                           -- gui class            |
        #Use user input to generate a file              -- generator class      |
        #Feed file to FIO/etc                           -- feeder class         |
        #Parse FIO/etc... results to some html file     -- visualizer class     v
# See LICENSE
from machine.capture import Capture

def main(): 
        #define all classes
        capture = Capture()

        #OS sanity check
        capture.sanity()



if __name__ == "__main__":
    main()