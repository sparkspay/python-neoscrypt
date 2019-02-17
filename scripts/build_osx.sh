#!/bin/sh

DEFINES="-DNEOSCRYPT_OPT -DNEOSCRYPT_MINER_4WAY -DNEOSCRYPT_SHA256"

CC="gcc"
CFLAGS="-Wall -O2 -fomit-frame-pointer -fno-stack-protector"

LD="gcc"
LDFLAGS="-Wl"

cd ../src

echo "$CC $CFLAGS $DEFINES -c neoscrypt.c"
`$CC $CFLAGS $DEFINES -c neoscrypt.c`


echo "$LD $LDFLAGS -o neoscrypt neoscrypt.o"
`$LD $LDFLAGS -dynamiclib -o neoscrypt.dylib neoscrypt.o`
