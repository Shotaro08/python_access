#取得したテキストから情報を抽出する
import re
import pprint as p

# ファイルからデータ取得
# 1行ずつ読み込む
f = open('DiskSizeResult.txt', 'r', encoding='CP932')
datalist = f.readlines()
f.close()

# 取得したデータを整理する
List = []

for data in datalist:
        #1行分の文字列として取得しているので、配列にする
        li = data.split()
        listReplaceData = []
        
        # 配列の中一つ一つの文字の処理をして、配列に格納する
        for organizedData in li:
            #"," ":" を取り除く
            replacedData = organizedData.strip(',').strip(':')
            listReplaceData.append(replacedData)
            
        #Listに配列を入れる　多元配列にする
        List.append(listReplaceData)
        


#SQL文のため、新しい配列に格納し直す
selectedList = []

for li in List:
    if(li):
        #サーバー名をプライマリーとして、serverの配列にいれる
        #正規表現でテキストファイルのサーバー名を取得し、格納
        if re.compile('^...[0-9][0-9][0-9]').search(li[0]):
            server = []
            server.append(li[0])
            selectedList.append(server)
            
        #'C'ファイルの使用量を格納する   
        elif(li[0] == 'C'):
            #使用量格納
            fileC = int(li[3]) - int(li[2])
            server.append(fileC)
            #空容量格納
            server.append(li[2])
            
        #'D'ファイルの使用量を格納する 
        elif(li[0] == 'D'):
            #使用量格納
            fileD = int(li[3]) - int(li[2])
            server.append(fileD)
            #空容量格納
            server.append(li[2])
            
        #'F'ファイルの使用量を格納する 
        elif(li[0] == 'F'):
            #使用量格納
            fileF = int(li[3]) - int(li[2])
            server.append(fileF)
            #空容量格納
            server.append(li[2])
            
        #'G'ファイルの使用量を格納する 
        elif(li[0] == 'G'):
            #使用量格納
            fileG = int(li[3]) - int(li[2])
            server.append(fileG)
            #空容量格納
            server.append(li[2])
            
        #'H'ファイルの使用量を格納する 
        elif(li[0] == 'H'):
            #使用量格納
            fileH = int(li[3]) - int(li[2])
            server.append(fileH)
            #空容量格納
            server.append(li[2])
            
        #'I'ファイルの使用量を格納する 
        elif(li[0] == 'I'):
            #使用量格納
            fileI = int(li[3]) - int(li[2])
            server.append(fileI)
            #空容量格納
            server.append(li[2])
        
selectedList.append(server)

#最後が重複して取れてしまうので削除する
del selectedList[-1]

# p.pprint(selectedList) #SQLで使用するデータになっている

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


#Iが入っているかどうか(要素数)で条件分岐
for content in selectedList:
    if(len(content) == 13):
        print(content[0])
        print('要素数:13')
        value = f'VALUES({content[0]}, {num}, {date}, time, 0, 0, 0, 0, {content[1]}, {content[2]}, {content[3]}, {content[4]}, {content[5]}, {content[6]}, {content[7]}, {content[8]}, {content[9]},{content[10]}, {content[11]}, {content[12]})'
        fullSql = sql + value 
        p.pprint(fullSql)
        
    elif(len(content) == 11):
        print(content[0])
        print('要素数:11')
        value = f'VALUES({content[0]}, {num}, {date}, time, 0, 0, 0, 0, {content[1]}, {content[2]}, {content[3]}, {content[4]}, {content[5]}, {content[6]}, {content[7]}, {content[8]}, {content[9]},{content[10]}, 0, 0)'
        fullSql = sql + value 
        p.pprint(fullSql)
        
    else:
        print('テキストファイルの内容を再度確認してください。')
    


