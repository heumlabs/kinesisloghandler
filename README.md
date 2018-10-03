# Kinesis Log Handler

[![Build Status](https://travis-ci.com/neillab/kinesis_log_handler.svg?branch=master)](https://travis-ci.com/neillab/kinesis_log_handler)
[![codecov](https://codecov.io/gh/neillab/kinesis_log_handler/branch/master/graph/badge.svg)](https://codecov.io/gh/neillab/kinesis_log_handler)

Python logging handler for sending logs to AWS Kinesis

# Requirements

- Python 3.5+
- boto3

# Installation
Install and update using pip
```bash
pip install -U kinesis-log-handler
```

# A Simple Example
```python
import logging
from kinesis_log_handler.firehose import FirehoseHandler

logger = logging.getLogger('neil')
fh = FirehoseHandler(region_name='ap-northeast-1')
logger.addHandler(fh)

logger.warning('Warning!')
```

# TODO
> - Emit asynchronously
