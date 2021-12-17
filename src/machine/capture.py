#capture.py
#Things that have to happen:
        #Check that FIO is installed
        #Create a way to call FIO
#See LICENSE

import subprocess
from .run import Run

class Capture():
        def __init__(self):
                '''How a program will be stored
                        self.__packagename = [
                        name: packagename
                        path: path
                        args: [arr]
                '''
                #They start empty
                self.__fio = [] 
                self.__smart = []


        # ---- OS Queries ----
        def check_installed(self, program):
                which = "/usr/bin/which"
                program = Run.return_all("which {program}")
                if program.find(which) != -1:
                        return True
                else:
                        return False






        




        def sanity(self):
                fio = self.check_installed("fio")
                smartctl = self.check_installed("smartctl")
                print(fio, smartctl)
