from re import findall,search
def code_syntax(c:str) -> bool:
    d="[GgZzDdCc][0-9]{1,5}"
    data=findall(d,c)
    if len(data) == 1:
        if data[0] == c:
            return True
        else:
            return False
    else:
        return False

def washTitle(d):
    title = search("<h1>.*</h1>", d).group(0)
    title = title.replace("<h1>", "")
    title = title.replace("</h1>", "")
    return title
def washSET(data,code):
    title = washTitle(data)
    start = search("从.*开往", title).group(0).replace("从", "") \
        .replace("开往", "")
    end=search("往.*%s" % code.lower(), title).group(0).replace("往", "").replace(code.lower(), "")
    train_type = search("列车类型：.*&nbsp;", data).group(0).replace("&nbsp;", "").replace("</td>", "").replace(
        "<td>", "")
    return [start,end,train_type]
def real(l):
    for i in l:
        if(i != ''):
            return i
    return -1