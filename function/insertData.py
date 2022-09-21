import pyodbc
import os

try:
    # データベースに接続
    # 現在のディレクトリ取得
    #現在のディレクトリの前のディレクトリにあるので、パスの処理が必要
    cwd = os.getcwd()
    print(cwd)

    #DB接続
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        f'DBQ={cwd}\hanbai.mdb;'
        )

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print('接続OK！')
    #sql文についてもsyntaxerrorになるのでそこをどこで処理するか
    #以下のsqlであればinsert可能　0921確認済み
    sql ="INSERT INTO リソーステスト VALUES('PSV131', 934, 20220921, 230000, 0, 0, 0, 0, 25555, 66103, 17669, 33531, 7039, 18430, 730, 14596, 9502, 10848, 0, 0);"
#     cursor.execute(sql)
#     cursor.commit()
    
#     cursor.close()
#     #接続閉じる
#     conn.close()
    
    print('データの登録が完了しました')

except SyntaxError as err:
    print(err)
    print('エラー：データベースに接続できませんでした')