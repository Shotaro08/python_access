

def data(datalist):
# 取得したデータを整理する
    list = []

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
            list.append(listReplaceData)
    
    return list