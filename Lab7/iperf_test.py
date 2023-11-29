import parser


class TestSuite():
    def test_iperf3_client_connection(self, client):
        transfer_criteria = lambda result: result['Transfer'] >= 2
        bitrate_criteria = lambda result: result['Bitrate'] >= 20
        output, error = client

        if error:
            assert False, f"Client connection error: {error}"

        results = parser.parse(output)

        if not results:
            assert False, f"Incorrect client output"

        if not any(transfer_criteria(result) for result in results):
            assert False, f"No transfer criteria"

        if not any(bitrate_criteria(result) for result in results):
            assert False, f"No bitrate criteria"

        assert True