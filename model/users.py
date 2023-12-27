from projects import Project
class User:
    
    def __init__(self, id, username, email, github, password):
        self.__id = id
        self.__username = username
        self.__email = email
        self.__github = github
        self.__password = password
        self.__projects = []
    
    def get_id(self):
        return self.__id

    def add_project(self, cursor, name, github, description):
        cursor.execute("""
                       INSERT INTO Project (name, github, description, creator_id) 
                            VALUES (
                                '%s',
                                '%s',
                                '%s',
                                %d
                            );""" % (name, github, description, self.__id))
        
    def read_projects_from_server(self, cursor):
        self.__projects = []
        cursor.execute("""
                        SELECT * FROM Project
                        WHERE Project.creator_id = %d;
                       """ % (self.__id))
        result = cursor.fetchall()
        return result
    
    def read_projects(self, cursor):
        all_projects = []
        project_data = self.read_projects_from_server(cursor)
        for project in project_data:
            proj = Project(project[0], project[1], project[2], project[3], project[4])
            all_projects.append(proj)
            self.__projects.append(proj)
        return all_projects
        
    def get_projects(self):
        return self.__projects

    def get_username(self):
        return self.__username;

    def get_allinfo(self):
        info = [self.__id, self.__username, self.__github, self.__projects]
        return info

    def verify_password(self, username, password):
        return self.__username == username and self.__password == password
    
    def change_password(self, new_password):
        self.__password = new_password
    
    
    