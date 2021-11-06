# -*- coding: utf-8 -*-
import socket
from tkinter import *
import time
import threading

global sock,t, txtMsg,txtMsgList,addr,M,chat_client_list

def Clear_History():
    txtMsgList.delete('0.0', END)
def sendMsg(sock):  # 发送消息
    text = txtMsg.get('0.0', END).strip() + "\n"
    txtMsg.delete('0.0', END)
    sock.send(text.encode('utf-8'))
    if text == "endchat\n":

        close()
def cancelMsg():  # 取消消息
    txtMsg.delete('', END)
def sendMsgEvent(event):  # 发送消息事件
    if event.keysym == "Return":# 按回车键可发送
        sendMsg(sock)
def send_close():
    sock.send("endchat\n".encode('utf-8'))
    close()
def close():#关闭键有bug向服务器发送退出请求
    t.destroy()#guan
def add_chat_client_info():
    listLianxi.delete(0,END)
    # print(chat_client_list)
    for i in range(len(chat_client_list)):
        client_NO = f'Client{i}(ONLINE):'
        client_If = str(chat_client_list[i])
        listLianxi.insert(END, client_NO)
        listLianxi.insert(END, client_If)
# <editor-fold desc=“TK块”>
t = Tk()# 创建窗口
t.title('Chat聊天窗口')  # 窗口名称
t.resizable(0, 0)  # 禁止调整窗口大小
###******创建frame容器******###
frmA1 = Frame(width=180, height=300)
frmB1 = Frame(width=350, height=300)
frmB2 = Frame(width=350, height=80)
frmB3 = Frame(width=350, height=25)
###******创建控件******###
# 1.Text控件

txtMsgList = Text(frmB1,width=45)
txtMsg = Text(frmB2,width=45);
txtMsg.bind("<KeyPress-Return>", sendMsgEvent)  # 事件绑定，定义快捷键

btnSend = Button(frmB3, text='发送', width=8, command=lambda: sendMsg(sock))
btnCancel = Button(frmB3, text='取消', width=8, command=cancelMsg)
btnCance2 = Button(frmB3, text="关闭", width=8, command=send_close)
btnCance3 = Button(frmB3, text="清除记录", width=8, command=Clear_History)
scroLianxi = Scrollbar(frmA1, width=22)#聊天群成员
listLianxi = Listbox(frmA1, width=24, height=20,
                     yscrollcommand=scroLianxi.set)  # 连接listbox 到 vertical scrollbar
scroLianxi.config(command=listLianxi.yview)  # scrollbar滚动时listbox同时滚动

###******窗口布局******###
frmA1.grid(row=0, column=0)
frmB1.grid(row=0, column=1)
frmB2.grid(row=2, column=1)
frmB3.grid(row=3, column=1)
###******窗口布局******###
frmA1.grid_propagate(0)
frmB1.grid_propagate(0)
frmB2.grid_propagate(0)
frmB3.grid_propagate(0)
###******控件布局******###
btnSend.grid(row=0, column=0)
btnCancel.grid(row=0, column=1)
btnCance2.grid(row=0, column=2)
btnCance3.grid(row=0, column=3)

txtMsgList.grid()
txtMsg.grid()

scroLianxi.grid(row=0, column=1, ipady=120)
listLianxi.grid(row=0, column=0)
# </editor-fold>
def autorobot(sock):
    illustrate = sock.recv(1024)
    print(illustrate.decode('utf-8'))
    while True:
        m = input('cloemt:')
        sock.send(m.encode('utf-8'))
        if m == "end":
            print('**结束autorobot模式**')
            break
        else:
            r = sock.recv(1024)
            r = r.decode('utf-8')
            print('server:', r)
