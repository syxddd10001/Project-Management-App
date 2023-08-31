-- @block
CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    username VARCHAR(64) NOT NULL UNIQUE, 
    email VARCHAR(255) NOT NULL UNIQUE, 
    password VARCHAR(64) NOT NULL
);
-- @block
CREATE TABLE IF NOT EXISTS Project(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    github MEDIUMTEXT default NULL,
    description MEDIUMTEXT,
    
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
CREATE TABLE IF NOT EXISTS ProjectAdmins(
    project_id INT NOT NULL,
    admin_id INT NOT NULL, 
    FOREIGN KEY (project_id) REFERENCES Project(id),
    FOREIGN KEY (admin_id) REFERENCES User(id),
    UNIQUE (project_id, admin_id)
);


-- @block
INSERT INTO Project (name, description, creator_id)
VALUES (
    'project1',
    'simple project!',
    1
);
-- @block
INSERT INTO ProjectAdmins (project_id, admin_id)
VALUES (
    1,
    1
); 
-- @block
SELECT * FROM User;
-- @block
SELECT * FROM Project;

SELECT * FROM ProjectAdmins;
