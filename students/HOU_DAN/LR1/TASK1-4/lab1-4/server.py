# -*- coding: utf-8 -*-
from lab1.autorobot import reply_msg
import re
import socket
import pandas as pd
import threading
import time

global monitor_text,conn_list_chat,addr_list_chat,conn_list,addr_list


def read(file, n=20):
    re=""
    x=0
    for i in file:
        i=str(i)
        re +=i
        x+=1
        if not i:
            return re
        elif x>n:
            return re
def endconn(conn,addr):
    conn.send("断开链接".encode('utf-8'))
    conn_list.remove(conn)
    addr_list.remove(addr)
    conn.close()
def autorobot(conn,addr):
    addr = addr
    conn.send("说明：开始与机器人聊天吧，end退出该模式".encode('utf-8'))
    while True:
        data = conn.recv(1024).decode('utf-8')
        # print(data)
        if data == "end":
            break
        else:
            re = reply_msg(data)
            conn.send(re.encode('utf-8'))
def math(conn,addr):
    addr = addr
    conn.send("说明：math进入计算模式，a进入勾股定理计算，b求解二次方程，c计算梯形面积，d计算平行四边形面积，end退出该模式".encode('utf-8'))
    while True:
        text = conn.recv(1024)
        text = text.decode('utf-8')
        if text == "end":
            break
        elif text == "math":
            conn.send("**maht中的math计算，完成后自动返回math模式中**".encode('utf-8'))

            text = conn.recv(1024)
            text = text.decode('utf-8')
            r = r'\d+'
            r2 = r'[/+-/*/]'
            ints = re.findall(r, text)
            symbols = re.findall(r2, text)

            count = float(ints.pop(0))

            for i in [0] * len(ints):
                pop = float(ints.pop(i))
                symbol = symbols.pop(i)
                if symbol == '+':
                    count += pop
                elif symbol == '-':
                    count -= pop
                elif symbol == '*':
                    count *= pop
                elif symbol == '/':
                    count /= pop
            conn.send(str(count).encode('utf-8'))
        elif text == "a":
            # 打印说明
            conn.send("**输入abc三边，以a+b或c-a或c-b形式输入，返回计算结果**".encode('utf-8'))
            text = conn.recv(1024)
            text = text.decode('utf-8')
            # **************************
            r1 = r'\d+'
            r2 = r'[\+-]'
            ints = re.findall(r1, text)
            symbols = re.findall(r2, text)
            result = 0.0
            count = float(ints.pop(0)) ** 2
            for i in [0] * len(ints):
                pop = float(ints.pop(i)) ** 2
                symbol = symbols.pop(i)
                print(symbols)
                if symbol == '+':
                    result = (count + pop) ** (1 / 2)
                elif symbol == '-':
                    if count > pop:
                        result = (count - pop) ** (1 / 2)
                    else:
                        result = (pop - count) ** (1 / 2)
            conn.send(str(result).encode('utf-8'))
        elif text == "b":
            # 打印说明
            conn.send("**输入二次方程，或者以a=,b=,c=的形式输入**".encode('utf-8'))
            text = conn.recv(1024)
            text = text.decode('utf-8')
            # *************************
            r_a = r'(?<=a=)\d+\.?\d*|\d+\.?\d*(?=[Xx].2)'
            r_b = r'(?<=b=)\d+\.?\d*|\d+\.?\d*(?=[Xx][/+-])'
            r_c = r'(?<=c=)\d+\.?\d*|(?<=\+|-)\d+\.?\d*$'
            a = float(re.findall(r_a, text)[0]) if re.findall(r_a, text) else 1
            b = float(re.findall(r_b, text)[0]) if re.findall(r_b, text) else 1
            c = float(re.findall(r_c, text)[0]) if re.findall(r_c, text) else 0
            D = b ** 2 - 4 * a * c
            if D > 0:
                x1 = (-b + D ** (1 / 2)) / 2 * a
                x2 = (-b * D ** (1 / 2)) / 2 * a
                x = "x1:" + str(x1) + ", x2:" + str(x2)
                conn.send(x.encode('utf-8'))
            elif D == 0:
                x = (-b * D ** (1 / 2)) / 2 * a
                conn.send(str(x).encode('utf-8'))
            else:
                conn.send("无解D<0".encode('utf-8'))
        elif text == "c":
            # 打印说明
            conn.send("**根据提示输入梯形参数**".encode('utf-8'))
            # *************************
            conn.send("上底:".encode('utf-8'))
            s = conn.recv(1024).decode('utf-8')

            conn.send("下底:".encode('utf-8'))
            x = conn.recv(1024).decode('utf-8')

            conn.send("高:".encode('utf-8'))
            h = conn.recv(1024).decode('utf-8')

            x = float(x)
            s = float(s)
            h = float(h)
            area = (s + x) * h / 2

            conn.send(str(area).encode('utf-8'))
        elif text == "d":
            # 打印说明
            conn.send("**根据提示输入平行四边形参数**".encode('utf-8'))
            # *************************
            conn.send("底边长:".encode('utf-8'))
            x = conn.recv(1024).decode('utf-8')

            conn.send("高:".encode('utf-8'))
            h = conn.recv(1024).decode('utf-8')

            x = float(x)
            h = float(h)
            area = x * h
            conn.send(str(area).encode('utf-8'))
        else:
            conn.send("UNKWON".encode('utf-8'))
