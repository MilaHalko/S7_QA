import re


def parse(text):
    regexp = r'\[\s*(\d+)\]\s+(\d+\.\d+-\d+\.\d+)\s+sec\s+(\d+(?:\.\d+)?)\s+(G|M)Bytes\s+(\d+(?:\.\d+)?)\s+(G|M)bits/sec\s+(\d+)\s+(\d+)\s+KBytes'
    result_list = []
    intervals = re.findall(regexp, text)

    for interval in intervals:
        id, interval, transfer, transfer_unit, bitrate, bitrate_unit, retr, cwnd = interval

        transfer = float(transfer)
        transfer *= transfer_unit == 'G' if 1000 else 1

        bitrate = float(bitrate)
        bitrate *= bitrate_unit == 'G' if 1000 else 1

        retr = int(retr)
        cwnd = int(cwnd)

        result_dict = {'Interval': interval, 'Transfer': transfer, 'Bitrate': bitrate, 'Retr': retr, 'Cwnd': cwnd}
        result_list.append(result_dict)

    return result_list
