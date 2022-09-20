import re

def select(list):

    #SQL文のため、新しい配列に格納し直す
    selectedList = []

    for li in list:
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
    
    return selectedList