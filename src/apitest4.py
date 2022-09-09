import json, requests
from lis import lis
#joke取得
uri = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}
r = requests.get(uri,headers=headers)
r = json.loads(r.content)['joke']
print(r)
#翻訳言語指定
trn = {1:'ja',2:'ko',3:'es'}
tr = int(input('日本:1,韓国:2,スペイン:3,4:言語を選択\n数字を入力:'))
tr = lis(input('言語を入力：')) if tr == 4 else trn[tr]
#翻訳＆エラー処理
while True:
    try:
        url = f'https://script.google.com/macros/s/AKfycbwMFaS2o-wXUtbgLaiUyYyf7GxFKVQwIoypzR31UmOG7uhw-zwkzmetseA7jTWopf8A/exec?text="{r}"&source=en&target={tr}'
        res = requests.get(url)
        data = json.loads(res.content)
        print(data['text'])
        break
    except json.JSONDecodeError as e:
        if 'en' == tr:
            print(r)
        else:
            print('言語なし')
        break