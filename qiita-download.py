#!/usr/bin/env python
# coding: utf-8

import sys
import json
import urllib.request
import urllib.parse

apiUrl = ''
apiKey = ''
teamName = ''
api = '/api/v2/items?per_page=100'

def argmentscheck():
    global apiUrl
    global apiKey
    global teamName

    if len(sys.argv) == 2:
        apiKey = sys.argv[1]
        apiUrl = 'https://qiita.com'
        print('Qiitaからデータを抜き出します')
    elif len(sys.argv) == 3:
        apiKey = sys.argv[1]
        teamName = sys.argv[2]
        apiUrl = 'https://' + teamName + '.qiita.com'
        print('Qiita:Teamの' + teamName + u'からデータを抜き出します')
    else :
        print('引数の数が何かおかしいです')

def main():
    header = {"header" : "Bearer " + apiKey}
    requestUrl = apiUrl + api
    request = urllib.request.Request(requestUrl, None, header)
    response = urllib.request.urlopen(request)
    jsonRaw = response.raed().decode('utf-8')
    json.dumps(jsonRaw, ensure_ascii=False)
    jsons = json.loads(jsonRaw)
    print(jsons)

if __name__ == '__main__':
    argmentscheck()
    main()


# coding: utf-8

#import json
#import sys
#import copy
#import urllib.request
#import urllib.parse

#url	= 'https://yumemi.backlog.jp/'
#api	= 'api/v2/users'
#api_key	= 'sFOPcDZ44xsh7HkwxoUD590ZlWurZlD1iaXgWMeVBEevSh4EN0KSZLS9SSoliY6A'

#if __name__ == "__main__":

#    認証処理
#    urlstring	= url + api + "/myself?apiKey=" + api_key
#    response	= urllib.request.urlopen(urlstring)

#    ユーザ一覧の取得
#    urlstring 	= url + api + "?apiKey=" + api_key
#    response	= urllib.request.urlopen(urlstring)
#    jsonRaw	= response.read().decode('utf-8')
#    json.dumps(jsonRaw, ensure_ascii=False)
#    userListString	= json.loads(jsonRaw)

#    print("ユーザID,ユーザ名,メールアドレス")
#    for user in userListString:
#        print(str(user['userId']) + "," + str(user['name']) + "," + str(user['mailAddress']))

#    jsonUserString = '['
#    for user in userListString:
#        urlstring	= url + api + "/" + str(user['id']) + "?apiKey=" + api_key
#        response	= urllib.request.urlopen(urlstring)
#        jsonRaw		= response.read().decode('utf-8')
#        jsonUserString	= jsonUserString + str(jsonRaw)
#        jsonUserString	= jsonUserString + ','
#    jsonUserString	= jsonUserString[:-1] + ']'
#    json.dumps(jsonUserString, ensure_ascii=False)
#    userListString	= json.loads(jsonUserString)

#    print("----------")
#    print("ユーザID,ユーザ名,メールアドレス")
#    for user in userListString:
#        print(str(user['userId']) + "," + str(user['name']) + "," + str(user['mailAddress']))
