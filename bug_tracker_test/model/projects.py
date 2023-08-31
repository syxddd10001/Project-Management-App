import numpy as np
import bugs


class Project:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__bugs = []
    '''
    def get_name(self):
        return self.__name

    def get_bugs(self):
        return self.__bugs

    def add_bug(self, bug):
        if type(bug) != bugs.Bug:
            return

        self.__bugs.append(bug)

    def de_bug(self, bug):
        if type(bug)!=bugs.Bug:
            return  
        self.__bugs.remove(bug)
                
    def rename_project(self, rename):
        self.__name = rename
    '''

   

    

    

    