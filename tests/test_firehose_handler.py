import logging
import unittest
from unittest.mock import patch
from kinesis_log_handler.firehose import FirehoseHandler, FirehoseJSONFormatter


class TestFirehoseHandler(unittest.TestCase):

    @patch('boto3.client')
    @patch('kinesis_log_handler.firehose.FirehoseHandler.emit')
    def test_emit_called(self, mock_emit, boto_client):
        boto_client.return_value = object
        mock_emit.return_value = None

        logger = logging.getLogger('firehose')
        logger.setLevel(logging.INFO)

        fh = FirehoseHandler()
        assert isinstance(fh.formatter, FirehoseJSONFormatter) is True

        logger.addHandler(fh)
        logger.info('logging test')

        assert mock_emit.called is True
        assert boto_client.called is True
