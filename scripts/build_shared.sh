#!/bin/sh

DEFINES="-DNEOSCRYPT_ASM -DNEOSCRYPT_OPT -DNEOSCRYPT_MINER_4WAY -DNEOSCRYPT_SHA256"

CC="gcc"
CFLAGS="-Wall -O2 -fomit-frame-pointer -fno-stack-protector -shared"

LD="gcc"
LDFLAGS="-Wl,-s"

cd ../src

echo "$CC $CFLAGS $DEFINES -c neoscrypt.c"
`$CC $CFLAGS $DEFINES -fPIC -c neoscrypt.c -o neoscrypt.so`

