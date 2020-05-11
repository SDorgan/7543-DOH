from resolver.domain import Domain


class InvalidDomain(Domain):

    def __init__(self, name):
        Domain.__init__(self, name, 0)

    def add_associated_ip(self, ip):
        raise Exception('Invalid Domain cannot add IPs')

    def resolve(self):
        raise Exception('Invalid Domain cannot resolve')

    def is_valid(self):
        return False
