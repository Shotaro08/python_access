import sys
import os
import pyodbc

#リリースNO取得、最大値+1を返す
def getReleaseNum():
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

def selectdata(selectedList, date):
    
    #リリースNOの最大値取得
    releaseNum = getReleaseNum()
    
    #timeは固定
    time = 230000
    
    date = int(date)
    
    sqlList = []
    
    #sql文作成　項目数合わせているので、valueのみ
    # sql = 'INSERT INTO リソース(System, リリースNO, Date, Time, CPU使用率, メモリー使用量, 受信IPパケット, 送信IPパケット, ドライブC使用スペース,ドライブC残りスペース, ドライブD使用スペース, ドライブD残りスペース, ドライブF使用スペース, ドライブF残りスペース, ドライブG使用スペース, ドライブG残りスペース, ドライブH使用スペース, ドライブH残りスペース, ドライブI使用スペース, ドライブI残りスペース)'
    #テストのため別のテーブルで実施
    sql = 'INSERT INTO リソーステスト '
    try:
        for content in selectedList:
            if(len(content) == 13):
                value = f'VALUES("{content[0]}", {releaseNum}, {date}, {time}, 0, 0, 0, 0, {content[1]}, {content[2]}, {content[3]}, {content[4]}, {content[5]}, {content[6]}, {content[7]}, {content[8]}, {content[9]},{content[10]}, {content[11]}, {content[12]})'
                fullSql = sql + value 
                sqlList.append(fullSql)

            elif(len(content) == 11):
                value = f'VALUES("{content[0]}", {releaseNum}, {date}, {time}, 0, 0, 0, 0, {content[1]}, {content[2]}, {content[3]}, {content[4]}, {content[5]}, {content[6]}, {content[7]}, {content[8]}, {content[9]},{content[10]}, 0, 0)'
                fullSql = sql + value 
                sqlList.append(fullSql)
            else:
                raise OSError
                
    except OSError as err:
        print('エラー')
        print('テキストファイルの内容を再度確認してください。')
        input()
        sys.exit()
    
    return sqlList