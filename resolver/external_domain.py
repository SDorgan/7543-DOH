from datetime import datetime

from resolver.domain import Domain


class ExternalDomain(Domain):
    next_ip_index = None
    SECONDS_IN_A_MINUTE = 60

    def __init__(self, name, time_to_live):
        if time_to_live == 0:
            raise Exception('External Domain cannot have infinite time to live')
        Domain.__init__(self, name, time_to_live)
        self.next_ip_index = 0

    def resolve(self):
        ip = self.associated_ips[self.next_ip_index]
        self.update_next_ip_index()

        return ip

    def update_next_ip_index(self):
        associated_ips_len = len(self.associated_ips)
        if associated_ips_len > 1:
            limit_index = associated_ips_len - 1
            if self.next_ip_index == limit_index:
                self.next_ip_index = 0
            else:
                self.next_ip_index = self.next_ip_index + 1

    def is_valid(self):
        domain_minutes_with_life = (datetime.now() - self.creation_time).total_seconds() / self.SECONDS_IN_A_MINUTE
        return self.time_to_live > domain_minutes_with_life
