#!/bin/bash

set -xe

export PATH="$HOME/miniconda/bin:$PATH"
source $HOME/miniconda/bin/activate
#
cd tests && bash run-all.sh && cd -

