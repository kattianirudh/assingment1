def get_sql_data(cursor):
    cursor.execute("SELECT * FROM Employees")
    data = cursor.fetchall()
    print(data)
    return data
    