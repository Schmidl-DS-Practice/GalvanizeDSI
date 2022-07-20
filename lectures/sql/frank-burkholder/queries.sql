/*
Implementing queries from
Introduction to SQL for Data Scientists
*/

-- Look at the tables and data shown in Section 1.2

/* 
Query 0: Paste the query below into the psql interactive
shell (or type \i queries.sql in the shell).
It should give the results of the first query
in Section 2 of the paper.
*/

SELECT
    s.id AS id,
    s.name AS name
FROM
    student AS s
WHERE
    s.id = 1;


/*
Query 1: Write a query that will return the
students whose first name starts with an H.
*/










/*
Query 2: Write a query that returns what terms degrees were 
awarded.
*/








/*
Query 3: Write a query that counts the number of times a term
g.p.a. was above 3.
*/













-- Back to lecture

/*
Query 4: Paste this query that uses a join to 
duplicate the second set of results in Section 2 of the paper.
It shows the student id, name, and gpa for student 1 and
term 2012.
*/

SELECT
    s.id AS id,
    s.name AS name,
    t.gpa AS gpa
FROM
    student AS s
JOIN
    term_gpa AS t
ON
    s.id = t.id
WHERE
    s.id = 1
    AND
    t.term = 2012;

/*
Query 5: Write a query that will find and display Edith Warton's 
and Henry James's gpas for 2011 and 2012.
*/












/* Query 6: Write a query that will find Edith Warton's and Henry 
James's highest gpas rounded to one decimal place.  Order them by 
whoever has the highest gpa.
*/













/* 
Query 7: In one table list all the students, the term they were 
enrolled, their gpa for that term, and the degree they received 
(if they received one).  Consider using a left join here.
*/















-- Extra credit
/* 
Find the students who have graduated (they have their
degree). Consider using GROUP BY.
*/








/*
Find the students who haven't graduated and their average 
gpa, rounded to one decimal place. You may want to use a subquery.
*/


















