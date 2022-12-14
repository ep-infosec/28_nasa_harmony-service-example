"""
=========
__main__.py
=========

Runs the harmony_service_example CLI
"""

import argparse
import logging
import harmony

from .transform import HarmonyAdapter


def main():
    """
    Parses command line arguments and invokes the appropriate method to respond to them

    Returns
    -------
    None
    """
    parser = argparse.ArgumentParser(
        prog='harmony_service_example', description='Run the example service')
    harmony.setup_cli(parser)
    args = parser.parse_args()
    if (harmony.is_harmony_cli(args)):
        harmony.run_cli(parser, args, HarmonyAdapter)
    else:
        parser.error("Only --harmony CLIs are supported")


if __name__ == "__main__":
    main()
