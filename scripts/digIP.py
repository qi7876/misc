import socket


def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        return str(e)


# 示例用法
domain = "prob00-4a655c067bc3391e61c369c8ab5f761d.recruit.yulinsec.cn"
ip = get_ip(domain)
print(f"域名 {domain} 对应的 IP 地址是: {ip}")