def Http(conn, addr):
    addr = addr
    conn.send("说明：按照要求输入请求段，hist查看历史，end退出该模式".encode('utf-8'))
    while True:

        method = (conn.recv(1024).decode('utf-8')).upper()
        if method == "END":
            print("tiaochu")
            break
        elif method == "HIST":
            with open('Historical_search.csv') as f:
                text = read(f, 5)
            conn.send(text.encode('utf-8'))
            continue
        else:

            host = conn.recv(1024).decode('utf-8')

            Port = int(conn.recv(1024).decode('utf-8'))

            url = conn.recv(1024).decode('utf-8')

            data = conn.recv(1024).decode('utf-8')

            Content_Type = conn.recv(1024).decode('utf-8')

            print(repr(method),repr(host),repr(Port),repr(url),repr(data),repr(Content_Type))
            dataset_pd = pd.read_csv('Historical_search.csv', sep=",")
            dnew_pd = pd.DataFrame([[method,host,Port,url,repr(data),Content_Type,pd.datetime.now()]],columns=['method','host','Port','url','data','Content_Type','data_time'])
            dataset_pd = dataset_pd.append(dnew_pd,ignore_index=True)
            dataset_pd =dataset_pd[['method','host','Port','url','data','Content_Type','data_time']]
            dataset_pd.to_csv('./Historical_search.csv')

            if method == "HEAD":
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, Port))
                    print(f"与{host}:{Port}建立连接")
                    ask = method + f" {url}" + " HTTP/1.1\r\n" + "Host: " + host + "\r\nAccept: " + Content_Type + "\r\nConnection: " + data + "\r\n\r\n"
                    s.sendall(ask.encode('utf-8'))
                    respones = s.recv(1024)
                    conn.send(respones)

            elif method == "GET":
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

                    s.connect((host, Port))
                    ask = method + f" {url}" + " HTTP/1.1\r\n" + "Host: " + host + "\r\nAccept: " + Content_Type + "\r\nConnection: " + data + "\r\n\r\n"
                    s.sendall(ask.encode('utf-8'))

                    data = s.recv(1024 * 1024).decode('utf-8')
                    respones = ""
                    while data:
                        respones = respones + data
                        data = s.recv(1024*1024).decode('utf-8')
                    print(respones)
                    conn.sendall(respones.encode('utf-8'))
