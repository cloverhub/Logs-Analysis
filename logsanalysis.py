#!/bin/env python2.7

import psycopg2
from datetime import datetime

dbname = "news"


def logs_analysis():
    # Connect to the database
    db = psycopg2.connect(database=dbname)

    # Open a cursor to execute PostgreSQL queries in the database session
    c = db.cursor()

    # Question 1. What are the most popular three articles of all time?
    # This PostgreSQL query joins the articles table with the log table
    # on the slug by deriving an equivalent slug from the article path
    # and fetches the top 3 rows of popular articles
    query = """
        select A.title, count(L.slug) as count
        from articles A
        inner join (select replace(path, '/article/', '') as slug from log) L
        on A.slug = L.slug
        group by A.title
        order by count desc
        fetch first 3 rows only;
    """
    c.execute(query)
    rows = c.fetchall()

    print('\n' + "Three most popular three articles of all time:")

    for (title, views) in rows:
        print(" \"{}\" - {} views".format(title, views))

    # Question 2. Who are the most popular article authors of all time?
    # This PostgreSQL query joins the articles and authors tables
    # to list authors by order of total article count
    query = """
        select W.name, count(L.slug) as count
        from articles A
        inner join ( select replace(path, '/article/', '') as slug from log ) L
        on A.slug = L.slug
        inner join authors W
        on A.author = W.id
        group by W.name
        order by count desc;
    """
    c.execute(query)
    rows = c.fetchall()

    print('\n' + "Most popular authors of all time:")

    for (name, count) in rows:
        print(" {} - {} views".format(name, count))

    # Question 3. On which days did more than 1% of requests lead to errors?
    # This PostgreSQL query groups log entries by http status code
    # and caculates a percentage if daily errpr rate exceeds 1%
    query = """
        select date(time),
        round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)
        /count(log.status),2) as error_rate
        from log
        group by date(time)
        having round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)
        /count(log.status),2) > 1;
    """
    # Use the datetime module to format the sql output of the date
    fmt = "%B %d, %Y"
    c.execute(query)
    rows = c.fetchall()

    print('\n' + "Day(s) on which more than 1% of requests led to errors:")

    for (date, rate) in rows:
        print(" {} - {}% errors".format(datetime.strftime(date, fmt), rate))

    # Close the cursor and the database session
    c.close()
    db.close()


logs_analysis()
