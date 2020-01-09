
def readHtml(fileName):
    """
    读取html源文件
    :param fileName: 文件名
    :return: 二进制的html源代码
    """
    # /正斜线做目录分隔符
    path = 'templates/'+fileName

    try:
        with open(path,'rb') as fp:
            html = fp.read()
    except Exception as e:
        html = b'File Not Found'
        print(e)
    return html





#首页
def index(environ,startResponse):
    startResponse('200 ok', [('Content-Type', 'text/html')])
    res = readHtml('index.html')
    return [res]


def login(environ, startResponse):
    startResponse('200 ok', [('Content-Type', 'text/html')])
    return [readHtml('login.html')]


def register(environ, startResponse):
    startResponse('200 ok', [('Content-Type', 'text/html')])
    return [b'Register']