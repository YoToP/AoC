#!/bin/sh

set -xe

CC=cc
CFLAGS="-Wall -Wextra"
$CC $CFLAGS -o aoc2021_2 aoc2021_2.c