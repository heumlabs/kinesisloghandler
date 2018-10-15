Kinesis Log Handler
===================

|Build Status| |codecov|

Python logging handler for sending logs to AWS Kinesis

Requirements
============

-  Python 3.5+
-  boto3

Installation
============

Install and update using pip

.. code:: bash

    pip install -U kinesisloghandler

A Simple Example
================

.. code:: python

    import logging
    from kinesis_log_handler.firehose import FirehoseHandler

    logger = logging.getLogger('neil')
    fh = FirehoseHandler(
        delivery_stream_name='your_kinesis_stream_name',
        region_name='ap-northeast-1')
    logger.addHandler(fh)

    logger.warning('Warning!')

TODO
====

    -  Emit asynchronously

.. |Build Status| image:: https://travis-ci.com/neillab/kinesisloghandler.svg?branch=master
   :target: https://travis-ci.com/neillab/kinesisloghandler
.. |codecov| image:: https://codecov.io/gh/neillab/kinesis_log_handler/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/neillab/kinesis_log_handler
