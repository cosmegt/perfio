#gui.py - Graphical User Interface
#Things that have to be done:
    #Menu
    #Navigate through menu
    #Use checkboxes for selection (maybe)
    #Back button
#From what the application should do: 
    #
    

import sys
import os
import curses

class Gui():
    def __init__(self):
        '''Haven't really thought this through all the way'''
        self._active = True
        self._coord = []

    def g_main(self, stdsrc: 'curses_CursesWindows') -> int:
        #curses settings
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)


        # rendering phase
        while  True:
            char = stdsrc.get_wch()


        return 0


    def start(self) -> int:
        return curses.wrapper(self.g_main)
    