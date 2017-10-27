#!/usr/bin/env python
import os
import sys
import argparse
import configparser
from appdirs import site_config_dir

sys.path.insert(0, os.path.join( os.path.dirname(__file__), '../libraries/' ) )

from project_options import ProjectOptions

import tornado

from .api_receive_application import ApiReceiveApplication


def main():
  parser = argparse.ArgumentParser(description="Bitex Api Receive application")
  parser.add_argument('-c', "--config",
                      action="store",
                      dest="config",
                      default=os.path.expanduser('~/.bitex/api_receive.ini'),
                      help='Configuration file', type=str)
  arguments = parser.parse_args()

  if not arguments.config:
    parser.print_help()
    return

  candidates = [ os.path.join(site_config_dir('bitex'), 'api_receive.ini'),
                 arguments.config ]
  config = configparser.SafeConfigParser()
  config.read( candidates )

  # Validate the whole file
  for section_name in config.sections():
    options = ProjectOptions(config, section_name)
    if not options.log or \
       not options.port or \
       not options.rpc_url or \
       not options.db_engine:
      raise RuntimeError("Invalid configuration file")

  # Start all applications
  applications = []
  for section_name in config.sections():
    options = ProjectOptions(config, section_name)

    application = ApiReceiveApplication(options, section_name)
    application.listen(options.port)
    applications.append(application)

  if applications:
    # start
    try:
      tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
      for application in applications:
        application.clean_up()

if __name__ == "__main__":
  main()
