"""
Firehose logging handler and default Formattter
"""

import logging
import platform
import json
import boto3


class FirehoseHandler(logging.Handler):
    def __init__(self,
                 level=logging.INFO,
                 delivery_stream_name=None,
                 **kwargs):
        """
        Use FirehoseJSONFormatter as the default logging formatter

        additional kwargs of boto3
            service_name
            region_name
            aws_access_key_id
            aws_secret_access_key
            aws_session_token
        """
        super(FirehoseHandler, self).__init__(level=level)
        self.setFormatter(FirehoseJSONFormatter())
        self.setLevel(level)
        self._delivery_stream_name = delivery_stream_name
        self._client = boto3.client('firehose', region_name='ap-northeast-1')

    def emit(self, record):
        data = {
            'Data': self.format(record),
        }
        try:
            self._client.put_record(
                DeliveryStreamName=self._delivery_stream_name,
                Record=data
            )
        except Exception:
            self.handleError(record)


class FirehoseJSONFormatter(logging.Formatter):
    """
    default JSON log formatter
    """
    def __init__(self, ensure_ascii=False):
        self._platform_dict = dict(platform.uname()._asdict())
        self._ensure_ascii = ensure_ascii

    def jsonify(self, log_record):
        return json.dumps(log_record, ensure_ascii=self._ensure_ascii)

    def format(self, record):
        data = {}
        for key, value in record.__dict__.items():
            if key == 'exc_info' and value is not None:
                value = self.formatException(value)
            else:
                data[key] = value
        # Add platform info
        data.update({'platform': self._platform_dict})
        return self.jsonify(data)
