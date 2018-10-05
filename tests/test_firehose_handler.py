import logging
import unittest
from unittest.mock import patch
from kinesis_log_handler.firehose import FirehoseHandler, FirehoseJSONFormatter


class MockClientSuccess(object):
    def put_record(DeliveryStreamName, Record):
        return True


class TestFirehoseHandler(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger('firehose')
        self.logger.setLevel(logging.INFO)

    @patch('boto3.client')
    def test_emit_called(self, boto_client):
        boto_client.return_value = MockClientSuccess

        with self.assertLogs(self.logger) as thlg:
            fh = FirehoseHandler(delivery_stream_name='test_stream',
                                 region_name='ap-northeast-1')
            assert boto_client.called is True
            assert isinstance(fh.formatter, FirehoseJSONFormatter) is True

            self.logger.addHandler(fh)
            self.logger.info('logging test')

            for record in thlg.records:
                fh_record = fh.get_firehose_record(record)
                assert 'Data' in fh_record
