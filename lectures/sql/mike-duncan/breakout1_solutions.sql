-- Run solution queries after creating DATABASE: `pets` and TABLE: `pets`

-- Usage: 
    -- $ psql -U postgres pets
    -- pets=# \i breakout1_solutions

-- BREAKOUT 1
-- 1: Owner(s) of Male pet(s)
\echo '#1:'
SELECT
    owner
FROM
    pets
WHERE
    gender ='M';

/* RESULT:
#1:
 owner 
-------
 Taryn
(1 row)
*/

-- 2: Names of dogs
\echo '#2:'
SELECT
    name
FROM
    pets
WHERE
    species = 'dog';

/* RESULT:
#2:
  name  
--------
 Bailey
 Kahlua
 Henley
(3 rows)
*/

-- 3: Names and ages of oldest 2 pets
\echo '#3:'
SELECT
    name,
    age
FROM
    pets
ORDER BY
    age DESC
LIMIT
    2;

/* RESULT:
#3:
  name  | age 
--------+-----
 Bailey |  11
 Belle  |  10
(2 rows)
*/

-- 4: The species of the youngest pet
\echo '#4:'
SELECT
    species
FROM
    pets
ORDER BY
    age
LIMIT 
    1;

/* RESULT:
#4:
 species 
---------
 cat
(1 row)
*/

-- 5: Names of cats that are 8 years old or younger
\echo '#5:'
SELECT
    name
FROM
    pets
WHERE 
    species = 'cat' AND
    age <= 8;

/* RESULT:
#5:
 name  
-------
 Max
 Daisy
 Salem
 Teeny
(4 rows)
*/

-- 6: Pets that are babies (<= 1 year) are expensive. Senior pets (>=8) can also be expensive.
--    Whos owns one or more expensive pets?
\echo '#6 with DISTINCT:'
SELECT
    DISTINCT(owner)
FROM
    pets
WHERE
    age <= 1 OR
    age >= 8;

/* RESULT:
#6 with DISTINCT:
 owner 
-------
 Megan
 Taryn
 Kyrie
(3 rows)
*/


\echo '#6 with GROUP BY:'
SELECT
    owner
FROM
    pets
WHERE
    age <= 1 OR
    age >= 8
GROUP BY
    owner;

/*RESULT:
#6 with GROUP BY:
 owner 
-------
 Megan
 Taryn
 Kyrie
(3 rows)
*/


    
