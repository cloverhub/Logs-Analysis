# Project 3: Logs Analysis - Shawn Clover
This is project 3 for the Udacity Full Stack Nanodegree.

## What is Does
This program uses Python and PSQL to connect to an existing PostgreSQL database, run three queries, and output the results in plain-text to a user's terminal.

The output displays:
1. Three most popular three articles of all time
2. Most popular authors of all time
3. Day(s) on which more than 1% of requests led to errors

## Required Libraries and Dependencies
The following must be used:
- Python 2.*.
- Vagrant
- VirtualBox 5.x

## Files Included
- logsanalysis.py: A Python program that runs the logs analysis and outputs results in plain text
- README.md: you are here

## Instructions
1. Install VirtualBox 5.x and Vagrant
2. Download the database data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. Extract newsdata.sql to the vagrant directory
4. Run ```vagrant up```
5. Log in with ```vagrant ssh```
6. ```cd``` to the vagrant directory
7. Load the database into vagrant using ```psql -d news -f newsdata.sql```
8. Clone or download logsanalysis.py into the vagrant directory
9. Run ```logsanalysis.py```