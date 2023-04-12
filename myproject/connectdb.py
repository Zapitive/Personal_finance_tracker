import mysql.connector



def con():

    mydb = mysql.connector.connect(
    host="awseb-e-pmitpa3uv5-stack-awsebrdsdatabase-duuttamccnml.cp3iiv7x0jke.eu-north-1.rds.amazonaws.com",
    user="Zapitive",
    password="Yanarp11",
    database="pfinancetracker"
    )
    #mycursor = mydb.cursor()
    # id=1
    # password="Yanarp@11"
    # email="pranay@admin.com"
    # psw = sha256_crypt.encrypt(password)
    # #creating expense table
    # # mycursor.execute("CREATE TABLE expense (id INT AUTO_INCREMENT PRIMARY KEY, uid INT, username VARCHAR(255), expense VARCHAR(255),ex_date Date, category VARCHAR(255), note VARCHAR(255), currency VARCHAR(255), amount FLOAT)")
    # # mycursor.execute("CREATE TABLE userdetails (uid INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), username VARCHAR(255), pno VARCHAR(10), password VARCHAR(15)")
    # sql = "INSERT INTO admindetails (admin_id, a_email, a_pass) VALUES (%i, %s, %s)"
    # val = (id,email,psw)
    # mycursor.execute(sql, val)
    # print("admin added successfully")
    return mydb