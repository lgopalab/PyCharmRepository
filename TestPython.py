import mysql.connector
from mysql.connector import errorcode
from flask import Flask

print("Namaste Macha!")
print("endha chicha")

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()




try:
  cnx = mysql.connector.connect(user='root',password='123',
                                database='TEST')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:

  cursor = cnx.cursor()
  query = ("select sno,name from TEST");
  cursor.execute(query)

  for (sno, name) in cursor:
    print("{}, With Serial umber {}".format(name,sno))

  cursor.close()
  cnx.close()
  cnx.close()