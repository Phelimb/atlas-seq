#! /usr/bin/env python
from __future__ import print_function
from atlasseq.mcdbg import McDBG
import argparse
import json
import pickle


stats = {}


def run(parser, args, conn_config):
    mc = McDBG(conn_config=conn_config)
    for k in mc.kmers():
        kmer_string = mc._bytes_to_kmer(k)
        print(kmer_string, "\t".join(
            [str(i) for i in mc._byte_arrays_to_bits(mc.get_kmer(kmer_string))]))