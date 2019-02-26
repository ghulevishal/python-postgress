#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database = "mydb", user = "doadmin", password = "********", host = "*********-digitalocean.com", port = "25060")

print ("Opened database successfully")
