#!/usr/bin/python3
'''module for script to parse HTTP request logs
'''
import re


def input_extraction(input_line):
    '''This will extract some snippets from an HTTP request log
    '''
    file_path = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    information_ = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(file_path[0], file_path[1], file_path[2], file_path[3], file_path[4])
    rsp_mtc = re.fullmatch(log_fmt, input_line)
    if rsp_mtc is not None:
        status_code = rsp_mtc.group('status_code')
        file_size = int(rsp_mtc.group('file_size'))
        information_['status_code'] = status_code
        information_['file_size'] = file_size
    return information_


def stats_print(file_totalSize, status_codes_stats):
    '''This will print all stats of HTTP request log
    '''
    print('File size: {:d}'.format(file_totalSize), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        number_ = status_codes_stats.get(status_code, 0)
        if number_ > 0:
            print('{:s}: {:d}'.format(status_code, number_), flush=True)


def metricsUpdate(line, file_totalSize, status_codes_stats):
    '''This will update metrics from a HTTP request log
    '''
    line_information_ = input_extraction(line)
    status_code = line_information_.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return file_totalSize + line_information_['file_size']


def run():
    '''Starts the log parser.
    '''
    line_number_ = 0
    file_totalSize = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            file_totalSize = metricsUpdate(
                line,
                file_totalSize,
                status_codes_stats,
            )
            line_number_ += 1
            if line_number_ % 10 == 0:
                stats_print(file_totalSize, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        stats_print(file_totalSize, status_codes_stats)


if __name__ == '__main__':
    run()
