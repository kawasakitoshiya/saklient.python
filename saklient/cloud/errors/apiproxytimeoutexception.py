# -*- coding:utf-8 -*-

from ...errors.httpgatewaytimeoutexception import HttpGatewayTimeoutException

# module saklient.cloud.errors.apiproxytimeoutexception

class ApiProxyTimeoutException(HttpGatewayTimeoutException):
    ## APIプロクシがタイムアウトしました。サーバが混雑している可能性があります。
    
    # (class field) default_message = "APIプロクシがタイムアウトしました。サーバが混雑している可能性があります。"
    
    pass