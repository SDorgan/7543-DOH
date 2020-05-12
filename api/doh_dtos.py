#  DTOs (DATA TRANSFER OBJECTS)


class Resolution:
    domain = None
    ip = None
    custom = None

    def __init__(self, domain, ip, custom):
        self.domain = domain
        self.ip = ip
        self.custom = custom

    def serialize(self):
        return {
            'domain': self.domain,
            'ip': self.ip,
            'custom': self.custom,
        }


class Error:
    error = None

    def __init__(self, error):
        self.error = error

    def serialize(self):
        return {
            'error': self.error
        }
