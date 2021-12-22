#gui.py - Graphical User Interface
#Things that have to be done:
    #Start a menu
    #Navigate through menu
    #Use checkboxes for selection
    #
import sys
import os
import curses

class Gui():
    def __init__(self):
        '''Haven't really thought this through all the way'''
        self._active = True

    def g_main(self, stdsrc: 'curses_CursesWindows') -> int:
        # rendering phase
        while  True:
            char = stdsrc.get_wch()


        return 0


    def start(self) -> int:
        return curses.wrapper(self.g_main)
    