def math(sock):
    # 接收说明
    illustrate = sock.recv(1024)
    print(illustrate.decode('utf-8'))
    while True:
        m = input('cloemt:')
        sock.send(m.encode('utf-8'))
        if m == "end":
            print('**结束math数学模式**')
            break
        elif m == "math":
            r = sock.recv(1024)
            r = r.decode('utf-8')
            print('server:', r)
        elif m == "a":
            # 接受说明
            ill = sock.recv(1024)
            print(ill.decode('utf-8'))
            # ********
            m = input('cloemt:')
            m = m.encode('utf-8')
            sock.send(m)
            # ********
            result = sock.recv(1024).decode('utf-8')
            print("返回结果:", result)
        elif m == "b":
            # 接受说明
            ill = sock.recv(1024)
            print(ill.decode('utf-8'))
            # ********
            m = input('cloemt:')
            m = m.encode('utf-8')
            sock.send(m)
            # ********
            result = sock.recv(1024).decode('utf-8')
            print("返回结果:", result)
        elif m == "c":
            # 接受说明
            ill = sock.recv(1024)
            print(ill.decode('utf-8'))
            # ********
            r1 = sock.recv(1024).decode('utf-8')
            m = input(r1)
            sock.send(m.encode('utf-8'))

            r2 = sock.recv(1024).decode('utf-8')
            m = input(r2)
            sock.send(m.encode('utf-8'))

            r3 = sock.recv(1024).decode('utf-8')
            m = input(r3)
            sock.send(m.encode('utf-8'))
            # ********
            result = sock.recv(1024).decode('utf-8')
            print("梯形面积:", result)
        elif m == "d":
            # 接受说明
            ill = sock.recv(1024)
            print(ill.decode('utf-8'))
            # ********
            r1 = sock.recv(1024).decode('utf-8')
            m = input(r1)
            sock.send(m.encode('utf-8'))

            r2 = sock.recv(1024).decode('utf-8')
            m = input(r2)
            sock.send(m.encode('utf-8'))
            # ********
            result = sock.recv(1024).decode('utf-8')
            print("平行四边形面积:", result)
        else:
            r = sock.recv(1024)
            print(r.decode('utf-8'))
def Http(sock):
    illustrate = sock.recv(1024)
    print(illustrate.decode('utf-8'))
    while True:

        m = input("请求方法:")
        sock.send(m.encode('utf-8'))
        if m == "end":
            print('**结束Http模式**')
            break  # 退出检测
        elif m == "hist" or m == "HIST":
            print("输出历史记录:")
            text = sock.recv(1024).decode('utf-8')
            print(text)
            continue
        else:

            m = input("Host:")
            sock.send(m.encode('utf-8'))

            m = input("Porst:")
            if not m:
                m = "80"
            sock.send(m.encode('utf-8'))

            m = input("Url:")
            if not m:
                m = "/"
            sock.send(m.encode('utf-8'))

            m = input("Connection:")
            if not m:
                m = "\r\n"
            sock.send(m.encode('utf-8'))

            m = input("Content-Type:")
            if not m:
                m = "text/html"
            sock.send(m.encode('utf-8'))

            response = sock.recv(1024 * 1024).decode('utf-8')
            print("返回数据：\n", response)
def monitor():
    while 1:
        text = sock.recv(1024)
        text = text.decode('utf-8')
        # print(text == "breack")
        # print(text[7:])
        if text == "breack":
            break
        elif text[:7] == "\\\\addr:":
            addr_client = text[7:]
            if addr_client not in chat_client_list:
                chat_client_list.append(addr_client)
                add_chat_client_info()
            continue
        txtMsgList.insert(END, text)
def Chat(sock):
    global M,chat_client_list
    illustrate = sock.recv(1024)
    print(illustrate.decode('utf-8'))
    chat_client_list = []
    M = threading.Thread(target=monitor)
    M.start()
    t.mainloop()

def main(sock):
    while True:
        mod = sock.recv(1024)
        print(mod.decode('utf-8'))
        m = input('cliemt:')
        sock.send(m.encode('utf-8'))
        re = sock.recv(1024)
        re = re.decode('utf-8')
        print('------------------model-------------->', re)
        # *************模式的选取与确认**************
        if re == "endserver":
            r = sock.recv(1024)
            print(r.decode('utf-8'))
            sock.close()
            break
        elif re == "autorobot":
            print("进入autorobot模式")
            autorobot(sock)
        elif re == "math":
            print("进入数学模式")
            math(sock)
        elif re == "Http":
            print("进入Http模式")
            Http(sock)
        elif re == "Chat":
            print("进入Chat模式")
            Chat(sock)

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('172.20.10.13', 9090))#'localhost'

    sock.send("Test".encode('utf-8'))
    test = sock.recv(1024)
    if test.decode('utf-8') == "Test":
        print('链接成功')
        addr = str(sock.recv(1024).decode('utf-8'))
        print(addr)
        # ***************链接验证*******************
        main(sock)
    else:
        print(test.decode('utf-8'))
        sock.close()
