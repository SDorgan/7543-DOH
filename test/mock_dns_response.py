class MockDnsResponse:
    response = None

    def __init__(self, response):
        self.response = response

    def query(self, _domain):
        return self

    @staticmethod
    def mock_with(rd_type=1, ttl=1, ip=None):
        item = MockDnsResponseAnswerItem(ip)
        answer = MockDnsResponseAnswer(rd_type, ttl, [item])
        answer_array = MockDnsResponseAnswerArray([answer])
        return MockDnsResponse(answer_array)


class MockDnsResponseAnswerArray:
    answer = None

    def __init__(self, answer):
        self.answer = answer


class MockDnsResponseAnswer:
    rdtype = None
    ttl = None
    items = None

    def __init__(self, rd_type, ttl, items):
        self.rdtype = rd_type
        self.ttl = ttl
        self.items = items


class MockDnsResponseAnswerItem:
    address = None

    def __init__(self, address):
        self.address = address
