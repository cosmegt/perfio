#pacman.py - Package Manager
#Things that have to be done:
        #Check if packages installed
        #If they're not installed, install them
        #Delete pacakges after we're done with them?
        #Check the distribution of this system
#See LICENSE

import subprocess
import os
import platform
from .run import Run

class Pacman():
        def __init__(self):
                '''How a program will be stored
                        self._programs = [ { name: packagename, path: path, args: [arr] } 
                '''
                #They start empty
                self._programs  = [] 
                self._distro    = platform.linux_distribution()
                self._manager   = ""

        # ---- Setters \ Getters ----
        @property
        def manager(self):
                return self._manager
        @manager.setter
        def manager(self, value):
                self._manager = value
        
        # For the programs, there has to be an object define, leave blank for now.
        

        # ---- OS Queries ----
        def check_installed(self, program):
                program = Run.return_all("which " + program)
                if program:
                        return program
                else:
                        return False

        
        def check_manager(self):
                result = ""
                if "CentOS" in self._distro[0]:
                        result = "yum"
                else:
                        exit("Unsupported Linux distribution.")
                print(result)
                self._manager = result



        def sanity(self):
                # Check if root
                if os.geteuid() != 0:
                        exit("You need to have root privilages to run this program. \nPlease try again using sudo. Exiting.")
                        
                # Check the package manager
                manager = self.check_manager()

                # Check necessary packages are installed, if not install them
                fio = self.check_installed("fio")
                smartctl = self.check_installed("smartctl")
