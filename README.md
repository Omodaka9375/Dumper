# Dumper
Capture a Memory Dump of any Process via PID using ProcDump and PsUtil

## How it works

It uses sysinternal tools like procdump and psutil to safely capture a memory dump of any running process.

## How to use it

`dumper.py <PID>` - suspend, dump, resume PID

`dumper.py <PID> --kill True` - suspend, dump, kill PID

eg. `dumper.py 1234 --kill True`
