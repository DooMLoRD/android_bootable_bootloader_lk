#!/bin/sh

if [ -z "$1" ]; then
    outfile=lk.elf
else
    outfile=$1
fi

make msm8960

if [ ! -f "build-msm8960/lk.bin" ]; then
   echo "Build Failed"
   exit
fi

python mkelf.py -o $outfile build-msm8960/lk.bin@0x80208000 RPM.bin@0x20000,rpm

# Delete the file used to build elf so that script can tell if 
# the build failed on the next invocation.
rm build-msm8960/lk.bin
