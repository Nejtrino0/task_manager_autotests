import os
import sys
import pathlib
from reports.report import ReportManager


def absolute_dir():
    return str(pathlib.Path(__file__).parent.absolute())[:-6]


def parse(**kwargs):
    try:
        return [_arg for _arg in sys.argv if _arg.startswith(kwargs.get('arg'))][0].split('=')[1]
    except IndexError:
        if kwargs.get('default'):
            return kwargs.get('default')
        return False


def clear_reports(*args):
    for test_type in args:
        if len(os.listdir(''.join([absolute_dir(), '/reports/{0}/reports'.format(test_type)]))) > 10:
            ReportManager('/{0}/reports/'.format(test_type)).delete()


clear_reports('ui', 'api')
