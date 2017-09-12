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
        print('Qiita:Teamの' + teamName + 'からデータを抜き出します')
    else :
        print('引数の数が何かおかしいです')

def main():
    headers = {"Authorization" : "Bearer " + apiKey}
    requestUrl = apiUrl + api
    request = urllib.request.Request(requestUrl, None, headers)
    response = urllib.request.urlopen(request)
    jsonRaw = response.read().decode('utf-8')
    json.dumps(jsonRaw, ensure_ascii=False)
    jsons = json.loads(jsonRaw)

    for oneWrote in jsons:
        print(oneWrote['title'])

if __name__ == '__main__':
    argmentscheck()
    main()

