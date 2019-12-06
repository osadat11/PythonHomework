# PythonHomework
  授業用課題のリポジトリです

## 概要
　flaskを用いてタスク管理アプリ用のapiを作りました。
  vuetifyを使ってuiも作ってみました。
  
## 使い方
```
 > cd backend
 > python3 app.py
```

## 仕様
- アプリの初期url  
http://127.0.0.1:5000/
もしくは
http://localhost:5000/  
  
以下最初の `http://<hoge>:5000`はどちらでもアクセスできます。
- apiのurl  
    GET  :   http://127.0.0.1:5000/api/tasks  
    POST :   http://127.0.0.1:5000/api/tasks  
    PUT :    http://127.0.0.1:5000/api/tasks/[task:id]  
    DELETE : http://127.0.0.1:5000/api/tasks/[task:id]  

POST、PUTはデータを一緒に送らないと動きません。
- データ形式  
```
application/json" -d 
'{
    "title":"String",       # タスクのタイトル
    "dueD":"String",        # タスクの期限(日付)
    "dueT":"String",        # タスクの期限(時刻)
    "priority": Integer,    # タスクの優先度(0~3)
    "description":"String", # タスクの説明
    "done": Integer         # タスクが完了済みかどうか(1,0)
}'
```

## 使用した(入れてた)ライブラリ
python 3.7.4
```
autopep8               1.4.4  
Click                  7.0    
Flask                  1.1.1   !!
Flask-Cors             3.0.8   !!
flask-marshmallow      0.10.1  !!
Flask-SQLAlchemy       2.4.0   !!
itsdangerous           1.1.0  
Jinja2                 2.10.1 
MarkupSafe             1.1.1  
marshmallow            3.2.0   !!
marshmallow-sqlalchemy 0.19.0  !!
pip                    19.2.3 
pycodestyle            2.5.0  
setuptools             41.2.0 
six                    1.12.0 
SQLAlchemy             1.3.8   !!
Werkzeug               0.15.5 
wheel                  0.33.6
```
!!がついているものは実行に必須なライブラリです。

frontend
```
node.js   v10.15.2
npm       5.8.0
```
```
vuetify  v2.0.0 (画面のデザインに使用、フレームワーク)
axios   v0.19.0 (自作のapiとの通信に使用)
```

## frontendフォルダーからの実行方法
```
 > cd frontend
 > npm install
 > npm run serve
```
先にbackendからapp.pyを実行しないと正しく動きません
