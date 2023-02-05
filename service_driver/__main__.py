from __future__ import absolute_import
import sys
from os.path import dirname

sys.path.append(dirname(sys.path[0]))
from service_driver.project_generator import command

command()
