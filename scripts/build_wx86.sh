#!/bin/sh

DEFINES="-DNEOSCRYPT_OPT -DNEOSCRYPT_MINER_4WAY -DNEOSCRYPT_SHA256"

CC="i686-w64-mingw32-gcc"
CFLAGS="-Wall -O2 -fomit-frame-pointer -fno-stack-protector"

LD="i686-w64-mingw32-gcc"
LDFLAGS="-shared -W -static-libgcc -static-libstdc++" #l," #,-s"

cd ../src

echo "$CC $CFLAGS $DEFINES -c neoscrypt.c"
`$CC $CFLAGS $DEFINES -c neoscrypt.c`

echo "$LD $LDFLAGS -o neoscrypt neoscrypt.o"
`$LD $LDFLAGS -o neoscrypt.dll neoscrypt.o`
