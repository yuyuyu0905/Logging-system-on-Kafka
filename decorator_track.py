import json
from inspect import getargspec
import getpass
from socket import socket,gethostname,AF_INET,SOCK_DGRAM

username = getpass.getuser()
hostname = gethostname()
address = ('localhost', 6005)
client_socket = socket(AF_INET, SOCK_DGRAM)


def decorator_send(func):
    def param(*my_args,**my_params):
        result=func(*my_args,**my_params)
        para_name = getargspec(func)[0]
        posparams=getargspec(func)[1] if getargspec(func)[1] else 'pargs'
        kwparams=getargspec(func)[2] if getargspec(func)[2] else 'kargs'
        dictionary={}
        l_myargs=len(my_args)
        j=0
        for i in range(len(para_name)):
            if i>=l_myargs:
                dictionary[para_name[i]] = getargspec(func)[3][j]
                j+=1
            else:
                dictionary[para_name[i]]=my_args[i]
        dictionary[posparams] = my_args[i+1:]
        if 'cls' in dictionary:
            dictionary.pop('cls')
        elif 'self' in dictionary:
            dictionary.pop('self')
        try:
            data = json.dumps({
                'category': 'sdk',
                'action': str(func).split()[1],
                'params': dictionary,
                kwparams: my_params,
                'hostname': hostname,
                'username': username
            })
            client_socket.sendto(data, address)
        except:
            print 'pass'
            pass
        return result
    return param
