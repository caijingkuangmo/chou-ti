# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os
from __init__ import create_app

app = create_app()


if __name__ == "__main__":
    host_port = int(os.environ.get('host_port', 8887))
    app.run(port=host_port, debug=app.debug, threaded=True)