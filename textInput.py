#取得したテキストから情報を抽出する
import re
import pprint as p
import function.data as d
import function.select as select

# ファイルからデータ取得
# 1行ずつ読み込む
f = open('DiskSizeResult.txt', 'r', encoding='CP932')
datalist = f.readlines()
f.close()

# 取得したデータを整理する
# data.py data()で処理
list = d.data(datalist)

selectedList = select.select(list)
#SQLで使用するデータになっている

#データ登録処理
#一旦400で設定（本当は最大値をとってくる）
num = 400
date = 20220920
time = 230000

#sql文作成　
sql = 'INSERT INTO リソース(System, リリースNO, Date, Time, CPU使用率, メモリー使用量, 受信IPパケット, 送信IPパケット, \
ドライブC使用スペース,ドライブC残りスペース, \
ドライブD使用スペース, ドライブD残りスペース, \
ドライブF使用スペース, ドライブF残りスペース, \
ドライブG使用スペース, ドライブG残りスペース,\
ドライブH使用スペース, ドライブH残りスペース, \
ドライブI使用スペース, ドライブI残りスペース)'


sql_access = []

#Iが入っているかどうか(要素数)で条件分岐
for content in selectedList:
    if(len(content) == 13):
        # print(content[0])
        # print('要素数:13')
        value = f'VALUES({content[0]}, {num}, {date}, time, 0, 0, 0, 0, {content[1]}, {content[2]}, {content[3]}, {content[4]}, {content[5]}, {content[6]}, {content[7]}, {content[8]}, {content[9]},{content[10]}, {content[11]}, {content[12]})'
        fullSql = sql + value 
        sql_access.append(fullSql)
        
    elif(len(content) == 11):
        # print(content[0])
        # print('要素数:11')
        value = f'VALUES({content[0]}, {num}, {date}, time, 0, 0, 0, 0, {content[1]}, {content[2]}, {content[3]}, {content[4]}, {content[5]}, {content[6]}, {content[7]}, {content[8]}, {content[9]},{content[10]}, 0, 0)'
        fullSql = sql + value 
        sql_access.append(fullSql)
        
    else:
        print('テキストファイルの内容を再度確認してください。')
    

p.pprint(sql_access)
p.pprint(len(sql_access))

