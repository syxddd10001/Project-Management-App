-- @block
CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    username VARCHAR(64) NOT NULL UNIQUE, 
    email VARCHAR(255) NOT NULL UNIQUE, 
    github VARCHAR(255) default NULL,
    password VARCHAR(64) NOT NULL
);

-- @block
CREATE TABLE IF NOT EXISTS Project(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    github VARCHAR(255) default NULL,
    description MEDIUMTEXT,
    creator_id INT NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES User(id),
    UNIQUE (name,creator_id)
);

-- @block
CREATE TABLE IF NOT EXISTS ProjectAdmins(
    project_id INT NOT NULL,
    admin_id INT NOT NULL, 
    FOREIGN KEY (project_id) REFERENCES Project(id),
    FOREIGN KEY (admin_id) REFERENCES User(id),
    UNIQUE (project_id, admin_id)
);
-- @block
CREATE TABLE IF NOT EXISTS ProjectUsers(
    project_id INT NOT NULL,
    users_id INT NOT NULL, 
    FOREIGN KEY (project_id) REFERENCES Project(id),
    FOREIGN KEY (users_id) REFERENCES User(id),
    UNIQUE (project_id, users_id)
);

-- @block
INSERT INTO User(username, email, github, password)
VALUES (
    'client',
    'client@domain.com',
    'github.com/client',
    'securedpassword'
);
-- @block
INSERT INTO Project (name, github, description, creator_id)
VALUES (
    'proj1',
    'github.com/proj1',
    'simple project!',
    2
);

-- @block
INSERT INTO ProjectAdmins (project_id, admin_id)
VALUES (
    2,
    4
); 

-- @block
SELECT * FROM User;
-- @block
SELECT * FROM Project;
-- @block
SELECT * FROM Project
INNER JOIN User
ON Project.creator_id = User.id;

-- @block 
SELECT * FROM Project
WHERE Project.creator_id=2;

-- @block
DELETE FROM User WHERE username="iq";

