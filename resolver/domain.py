from datetime import datetime


class Domain:
    name = None
    # time_to_live (minutes)
    # time_to_live=0 means it never dies
    time_to_live = None
    associated_ips = None
    creation_time = None
    custom = None

    def __init__(self, name, time_to_live):
        self.name = name
        self.time_to_live = time_to_live
        self.associated_ips = []
        self.creation_time = datetime.now()
        self.custom = False

    def add_associated_ip(self, ip):
        self.associated_ips.append(ip)

    def reset_associated_ips(self):
        self.associated_ips.clear()

    def resolve(self):
        raise Exception('To Be Defined!')

    def is_valid(self):
        raise Exception('To Be Defined!')
