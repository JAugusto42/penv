#!/usr/bin/env python
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Manage your virtualenv")
    parser.add_argument('action', metavar='action', type=str, help='Command (create, delete, use, deactivate).')
    parser.add_argument('name', metavar='venv_name', type=str, help='Name of the virtualenv.')
    parser.add_argument('--python_path', metavar='python_path', type=str, help='Python path.')

    return parser.parse_args()