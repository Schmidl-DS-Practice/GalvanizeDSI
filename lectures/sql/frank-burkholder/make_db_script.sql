/*  
PostgreSQL port of the tables in 
Introduction to SQL for Data Scientists by Ben Smith
*/

-- One-line comment

/*
This is
a comment
block
*/

-- Start a transaction (series of commands)
BEGIN;

-- Create the tables

CREATE TABLE student                               (
    id      integer         PRIMARY KEY,
    name    text            NOT NULL
);


CREATE TABLE term_gpa                              (
    id      integer         REFERENCES student (id),
    term    integer         NOT NULL,
    gpa     numeric(3,2)    NOT NULL,
    PRIMARY KEY(id, term)
);


CREATE TABLE degrees                               (
    id      integer         REFERENCES student (id),
    term    integer         NOT NULL,
    degree  character(5)    NOT NULL,
    PRIMARY KEY(id, degree)
);


/* 
Fill the tables with data.
You will have to modify the paths to where
the data files are.
*/


COPY student(id,name)
FROM '/home/frank/galvanize/lectures_dsi/sql/frank/SQL_halfday/data/student_data.csv' 
DELIMITER ',' CSV HEADER;

COPY term_gpa(id,term,gpa)
FROM '/home/frank/galvanize/lectures_dsi/sql/frank/SQL_halfday/data/term_gpa_data.csv' 
DELIMITER ',' CSV HEADER;

COPY degrees(id,term,degree)
FROM '/home/frank/galvanize/lectures_dsi/sql/frank/SQL_halfday/data/degrees_data.csv' 
DELIMITER ',' CSV HEADER;


/*
-- Set PRIMARY and FOREIGN KEYS - could do it here too

ALTER TABLE ONLY student
    ADD CONSTRAINT student_id PRIMARY KEY (id);

*/

COMMIT;
-- End the transaction with the COMMIT and no this is not git

ANALYZE VERBOSE student;
ANALYZE VERBOSE term_gpa;
ANALYZE VERBOSE degrees;
