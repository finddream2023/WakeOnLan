import socket
import struct
import time


def wake_up(name='', ip='', mac='DC-4A-3E-78-3E-0A'):
    MAC = mac
    BROADCAST = ip
    if len(MAC) != 17:
        raise ValueError(
            "MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
    mac_address = MAC.replace("-", '')
    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])  # 构造原始数据格式
    send_data = b''

    # 把原始数据转换为16进制字节数组，
    for i in range(0, len(data), 2):
        send_data = b''.join(
            [send_data, struct.pack('B', int(data[i: i + 2], 16))])
    # print('数据长度：'+str(len(send_data)))
    # print(send_data)

    # 通过socket广播出去，为避免失败，间隔广播三次
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s = sock.sendto(send_data, (BROADCAST, 7))
        # print(s)
        time.sleep(1)
        s = sock.sendto(send_data, (BROADCAST, 7))
        # print(s)
        time.sleep(1)
        s = sock.sendto(send_data, (BROADCAST, 7))
        # print(s)
        # return HttpResponse()
        print("Done，{}，{}，{}".format(name, ip, mac))
    except Exception as e:
        # return HttpResponse()
        print("异常：{}，{}，{}，{}".format(e, name, ip, mac))


if __name__ == '__main__':
    iplist = [
        # 格式：姓名、IP地址、MAC地址
        ['张三', '132.115.122.101', '4f-d1-9a-62-c0-f6'],
        ['李四', '132.115.123.102', '5a-1f-c3-a7-94-20']
    ]
    mode = 2  # 1=全部开机,2=指定设备开机【按姓名】,3=按ip和mac
    name = '张三'  # 模式2时才生效

    if mode == 1:
        for item in iplist:
            if item[2] == '':
                continue
            wake_up(item[0], item[1], item[2])
    elif mode == 2:
        for item in iplist:
            if item[0] == name:
                wake_up(item[0], item[1], item[2])
                break
    else:
        wake_up(ip='132.115.250.122', mac='00-D8-61-62-AB-3F')
