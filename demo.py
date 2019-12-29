import socket
from scipy import *
import matplotlib.pyplot as plt
import sick_telegram

HOST = '192.168.0.1'
PORT = 2112

def startclient():
    """

    :return:
    """
    BUFSIZE = 40000
    ADDR = (HOST, PORT)

    # while True:
    # data = input('>')
    #data = '02 73 52 4E 20 4C 4D 44 73 63 61 6E 64 61 74 61 03'
    data = '02 73 52 4E 20 4C 4D 44 73 63 61 6E 64 61 74 61 03'
    # if not data:
    #     break
    bites = getcmd(data)
    cmdstring = bytearray(bites, encoding='utf-8')
    print('@'*20, cmdstring)
    # tcpclisocket = socket(AF_INET, SOCK_STREAM)
    tcpclisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpclisocket.connect(ADDR)
    tcpclisocket.send(cmdstring)
    pcddata = tcpclisocket.recv(BUFSIZE).decode()
    print('#'*10,'\n') 
    print(pcddata)
    print(type(pcddata))
    print('\n','#'*10) 
    # caldata(pcddata)
    #
    
    # sick = sick_telegram.SickTelegram()

    tcpclisocket.close()

def handle_data(sourcedata):
    data = sourcedata.split(' ')
    # https://www.cnblogs.com/rouwawa/p/6959009.html
    
def getcmd(hexstring):
    """

    :param hexstring:
    :return:
    """
    hexstring = hexstring.replace(" ", "")
    if (len(hexstring) % 2) != 0:
        hexstring += " "
    bits = ""
    for x in range(0, len(hexstring), 2):
        bits += chr(int(hexstring[x:x + 2], 16))
    return bits


if __name__ == '__main__':
    startclient()