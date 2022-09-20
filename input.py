#ファイルへのパス、日付登録のプログラム
import re
import pprint as p
import sys

url = input('読み込むファイルへのフルパスを入力してください')
date = input('登録したい日付を入力してください')

print('以下でよろしいですか')
print(url)
print(date)
check = input('Enter or cancel(C)')

if (check == 'C'):
	print('chancelしました')
	print('再度やり直してください')
	sys.exit();


f = open(f'{url}', 'r')
datalist = f.readlines()
arr = []

for data in datalist:
  selectData = re.findall('^...[0-9][0-9][0-9]', data)
  dataMap = re.search('^...[0-9][0-9][0-9]', data)
  if(selectData):
   arr.append(selectData)
   
f.close()
p.pprint(arr)
p.pprint(url)
p.pprint(date)