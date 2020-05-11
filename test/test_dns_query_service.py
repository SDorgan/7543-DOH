from unittest import TestCase

from resolver.dns_query_service import DnsQueryService
from test import utils
from test.mock_dns_response import MockDnsResponse


class TestDnsQueryService(TestCase):

    def test_assign_query_response_to_domain(self):
        time_to_live = 1
        resolver_mock = MockDnsResponse.mock_with(1, time_to_live, utils.DEFAULT_DOMAIN_IP_1)
        dns_query_service = DnsQueryService(utils.DEFAULT_DOMAIN_NAME, resolver_mock)
        external_domain = dns_query_service.get_response_as_external_domain()
        assert external_domain.time_to_live == time_to_live
        assert external_domain.name == utils.DEFAULT_DOMAIN_NAME
        assert external_domain.associated_ips[0] == utils.DEFAULT_DOMAIN_IP_1
