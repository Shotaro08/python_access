import pprint as p
import sys

def textInput(url):
    #取得したテキストから情報を抽出する
    # ファイルからデータ取得
    # 1行ずつ読み込む
    try:
        f = open(f'{url}', 'r')
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
        
        return List

    #ファイルがみつからない場合        
    except FileNotFoundError as err: 
        print(err)
        print("ファイルがみつかりませんでした")
        print("ファイルへのパスを再度確認してください")
        input()
        sys.exit()
    
    
