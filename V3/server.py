import socket
import threading
import time

print("HH的局域网通讯程序-服务端 正在初始化")

transport_protocol = 2.0
sockets = []
# 这里面的套接字用来接收数据
out = []
# 这里用来转发
t = []
# 线程列表
ports = 9980
# 端口号
myname = socket.gethostname()
myIP = socket.gethostbyname(myname)
is_running = True

print(f"当前连接协议：HH_web-V{transport_protocol}")
print("请使用相同协议的客户端连接")
print("最大连接数：20")
print("当前网络IPV6支持：", socket.has_ipv6)
print(f"本机主机名：{myname}")
print(f"本机局域网IP：{myIP}")

print("HH的局域网通讯程序-服务端 初始化完成")


def retransmission(index):
    global sockets
    print(f"第{index}台设备已建立连接")
    sockets[index].setblocking(True)
    while True:
        if not is_running:
            sockets[index].close()
            return 0
        datas = sockets[index].recvfrom(2048)[0]
        if str(datas)=="b''":continue
        # print(f"接收数据:{datas}")
        for i in sockets:
            try:
                i.send(datas)
            except Exception as e:
                pass
        print(f"来自第{index}台设备的信息转发完成")


def listen_socket():
    # 服务器核心函数(里面有很多sleep,防止"BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作"的)
    global sockets, ports, out, t
    s = socket.socket()
    s.bind(("", ports))
    ports -= 1
    print(f"已开启{ports + 1}端口，开始获取连接")
    s.listen(20)
    # 创建TCP服务器
    print("服务器已准备好接收连接请求")
    print("HH的局域网通讯程序-服务端 已启动")
    s.setblocking(False)
    print("开始等待连接")
    while is_running:
        if not is_running: break
        try:
            if not is_running: break
            new_s = s.accept()
        except socket.error:
            continue
        print("检测到连接请求，套接字信息：", new_s)
        time.sleep(0.01)
        c = new_s[0].recvfrom(2048)
        client_ip = new_s[1][0]
        new_s = new_s[0]
        print(f"连接请求ip：{client_ip}")
        strs = str(c[0])
        yn = strs.replace(f"Request-connection-V{transport_protocol} ", "")
        # print(strs)
        if f"Request-connection-V{transport_protocol}" in strs:
            print("已接收到客户端连接请求")
            strs.split(" ")
            client_uuid = strs.split(" ")[2]
            b = bytes(client_uuid, "utf-8")
            new_s.send(b)
            print("客户端连接校验信息已发送，等待客户端通过验证")
            time.sleep(0.01)
            a = str(new_s.recvfrom(2048))
            print(f"来自客户端的连接请求校验信息：{a}\n服务器请求校验信息：{yn}")
            if yn in a:
                print("服务端验证通过")
                time.sleep(0.01)
                new_s.send(bytes("hello", "utf-8"))  # 服务器在结束该连接请求前发送给客户端的数据
                sockets.append(new_s)
                print("启动数据处理线程")
                ts = threading.Thread(target=retransmission, args=tuple([len(sockets) - 1]))
                ts.start()
                t.append(ts)
                print("已建立连接")
            else:
                print("服务端校验失败")
                print("以下是错误诊断信息:")
                print(yn, "\n", a)
                continue
        else:
            print("连接请求校验失败")
            print("以下是错误诊断信息:")
            print(strs, f"\nRequest-connection-V{transport_protocol}")
            continue

    s.close()
