import socket
import struct
import fcntl
import yaml


class Config(object):

    def __init__(self):
        self.read_configs()

    def read_configs(self):
        pass

    def get_ip_address(self,ifname):
        """
        Return ip adresse from a choosen iface

        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
