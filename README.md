# 簡単な使い方の説明
  
以下のURLからQiitaのアクセストークンを発行しましょう  
https://qiita.com/settings/applications  
  
あとは以下の通りコマンドを叩けばOKです。  

■ QiitaからWebスクレイピングする

```
python3 qiita-download {アクセストークン}
```

■ Qiita:Teamからwebスクレイピングする

```
python3 qiita-download {アクセストークン} {TeamName}
```


## 事前準備
   
最新のpython3をインストールしておく  
  
```
brew install python3
```

標準ライブラリを使っているのでpip installとかは不要です。
