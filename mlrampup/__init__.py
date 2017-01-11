# -*- coding: utf-8 -*-
import pkg_resources
import logging
from os import path
from logging.config import fileConfig

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'


print()

logger = logging.getLogger(__name__)
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
print(log_file_path)
fileConfig(log_file_path)
logger.setLevel(level=logging.DEBUG)
