import socket

def is_internet_alive(host="8.8.8.8", port=53, timeout=3):
    """Check if Internet Connection is alive and external IP address is reachable.

    Input Parameters:
        host: (string) 8.8.8.8 (google-public-dns-a.google.com)
        port: (integer) (53/tcp DNS Service).
        timeout: (float) timeout in seconds.

    Returns:
        True (Boolean) if external IP address is reachable.
        False (Boolean) if external IP address is unreachable.
    """

    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
    except OSError:
        # print(error.strerror)
        print("Disconnected")
        return False
    else:
        s.close()
        print("Connected")
        return True