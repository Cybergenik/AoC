#!/bin/bash

set -xe

rustc part2.rs && time ./part2 && rm -f part2
