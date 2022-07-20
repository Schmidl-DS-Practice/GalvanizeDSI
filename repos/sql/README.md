# Structured Query Language (SQL)

## Learning Objectives

* Creating and populating a DB
* Query primer
* Filtering
* Querying multiple tables
* Working with sets
* Grouping and Aggregates

## Introduction

Structured Query Language (SQL for short) is the bread and butter of a working data scientist. Whether generating reports, grabbing data for a machine learning model, or implementing a data product — SQL is one of the most important skills to master during this course. In this sprint, we'll be gaining familiarity with SQL fundamentals. We'll start with basic querying, and move on to joins, aggregations, subqueries, and working with sets. 

## Primer

First off, read through [SQL for Data Scientists](http://bensresearch.com/downloads/SQL.pdf)  and become familiar with basic SQL commands, inner and outer joins, and basic grouping and aggregation functions.

We will be using [Postgres SQL](http://www.postgresql.org/) in this exercise, a flavor of SQL that is quickly becoming _de rigueur_ in web startups and big companies alike. Postgres is fast, scales well, and comes with a bunch of useful extensions such as [PostGIS](http://postgis.net/) for working with geographical data.

While Postgres adheres to the ANSI 92 SQL standard, there are a few extra functions implemented that we'll be using in later sprints. Check out the the Postgres [tutorial](http://www.postgresqltutorial.com/) for an overview of the provided functions. This will give you a basic overview of the syntax and will be your reference going forward.

## Assignment

In the [exercise for today](assignment.md), you'll be using the interactive SQL shell from the console for most of your work. Once you have a satisfactory answer to a question, remember to copy your SQL query to a text file for safe keeping. You'll submit all your finished queries at the end of the day as a pull request. Remember: _Commit Early, Commit Often_

## Extra Credit:

Go through some useful SQL examples for data science from yhat's blog: [SQL for Data Scientists](http://blog.yhathq.com/posts/sql-for-data-scientists.html)

## References

* [ModeAnalytics: SQL School](http://sqlschool.modeanalytics.com/)
* [7 Handy SQL features for Data Scientists](http://blog.yhathq.com/posts/sql-for-data-scientists.html)
* [Postgres Docs](http://www.postgresql.org/docs/7.4/static/tutorial.html)
* [Postgres Guide](http://postgresguide.com/)
* [Statistics in SQL](https://github.com/tlevine/sql-statistics)
* [A Gentle Introduction to SQL Using SQLite](https://github.com/zipfian/SQL-Tutorial)
* [The fast-track, hands-on, no-nonsense introduction to SQL](https://github.com/dserban/WebDevCourseMaterials/tree/master/1-intro-to-sql)
* [Intro to SQL](http://bensresearch.com/downloads/SQL.pdf)

### Joins

* [Visual Explanation of Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)
* [SQL Joins](https://chartio.com/education/sql/joins)
