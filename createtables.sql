-- create a sql table of the following attributes
-- Name: string
-- State: string
-- Salary: integer
-- Grade: integer
-- Room: integer
-- Telnum: string
-- Picture: string
-- Keywords: string

--  Write for microsft SQL server
--  Create an id which is primary key

CREATE TABLE Employees
(
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50),
    State VARCHAR(50),
    Salary INT,
    Grade INT,
    Room INT,
    Telnum VARCHAR(50),
    Picture VARCHAR(50),
    Keywords VARCHAR(50)
);


-- Dhruvi	TX	99099	100	550	1000010	dhru.jpg	Dhruvi is nice
-- Chuck	TX	1000	98	420		chuck.jpg	Chuck is amazing
-- Meena	TX	125000	99			 	Meena is outa here
-- Dave	NN	20	40	525	0	dave.jpg	Who is this
-- Tuan	CA		80	-1		 	Tuan is gone
-- Tavo	CA	220200	 			tavo.jpg	Tavo works very hard
-- Nora	TX	-1	80	520	808	 	
-- Sue	NN	 	79	0	2723785	upset.jpg	Sue isn't Susan
-- Susan	OK	255000	84	101	911	 	Susan is very smart
-- Darwin	TN	25	100		1009	dar.jpg	Darwin is very creative
-- Insert above data into database

INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Picture, Keywords) VALUES ('Dhruvi', 'TX', 99099, 100, 550, '1000010', 'dhru.jpg', 'Dhruvi is nice');
INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Picture, Keywords) VALUES ('Chuck', 'TX', 1000, 98, 420, '', 'chuck.jpg', 'Chuck is amazing');
INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Keywords) VALUES ('Meena', 'TX', 125000, 99, 0, '', 'Meena is outa here');
INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Picture, Keywords) VALUES ('Dave', 'NN', 20, 40, 525, '0', 'dave.jpg', 'Who is this');
INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Keywords) VALUES ('Tuan', 'CA', 0, 80, -1, '', 'Tuan is gone');
INSERT INTO Employees (Name, State, Salary, Grade, Telnum, Picture, Keywords) VALUES ('Tavo', 'CA', 220200, 0, 0, 'tavo.jpg', 'Tavo works very hard');
INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Keywords) VALUES ('Nora', 'TX', 0, 79, 520, '808', '', 'Nora isnt Susan');
INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Picture, Keywords) VALUES ('Sue', 'NN', 0, 79, 2723785, 'upset.jpg', 'Sue isnt Susan');
INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Keywords) VALUES ('Susan', 'OK', 255000, 84, 101, '911', 'Susan is very smart');
INSERT INTO Employees (Name, State, Salary, Grade, Room, Telnum, Picture, Keywords) VALUES ('Darwin', 'TN', 25, 100, 1009, 'dar.jpg', 'Darwin is very creative');

