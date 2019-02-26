## python-postgress

- Install pip dependencies.

```command
pip install -r requirements.txt
```

- Create a Postgres database on Digitalocean. There you will get Database name, Username, Password, Host, Password. Note down these things for your database connection.

- In `app.py`, update the database, username, password, host and port with the data you get from the Digitalocean.

```
conn = psycopg2.connect(database = "*****", user = "*****", password = "********", host = "*********-digitalocean.com", port = "25060")
```

- Once you update the database connection information. Run python program. 

```command
python app.py
```

If it shows output like `Opened database successfully`, it means you have successfully connected to the DB.
