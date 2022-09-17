# テキストファイルの読み込み
import pprint as p

# テキストファイルのパスは入力の際に指定するが、取り急ぎ読み込みの処理の確認を優先する
f = open('DiskSizeResult.txt', 'r', encoding='CP932')
datalist = f.readlines()

List = []

for data in datalist:

    li = data.split()
    List.append(li)

f.close()
p.pprint(List)
