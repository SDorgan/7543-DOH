from api.doh_dtos import Resolution
from resolver.database import Database
from resolver.dns_query_service import DnsQueryService
from resolver.invalid_domain import InvalidDomain


class GetDomainService:
    domain_name = None
    domain = None
    dns_query_service = None

    def __init__(self, domain_name, dns_query_service):
        self.domain_name = domain_name
        self.domain = Database.get_instance().db['domains'].get(self.domain_name)
        self.dns_query_service = dns_query_service

    def get_domain_resolution(self):
        self.check_if_exists()
        self.validate_time_to_live()
        ip = self.domain.resolve()
        return Resolution(self.domain_name, ip, self.domain.custom)

    def get_domain_by_name(self):
        self.check_if_exists()
        self.validate_time_to_live()

    def check_if_exists(self):
        if not self.domain:
            self.domain = InvalidDomain(self.domain_name)

    def validate_time_to_live(self):
        valid_domain = self.domain.is_valid()
        if not valid_domain:
            self.domain = self.dns_query_service.get_response_as_external_domain()
            Database.get_instance().db['domains'][self.domain.name] = self.domain

