#!/usr/bin/env python
import os
import sys

error_message = r"""
无法导入Django框架!
(1) 'PYTHONPATH'环境变量是否正确?
(2) Python虚拟环境是否正确?
"""


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(error_message) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
