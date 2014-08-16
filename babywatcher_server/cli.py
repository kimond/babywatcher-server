# -*- coding: utf-8 -*-
import sys
from server import BabyWatcherServer
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Babywatcher server cli")
    subparsers = parser.add_subparsers(title='Server commands', description='Server commands')
    #Commande a parser
    start_server = subparsers.add_parser('start-server', help="Start the server")
    start_server.set_defaults(action="start_server")
    stop_server = subparsers.add_parser('stop-server', help="Stop the server")
    stop_server.set_defaults(action="stop_server")
    restart_server = subparsers.add_parser('restart-server', help="Restart the server")
    restart_server.set_defaults(action="restart_server")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    #Init server
    server = BabyWatcherServer("/tmp/babywatcher.pid")
    try:
        if not hasattr(args, 'action'):
            parser.print_help()
        elif args.action == "start_server":
            server.start()
        elif args.action == "stop_server":
            server.stop()
        elif args.action == "restart_server":
            server.restart()
    except KeyboardInterrupt:
        pass
if __name__ == "__main__":
    main()
