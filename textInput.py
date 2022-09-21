#取得したテキストから情報を抽出する
import pprint as p
import function.data as d
import function.select as select
import function.sqlAccess as sql

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

sql_access = sql.sqlAccess(selectedList)


p.pprint(sql_access)
p.pprint(len(sql_access))

