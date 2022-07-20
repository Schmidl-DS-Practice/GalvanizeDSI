-- Run solution queries after creating DATABASE: `pets` and TABLE: `pets`

-- Usage: 
    -- $ psql -U postgres pets
    -- pets=# \i breakout2_solutions

-- BREAKOUT 2
-- 1: Owners and the number of pets they own
\echo '#1'
SELECT
    owner,
    COUNT(*)
FROM
    pets
GROUP BY
    owner;

-- 2: Owners and the count of each species of pet
\echo '#2'
SELECT
    owner,
    species,
    COUNT(*)
FROM
    pets
GROUP BY
    owner,
    species
ORDER BY
    owner;

-- 3: Count of pets by gender and species
\echo '#3'
SELECT
    species,
    gender,
    COUNT(*)
FROM
    pets
GROUP BY
    species,
    gender;

-- 4: All owners who own two or more cats
\echo '#4'
SELECT 
    owner,
    COUNT(*) AS num_of_cats
FROM
    pets
WHERE 
    species = 'cat'
GROUP BY
    owner
HAVING 
    COUNT(*) >= 2;



    
