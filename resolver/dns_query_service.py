import dns.resolver

from resolver.external_domain import ExternalDomain


class DnsQueryService:
    dns_resolver = None
    domain_name = None
    RD_TYPE_A = 1

    def __init__(self, domain_name, dns_resolver=dns.resolver):
        self.dns_resolver = dns_resolver
        self.domain_name = domain_name

    def get_response_as_external_domain(self):
        response = self.dns_resolver.query(self.domain_name).response
        answer = list(filter(lambda response_answer: response_answer.rdtype == self.RD_TYPE_A, response.answer))[0]

        domain = ExternalDomain(self.domain_name, answer.ttl)
        for item in answer.items:
            domain.add_associated_ip(item.address)

        return domain
