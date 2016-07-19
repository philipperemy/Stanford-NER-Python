#!/usr/bin/env python

"""
A simple Python wrapper for the stanford NER binary that makes it easier to use it
on UNIX/Windows systems.
Note: The script does some minimal sanity checking of the input, but don't
    expect it to cover all cases. After all, it is a just a wrapper.
Example:
    > echo "Barack Obama was born in Hawaii." > text.txt
    > python python main.py -f text.txt
    Should display
    1.000: (Barack Obama; was; born)
    1.000: (Barack Obama; was born in; Hawaii)
Authors:    Philippe Remy       <github: philipperemy>
Version:    2016-07-08
"""

# Copyright (c) 2016, Philippe Remy <github: philipperemy>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from __future__ import print_function

import os
import pickle
from argparse import ArgumentParser
from platform import system
from subprocess import Popen
from sys import argv
from sys import stderr

IS_WINDOWS = True if system() == 'Windows' else False
JAVA_BIN_PATH = 'java.exe' if IS_WINDOWS else 'java'
STANFORD_NER_FOLDER = 'stanford-ner'


def arg_parse():
    arg_p = ArgumentParser('Stanford NER Python Wrapper')
    arg_p.add_argument('-f', '--filename', type=str, default=None)
    arg_p.add_argument('-v', '--verbose', action='store_true')
    return arg_p


def debug_print(log, verbose):
    if verbose:
        print(log)


def process_entity_relations(entity_relations_str, verbose=True):
    # format is ollie.
    entity_relations = list()
    for s in entity_relations_str:
        entity_relations.append(s[s.find("(") + 1:s.find(")")].split(';'))
    return entity_relations


def stanford_ner(filename, verbose=True, absolute_path=None):
    out = 'out.txt'

    command = ''
    if absolute_path is not None:
        command = 'cd {};'.format(absolute_path)
    else:
        filename = '../{}'.format(filename)

    command += 'cd {}; {} -mx1g -cp "*:lib/*" edu.stanford.nlp.ie.NERClassifierCombiner ' \
               '-ner.model classifiers/english.all.3class.distsim.crf.ser.gz ' \
               '-outputFormat tabbedEntities -textFile {} > ../{}' \
        .format(STANFORD_NER_FOLDER, JAVA_BIN_PATH, filename, out)

    if verbose:
        debug_print('Executing command = {}'.format(command), verbose)
        java_process = Popen(command, stdout=stderr, shell=True)
    else:
        java_process = Popen(command, stdout=stderr, stderr=open(os.devnull, 'w'), shell=True)
    java_process.wait()
    assert not java_process.returncode, 'ERROR: Call to stanford_ner exited with a non-zero code status.'

    if absolute_path is not None:
        out = absolute_path + out

    with open(out, 'r') as output_file:
        results_str = output_file.readlines()
    os.remove(out)

    results = []
    for res in results_str:
        if len(res.strip()) > 0:
            split_res = res.split('\t')
            entity_name = split_res[0]
            entity_type = split_res[1]

            if len(entity_name) > 0 and len(entity_type) > 0:
                results.append([entity_name.strip(), entity_type.strip()])

    if verbose:
        pickle.dump(results_str, open('out.pkl', 'w'))
    debug_print('wrote to out.pkl', verbose)
    return results


def main(args):
    arg_p = arg_parse().parse_args(args[1:])
    filename = arg_p.filename
    verbose = arg_p.verbose
    print(arg_p)
    if filename is None:
        print('please provide a text file containing your input. Program will exit.')
        exit(1)
    if verbose:
        debug_print('filename = {}'.format(filename), verbose)
    entities = stanford_ner(filename, verbose)
    print(entities)


if __name__ == '__main__':
    exit(main(argv))
