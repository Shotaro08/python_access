#ファイルへのパス、日付登録のプログラム
from datetime import datetime
import re
import pprint as p
import sys

def inputUrlDate():
    try:
        #フルパスと日付の入力
        url = input('読み込むテキストファイルのフルパス（拡張子.txtまで）を入力してください ')
        date = input('登録日付(YYYYMMDD)を入力してください ')

        #入力されていない場合、例外とばす
        if url == '':
            raise OSError


        if date == '':
            raise OSError
        
        datetime.strptime(date, '%Y%m%d')
        print('yes')


        print('以下でよろしいですか')
        print('フルパス: ' + url)
        print('登録日付: ' + date)


        #入力内容の確認
        check = input('Enter or cancel(C)')

        #'C'の場合はシステムを終了する
        if (check == 'C'):
            print('chancelしました')
            print('再度やり直してください')
            input()
            sys.exit()
                
        #入力されたurlと日付を返す
        return url, date

    except OSError as e:
        print("ファイルへのパスまたは日付が空欄です")
        print('再度やり直してください')
        input()
    
    except ValueError as err:
        print(err)
        print('日付が正しくありません')
        print('再度ご確認ください')
        input()

