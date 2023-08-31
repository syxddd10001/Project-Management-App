import projects
class User:
    
    def __init__(self, id, username, email, github, password):
        self.id = id
        self.__username = username
        self.__email = email
        self.__github = github
        self.__password = password

        self.__projects = []
    
    def add_project(self, cursor, name, github, description):
        cursor.execute("""
                       INSERT INTO Project (name, github, description, creator_id) 
                            VALUES (
                                '%s',
                                '%s',
                                '%s',
                                %d
                            );""" % (name, github, description, self.id))

    def read_projects(self, cursor):
        cursor.execute("""
                        SELECT * FROM Project
                        WHERE Project.creator_id = %d;
                       """ % (self.id))
        result = cursor.fetchall()
        return result
        

    def get_projects(self):
        return self.__projects

    def get_username(self):
        return self.__username;

    def verify_password(self, username, password):
        return self.__username == username and self.__password == password
    
    def change_password(self, new_password):
        self.__password = new_password
    
    
    