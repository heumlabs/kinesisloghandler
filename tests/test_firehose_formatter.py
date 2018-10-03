import json
import logging
import unittest
from kinesis_log_handler.firehose import FirehoseJSONFormatter


class TestFirehoseFormatter(unittest.TestCase):

    def test_json_format(self):
        with self.assertLogs('firehose', level='INFO') as thlg:
            logger = logging.getLogger('firehose')
            logger.setLevel(logging.INFO)
            logger.info('logging test')

            json_fmt = FirehoseJSONFormatter()

            for record in thlg.records:
                jsonify_str = json_fmt.format(record)
                assert isinstance(jsonify_str, str)

                record_dict = json.loads(jsonify_str)
                assert isinstance(record_dict, dict)
                assert 'platform' in record_dict
