#!/usr/bin/env python
# coding: utf-8

import os
import sys
import re
import json
import urllib.request
import urllib.parse

url = ''
apiKey = ''
teamName = ''
api = '/api/v2/items?per_page=100'
pageApi = '&page='
pageCount = 0
maxCount = 0

def argmentscheck():
    global url
    global apiKey
    global teamName
    global api

    url = ''
    apiKey = ''
    teamName = ''
    api = '/api/v2/items?per_page=100'

    if len(sys.argv) == 2:
        apiKey = sys.argv[1]
        url = 'https://qiita.com'
        print('Qiitaからデータを抜き出します')
    elif len(sys.argv) == 3:
        apiKey = sys.argv[1]
        teamName = sys.argv[2]
        url = 'https://' + teamName + '.qiita.com'
        print('Qiita:Teamの' + teamName + 'からデータを抜き出します')
    else :
        print('引数の数が何かおかしいです')

def createDirectory(createDay, markdownUrl):
    directoryArray = createDay.split('-')
    createPath = "./" + directoryArray[0] + "/" + directoryArray[1]

    if not(os.path.exists(createPath)):
        os.makedirs(createPath)

def getPerPageJsonDownload():
    global pageApi
    global pageCount
    global maxCount

    headers = {"Authorization" : "Bearer " + apiKey}
    requestUrl = url + api

    if pageCount:
        requestUrl = url + api + pageApi + str(pageCount)
    print(requestUrl)
    request = urllib.request.Request(requestUrl, None, headers)
    response = urllib.request.urlopen(request)
    responseHeader = str(response.info())

    if maxCount == 0:
        headerList = []
        headerDict = {}
        for headerOneline in responseHeader.split('\n'):
            for oneWord in headerOneline.split(': '):
                if len(oneWord):
                    headerList.append(oneWord)
        headerDict = dict(zip(headerList[0::2], headerList[1::2]))
        maxCount = headerDict['Total-Count']

    jsonRaw = response.read().decode('utf-8')
    json.dumps(jsonRaw, ensure_ascii=False)
    return jsonRaw

def fileWriting(createDay, markdown, title, author):
    markdownTitle = title.replace('/', ' ') + '.md'
    directoryArray = createDay.split('-')

    createPath = "./" + directoryArray[0] + "/" + directoryArray[1] + "/" + "files/"
    filePath = "./" + directoryArray[0] + "/" + directoryArray[1] + "/" + markdownTitle

    if not(os.path.exists(createPath)):
        os.makedirs(createPath)

    pattern = r"https://qiita.com[a-zA-Z0-9/-].*\.(?:png|jpg|jpeg)"
    pattern += r"|https://qiita-image-store.s3.amazonaws.com[a-zA-Z0-9/-].*\.(?:png|jpg|jpeg)"
    if len(teamName):
        pattern += r"|https://" + teamName + r".qiita.com[a-zA-Z0-9/-].*\.(?:png|jpg|jpeg)"

    matchedList = re.findall(pattern, markdown)
    headers = {"Authorization" : "Bearer " + apiKey}

    for oneImage in matchedList:
        url = oneImage.split(" ")[0].split(")")[0]
        request = urllib.request.Request(url)

        if (re.search(r"qiita.com", url)):
            request = urllib.request.Request(url, None, headers)

        response = urllib.request.urlopen(request)
        fileName = url.split('/')[-1]
        writeFile = open(createPath + fileName, 'wb')
        writeFile.write(response.read())
        writeFile.close()
        markdown = markdown.replace(url, createPath + fileName)

    writeFile = open(filePath, 'a')
    writeFile.write('寄稿者ID:' + author + '\n\n')
    writeFile.write(markdown)
    writeFile.close()

def main():
    global pageCount

    jsonRaw = getPerPageJsonDownload()
    jsons = json.loads(jsonRaw)
    for count in range(round(int(maxCount)/len(jsons))):
        pageCount += 1
        for oneWrote in jsons:
            createDirectory(oneWrote['created_at'], oneWrote['url'])
            fileWriting(oneWrote['created_at'], oneWrote['body'], oneWrote['title'], oneWrote['user']['id'] )
        jsonRaw = getPerPageJsonDownload()
        jsons = json.loads(jsonRaw)

if __name__ == '__main__':
    argmentscheck()
    main()

