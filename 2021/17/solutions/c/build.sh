#!/bin/sh

set -xe

CC=cc
CFLAGS="-Wall -Wextra -std=c18 -pedantic -O2"
$CC $CFLAGS -o aoc2021_17 aoc2021_17.c