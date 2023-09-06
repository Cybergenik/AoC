#!/bin/bash

set -xe

rustc part1.rs && time ./part1 && rm -f part1
