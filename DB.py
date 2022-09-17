# DB接続部分
import pyodbc
import os

# 現在のディレクトリ取得
cwd = os.getcwd()
print(cwd)


# Microsoft Access へのDB接続
conn_str = (

    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'

    f'DBQ={cwd}\hanbai.mdb;'

)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


# SQL文 一旦selectでデータ操作できるかを確認
sql = 'SELECT * FROM リソース'
cursor.execute(sql)

list = []
for row in cursor.fetchall():
    list.append(row)

cursor.close()


# 接続閉じる
conn.close()


print(list[0])
input("入力待ち")
