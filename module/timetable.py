from warnings import warn
import colorama,prettytable
from re import findall
try:
    import datawash
    import warnerror as we
except (ModuleNotFoundError,ImportError):
    from . import datawash
    from . import warnerror as we
FROM_URL = "http://qq.ip138.com/train/%s.htm"
FROM_DOMAIN = "qq.ip138.com"
FROM_MAIN_DOMAIN="ip138.com"
def getFromUrl(code:str) -> str:
    '''
    Get schedule excuse address.
    :param code:Train Code
    :return:URL String
    '''
    return FROM_URL % code
class TrainData(object):
    '''
    TrainData Get Object
    >>>obj=TrainData("G1")
    >>>obj.syntax()
    True
    >>>obj.go()
    >>>print(obj.getTitle())
    '''
    def __init__(self,code:str=""):
        if code == "":
            warn("The TrainCode Isn't Set",we.TrainCodeNoneWarning)
        self.code=code
        self.data=None
    def reset(self,code:str):
        self.code=code
        self.data=None
    def syntax(self) -> bool:
        return datawash.code_syntax(self.code)

    def go(self) -> int:
        from requests import get
        if(self.code == ""):
            raise we.TrainCodeNoneError("Train Code Isn't Defined")
        self.data=get(getFromUrl(self.code))
        return 0

    def getTitle(self):
        return datawash.washTitle(self.data)

    def getStartEndType(self):
        return datawash.washSET(self.data,self.code)

    def getCnTable(self):
        train_station = findall("<a href=\"/train.*\" target=\"_blank\">.*</a>", self.data)

        train_time = findall("([0-9]{2}:[0-9]{2})|(---)", self.data)
        train_time.pop(0)
        tableHead = ["车站", "到达时间", "发车时间", "走行时间（小时）"]
        for i in tableHead:
            tableHead[tableHead.index(i)] = colorama.Fore.GREEN + i + colorama.Fore.RESET
        tableObj = prettytable.PrettyTable(tableHead)
        tableObj.header = True
        tableObj.horizontal_char = '-'
        tableObj.junction_char = '|'
        cnt = 0
        for i in train_station:
            row = []
            j = i.replace("</a>", "")

            e = j.index(">")

            # print(j[e+1:],
            #       real(train_time[cnt]),
            #       real(train_time[cnt+1]),
            #       real(train_time[cnt+2]))
            row.append(colorama.Fore.RED + j[e + 1:] + colorama.Fore.RESET)
            # print(colorama.Back.BLACK)
            row.append(colorama.Fore.LIGHTMAGENTA_EX + datawash.real(train_time[cnt]))
            row.append(datawash.real(train_time[cnt + 1]))
            row.append(datawash.real(train_time[cnt + 2]))
            print(colorama.Fore.RESET)
            tableObj.add_row(row)
            cnt = cnt + 3
        return tableObj
