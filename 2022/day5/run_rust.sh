#!/bin/bash

set -xe

rustc part1.rs && ./part1 && rm -f part1
