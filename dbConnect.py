#DB接続部分

import pyodbc
import os
import sys

def dbConnect():
    try:
        # 現在のディレクトリ取得
        cwd = os.getcwd()
        print(cwd)

        #DB接続
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            f'DBQ={cwd}\hanbai.mdb;'
            )

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        #SQL文
        #現在のデータのリリースNOの最大値を取得
        sql = 'SELECT MAX(リリースNO) FROM リソース'
        cursor.execute(sql)

        max = cursor.fetchval()

        cursor.close()
        #接続閉じる
        conn.close()

        #格納するデータのリリースNO
        releaseNum = max + 1

        return releaseNum
    
    except:
        print('エラー')
        print('hanbai.mdbファイルがみつかりません')
        input()
        sys.exit()

