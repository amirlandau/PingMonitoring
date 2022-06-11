import platform
import subprocess
from ping3 import ping


# Pinging an IP address in a reliable way, used for monitoring by update_ip_status() function.
def reliable_ping(host):
    status = ping(host)

    if type(status) != float and type(status) != int:
        status = False
    else:
        status = True

    return status

# Pinging an IP address in a fast way, used for adding or updating a server.
def fast_ping(host):
    status = ping(host, timeout=0.6)

    if type(status) != float and type(status) != int:
        status = False
    else:
        status = True

    return status