# Read From DB
## Description
This repository contains two Python scripts designed to interact with a MySQL database. The first script, `file_read.py`, is used to retrieve a file stored in the database and save it to the user's local Downloads folder. The second script, `column_rename.py`, is used to rename a specific column in all tables of the database where it exists, ensuring consistency in column naming.

## Prerequisites
- Python 3.x: Ensure you have Python installed on your system.
- MySQL Server: A running instance of MySQL where your database is hosted.
- `mysql-connector-python` package: A Python package to connect to MySQL databases.

Install the required package using pip:
```bash
pip install mysql-connector-python
