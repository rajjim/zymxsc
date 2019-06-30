import decimal

def getFileContent(filename):
    file=None
    try:
        file=open(filename,encoding='utf-8')
        lines=file.readlines()
        listcontent=[]
        for line in lines:
            contents=line.split(':')
            content=contents[1].split('\n')
            listcontent.append(content[0])
        return listcontent
    except Exception as e:
        print("配置文件不存在")
        print(str(e))
        return []
