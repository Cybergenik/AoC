#!/bin/bash

set -xe

rustc part2.rs && ./part2 && rm -f part2
