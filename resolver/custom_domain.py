from resolver.domain import Domain


class CustomDomain(Domain):

    def __init__(self, name):
        Domain.__init__(self, name, 0)

    def add_associated_ip(self, ip):
        if self.associated_ips:
            raise Exception('Custom Domain already exist with an IP')
        super().add_associated_ip(ip)

    def resolve(self):
        return self.associated_ips[0]

    def is_valid(self):
        return True