def broadcast():
    while True:
        for x in range(len(monitor_text)):
            info = monitor_text.pop(0)
            for i in range(len(conn_list_chat)):
                re = f"{info[1]}:"+info[2]
                # print(re)
                if info[2] == "《---进入聊天---》\n":
                    # 传送成员列表
                    for client_addr in addr_list_chat:
                        addr_client = "\\\\addr:"+str(client_addr)
                        for i in range(len(conn_list_chat)):
                            conn_list_chat[i].send(addr_client.encode('utf-8'))
                            time.sleep(0.01)
                time.sleep(0.001)#两个发送相隔时间过短会被一个recv接收
                conn_list_chat[i].send(re.encode('utf-8'))
def Chat(conn,addr):
    addr = addr
    conn.send("说明：进入聊天群，endchat结束模式".encode('utf-8'))
    conn_list_chat.append(conn)
    addr_list_chat.append(addr)
    #将用户进入信息压入广播列表内
    info = [conn, addr, "《---进入聊天---》\n"]
    monitor_text.append(info)
    thread_broadcast = threading.Thread(target=broadcast)#开启广播线程
    thread_broadcast.start()
    while True:
        r = conn.recv(1024)
        r = r.decode('utf-8')
        # print(r == "endchat\n")
        if r == "endchat\n":
            info =[conn,addr,"《----退出聊天---》\n"]
            conn.send("breack".encode('utf-8'))#杀掉客户端监听线程
            monitor_text.append(info)
            conn_list_chat.remove(conn)
            addr_list_chat.remove(addr)
            time.sleep(0.5)
            break
        else:
            list_info = []
            list_info.append(conn)
            list_info.append(addr)
            list_info.append(r)
            monitor_text.append(list_info)
            # time.sleep(0.1)

def main(conn,addr):
    while True:
        conn.send("***功能选取模式***\nendserver结束链接，math进入数学模式，autorobot自动俩天机器人，Http发送http请求，Chat进入聊天群，UNKWON未知指令".encode('utf-8'))
        r = conn.recv(1024)
        r = r.decode('utf-8')
        if r == "endserver":
            conn.send(r.encode('utf-8'))
            endconn(conn,addr)
            break
        elif r == "math":
            conn.send(r.encode('utf-8'))
            math(conn,addr)
        elif r == "autorobot":
            conn.send(r.encode('utf-8'))
            autorobot(conn,addr)
        elif r == "Http":
            conn.send(r.encode('utf-8'))
            Http(conn,addr)
        elif r == "Chat":
            conn.send(r.encode('utf-8'))
            Chat(conn,addr)
        else:
            conn.send('UNKWON'.encode('utf-8'))
if __name__ == "__main__":
    addr_list = []
    conn_list = []
    conn_list_chat=[]
    addr_list_chat=[]
    monitor_text = []
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('172.20.10.13', 9090))
        sock.listen(1)
        conn, addr = sock.accept()
        print(conn)
        print(addr)
#***************无验证***********************************************
        addr_list.append(addr)
        conn_list.append(conn)
        # print(conn_list)
        # print(addr_list)

        test = conn.recv(1024)
        conn.send(test)
        client = f'(\'{addr[0]}\', {str(addr[1])})'
        conn.send(client.encode('utf-8'))
        time.sleep(0.5)
        # *********链接验证********
        thread = threading.Thread(target=main, args=(conn, addr))
        thread.start()
#***************有验证************************************************
        # if addr[0] in addr_list:
        #     test = conn.recv(1024)
        #     conn.send("已经在服务器中,关闭此次链接".encode('utf-8'))
        #     conn.close()
        # else:
        #     addr_list.append(addr[0])
        #     conn_list.append(conn)
        #     print(conn_list)
        #     print(addr_list)
        #
        #     test = conn.recv(1024)
        #     conn.send(test)
        #     thread = threading.Thread(target=main, args=(conn, addr))
        #     thread.start()
        #     # *********链接验证********
        #     thread = threading.Thread(target=main,args=(conn,addr))
        #     thread.start()

