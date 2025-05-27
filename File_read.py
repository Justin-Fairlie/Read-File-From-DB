import mysql.connector
import os


conn = mysql.connector.connect(
    host='localhost',
    port=3308,
    user='root',
    password='2003',
    database='ignition'
)
cursor = conn.cursor()


file_id = 1 
cursor.execute("SELECT fileName, fileBytes FROM file WHERE id = %s", (file_id,))
result = cursor.fetchone()

if result:
    filename, file_data = result
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", filename)
    with open(downloads_path, 'wb') as f:
        f.write(file_data)
    print(f"File '{filename}' downloaded to your Downloads folder.")
else:
    print("File not found.")

cursor.close()
conn.close()