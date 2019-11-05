# AI CONTEST
## structure of recognization of entity
### CCF
- scripts
    + train class
        + import argparse
        + import math
        + import os
        + import re
        + import sys
        + import gluonlp
        + import jieba.posseg
        + import BeamSearchScorer
        + import ...
        + train_and_valid
        + dev
        + predict
        + main
    + add key entity
        * import pandas
        * PickKeyEntity
            - run
            - func_on_row
            - _generate_nike_data
            - _romove_substring
    + utils
- data
    + scripts
        * dataloader
            - import gluon
            - import gluonnlp
            - import mxnet
            - import tokenization
            - DatasetAssiantTransformer
                + ClassProcess
            - ClassDataLoader
                + _build_dataloader
                + dataiter
                + data_lengths
        * dataset
            - import gluon
            - import ArrayDataset
            - ClassDataset
                + _get_data
            - ClassTestDataset
                + _get_data
        * process
            - import itertool.islice
            - import jieba.posseg
            - import multiprocessing
            - import Counter
            - split_to_train_valid
- models
    + BertClass
        * import mxnet
        * BertClass
            - forward
-