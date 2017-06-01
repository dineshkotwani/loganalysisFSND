#!/usr/bin/env python

import psycopg2
import sys

DBNAME = "news"


def get_popular_posts():
    """Return  top 3 most popular articles from news database."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT title,reads from popularposts")
    return c.fetchall()
    db.close()


def get_popular_authors():
    """Return top 3 most popular authors from the news database."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT name,viewcounts from popularauthors")
    return c.fetchall()
    db.close()


def get_errorful_day():
    """Return all days from the news database where error percent was > 1 ."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT day,percent from failureday")
    return c.fetchall()
    db.close()


posts = get_popular_posts()

authors = get_popular_authors()

errordays = get_errorful_day()

outputfile = open("output.txt", 'w')

outputfile.write("Top 3 popular posts are : ")

for post in posts:
    outputfile.write("\n")
    outputfile.write(post[0] + " -- " + str(post[1]) + " views")
    print post[0] + " -- " + str(post[1]) + " views"

outputfile.write("\n")
outputfile.write("\n")
outputfile.write("Top 3 popular authors are : ")

for author in authors:
    outputfile.write("\n")
    outputfile.write(author[0] + " -- " + str(author[1]) + " views")
    print author[0] + " -- " + str(author[1]) + " views"

outputfile.write("\n")
outputfile.write("\n")
outputfile.write("Days where error percent of requests was greater than 1% : ")

for errorday in errordays:
    outputfile.write("\n")
    outputfile.write(
        errorday[0].strftime("%Y-%m-%d") + "-" + str(errorday[1]) + "%"
        )
    print errorday[0].strftime("%Y-%m-%d") + " -- " + str(errorday[1]) + "%"

outputfile.close()
