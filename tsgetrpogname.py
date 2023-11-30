import sys

from ariblib import tsopen
from ariblib.descriptors import ShortEventDescriptor
from ariblib.sections import EventInformationSection

def show_program(eit):
    event = iter(eit.events).__next__()
    program_title = event.descriptors[ShortEventDescriptor][0].event_name_char
    d_week = {'Sun': '日', 'Mon': '月', 'Tue': '火', 'Wed': '水', 'Thu': '木', 'Fri': '金', 'Sat': '土'}
    start = event.start_time.strftime('%Y%m%d(') + d_week[event.start_time.strftime('%a')] + event.start_time.strftime(')%H%M')
    return "{} {}".format(start, program_title)

with tsopen(sys.argv[1]) as ts:

    #番組を表示する
    int_i = 0
    while True:
        EventInformationSection._table_ids = [0x4E]
        try:
            current = next(table for table in ts.sections(EventInformationSection) if table.section_number == int_i)
            print(show_program(current))
            int_i += 1
        except:
            break
