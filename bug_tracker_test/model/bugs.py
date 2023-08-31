from datetime import date, datetime


class Bug:
    def __init__(self, name, tracking_id, priority, description):
        self.__name = name
        self.__tracking_id = tracking_id
        self.__priority = priority
        self.__description = description
        self.__timestamp = datetime.now()

    '''
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def set_priority(self, priority):
        self.__priority = priority

    def get_priority(self):
        return self.__priority
    
    def same_id(self, other):
        return self.__tracking_id == other.__tracking_id

    def __lt__(self, other):
        return self.__priority < other.__priority
    
    def __eq__(self, other):
        return self.__priority == other.__priority
    
    def __gt__(self, other):
        return self.__priority > other.__priority
    '''
