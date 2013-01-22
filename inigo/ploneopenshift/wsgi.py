from Zope2.Startup.run import make_wsgi_app
import socket

def app_factory(global_config, instances):
    instances_config = {}
    for line in instances.split('\n'):
        if not line.strip():
            continue

        name, address, zope_conf = line.strip().split()
        instances_config[name] = {
            'address': address,
            'zope_conf': zope_conf
        }

    for instance in instances_config.values():
        if is_listening(instance['address']):
            continue
        
        return make_wsgi_app(global_config, instance['zope_conf'])

    raise Exception('Failure to create worker')

def is_listening(address):
    host, port = parse_address(address)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
        return True
    except:
        return False

def parse_address(address):
    if ':' in address:
        host, port = address.strip().split(':')
        return host, int(port)
    return '127.0.0.1', int(address)

