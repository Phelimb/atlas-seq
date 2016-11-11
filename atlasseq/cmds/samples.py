#! /usr/bin/env python
from __future__ import print_function
from atlasseq.graph import ProbabilisticMultiColourDeBruijnGraph as Graph
import argparse
import json
import pickle


def samples(conn_config):
    mc = Graph(storage={'redis': {"conn": conn_config,
                                  "array_size": 25000000,
                                  "num_hashes": 2}})
    out = mc.colours_to_sample_dict()
    print(json.dumps(out, indent=4))
