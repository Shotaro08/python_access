import function.inputUrlDate as inputUrlDate
import function.textInput as textInput
import function.selectList as selectList
import function.selectdata as selectdata
import dbConnect as db
import pprint as p

urlAndDate = inputUrlDate.inputUrlDate()

#値がとれるまで再実行/ cancelされた場合はやり直し
while not urlAndDate:
    # retry
    urlAndDate = inputUrlDate.inputUrlDate()
    
url = urlAndDate[0]
date = urlAndDate[1]

#テキストファイルからの読み込み(入力したフルパスから)
list = textInput.textInput(url)


#データの整理
selectedList = selectList.selectList(list)


# #SQL文作成 入力した日付を渡す
sqlList = selectdata.selectdata(selectedList, date)

for sql in sqlList:
    print(sql)

input()



               