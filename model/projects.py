import numpy as np
import bugs


class Project:
    def __init__(self, id, name, github, description, creator_id):
        self.__name = name
        self.__id = id
        self.__github = github
        self.__description = description
        self.__creator_id = creator_id
        self.__bugs = []
    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_github(self):
        return self.__github

    def get_description(self):
        return self.__description

    def get_creator_id(self):
        return self.__creator_id

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
    

   

    

    

    