# -*- coding:utf-8 -*-

from ...util import Util
from .lbserver import LbServer

# module saklient.cloud.resources.lbvirtualip

class LbVirtualIp:
    ## ロードバランサの仮想IPアドレス。
    
    # (instance field) _virtual_ip_address
    
    ## @return {str}
    def get_virtual_ip_address(self):
        return self._virtual_ip_address
    
    ## VIPアドレス
    virtual_ip_address = property(get_virtual_ip_address, None, None)
    
    # (instance field) _port
    
    ## @return {int}
    def get_port(self):
        return self._port
    
    ## ポート番号
    port = property(get_port, None, None)
    
    # (instance field) _delay_loop
    
    ## @return {int}
    def get_delay_loop(self):
        return self._delay_loop
    
    ## チェック間隔 [秒]
    delay_loop = property(get_delay_loop, None, None)
    
    # (instance field) _servers
    
    ## @return {saklient.cloud.resources.lbserver.LbServer[]}
    def get_servers(self):
        return self._servers
    
    ## 実サーバ
    servers = property(get_servers, None, None)
    
    ## @ignore
    # @param {any} obj
    def __init__(self, obj):
        vip = Util.get_by_path_any([obj], ["VirtualIPAddress", "virtualIpAddress", "virtual_ip_address", "vip"])
        self._virtual_ip_address = vip
        port = Util.get_by_path_any([obj], ["Port", "port"])
        self._port = None if port is None else int(port)
        if self._port == 0:
            self._port = None
        delayLoop = Util.get_by_path_any([obj], ["DelayLoop", "delayLoop", "delay_loop", "delay"])
        self._delay_loop = None if delayLoop is None else int(delayLoop)
        if self._delay_loop == 0:
            self._delay_loop = None
        self._servers = []
        serversDyn = Util.get_by_path_any([obj], ["Servers", "servers"])
        if serversDyn is not None:
            servers = serversDyn
            for server in servers:
                self._servers.append(LbServer(server))
    
    ## @param {any} settings
    # @return {saklient.cloud.resources.lbvirtualip.LbVirtualIp}
    def add_server(self, settings):
        self._servers.append(LbServer(settings))
        return self
    
    ## @return {any}
    def to_raw_settings(self):
        servers = []
        for server in self._servers:
            servers.append(server.to_raw_settings())
        return {
            'VirtualIPAddress': self._virtual_ip_address,
            'Port': self._port,
            'DelayLoop': self._delay_loop,
            'Servers': servers
        }
    
