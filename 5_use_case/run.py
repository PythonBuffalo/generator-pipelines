import pprint
import os

from filter_pipeline import FilterPipeline


def strip_lines(lines):
    for line in lines:
        yield line.strip()


def remove_empty(lines):
    for line in lines:
        if line:
            yield line


def to_lower(lines):
    for line in lines:
        yield line.lower()


def to_dict(lines):
    for line in lines:
        parts = line.split('\t')
        yield dict(part.split('=', 1) for part in parts)


def remove_pastrami_subject(lines):
    for line in lines:
        if 'pastrami' not in line['subject']:
            yield line

pipeline = FilterPipeline()
pipeline.add_filter(strip_lines)
pipeline.add_filter(remove_empty)
pipeline.add_filter(to_lower)
pipeline.add_filter(to_dict)
pipeline.add_filter(remove_pastrami_subject)

this_dir = os.path.dirname(__file__)
fp = open(os.path.abspath(os.path.join(this_dir, './test.tsv')))
for line in pipeline.read(fp):
    pprint.pprint(line)
