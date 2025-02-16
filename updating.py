import mysql.connector

def insertProduct(name,price,imageUrl,destription):
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "123456789",database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,destription)

    cursor.execute(sql,values)
    

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("'hata",err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı")

def insertProducts(list):
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "123456789",database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)
    

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("'hata",err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı")        

def getProducts():
    connection = connection = mysql.connector.connect(host = "localhost",user = "root",password = "123456789",database = "node-app")
    cursor = connection.cursor()

    #cursor.execute('Select * From Products')
    cursor.execute('Select name,price From Products')

    # result = cursor.fetchall() # birden fazla kayıt almak istersek 
    result = cursor.fetchone()
    print(f'name : {result[0]} price : {result[1]}')

    # for product in result:
    #     # print(f'name : {product[1]} price : {product[2]}')
    #     print(f'name : {product[0]} price : {product[1]}')

def getProductsById():
    connection = connection = mysql.connector.connect(host = "localhost",user = "root",password = "123456789",database = "node-app")
    cursor = connection.cursor()

    sql= "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id : {result[0]} name : {result[1]} price : {result[2]}')

def updateProduct(id,name,price):
    connection = connection = mysql.connector.connect(host = "localhost",user = "root",password = "123456789",database = "node-app")
    cursor = connection.cursor()


    sql= "Update products Set name = %s , price = %s where id = %s"
    values =  (name,price,id)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt güncellendi')
        
    except mysql.connector.Error as err:
        print("'hata",err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı")

updateProduct(1, 'Iphone 8',6000)
getProducts()
