from unittest import TestCase

from resolver.database import Database
from resolver.dns_query_service import DnsQueryService
from resolver.get_domain_service import GetDomainService
from test import utils
from test.mock_dns_response import MockDnsResponse


class TestGetDomainService(TestCase):

    def tearDown(self):
        super().tearDown()
        Database.get_instance().db = {'domains': {}}

    def test_resolve_for_custom_domain(self):
        domain = utils.persist_custom_domain()
        resolver = GetDomainService(domain.name, DnsQueryService(domain.name))
        assert resolver.get_domain_resolution().ip == domain.associated_ips[0]

    def test_resolve_for_external_domain_with_one_ip(self):
        resolver_mock = MockDnsResponse.mock_with(1, 1, utils.DEFAULT_EXTERNAL_DOMAIN_IP_1)
        dns_query_service = DnsQueryService(utils.DEFAULT_DOMAIN_NAME, resolver_mock)
        resolver = GetDomainService(utils.DEFAULT_DOMAIN_NAME, dns_query_service)
        assert resolver.get_domain_resolution().ip == utils.DEFAULT_EXTERNAL_DOMAIN_IP_1

    def test_resolve_for_multiple_queries_external_domain_with_one_ip(self):
        domain = utils.persist_external_domain_with_one_ip()
        resolver = GetDomainService(domain.name, DnsQueryService(domain.name))
        assert resolver.get_domain_resolution().ip == domain.associated_ips[0]
        assert resolver.get_domain_resolution().ip == domain.associated_ips[0]

    def test_resolve_for_external_domain_with_one_ip_and_expired_ttl(self):
        domain = utils.persist_external_domain_with_one_ip()
        resolver = GetDomainService(domain.name, DnsQueryService(domain.name))
        assert resolver.get_domain_resolution().ip == utils.DEFAULT_EXTERNAL_DOMAIN_IP_1

        resolver_mock = MockDnsResponse.mock_with(1, 1, utils.DEFAULT_EXTERNAL_DOMAIN_IP_2)
        dns_query_service = DnsQueryService(utils.DEFAULT_DOMAIN_NAME, resolver_mock)
        utils.do_expire_ttl(domain)
        resolver = GetDomainService(domain.name, dns_query_service)
        new_ip = resolver.get_domain_resolution().ip
        assert not new_ip == utils.DEFAULT_EXTERNAL_DOMAIN_IP_1
        assert new_ip == utils.DEFAULT_EXTERNAL_DOMAIN_IP_2


