#!/usr/bin/python
#
# Bump symbol versions of libvirt0

# Usage: ./bump-symbol-versions 1.2.16~rc2

import os
import re
import sys
import shutil
import subprocess

#import gbp.git.GitRepository

symbols_file = 'debian/libvirt0.symbols'
symbols_new_file = symbols_file + '.new'

symbols = open(symbols_file)
symbols_new = open('%s.new' % symbols_file, 'w+')

if len(sys.argv) != 2:
    print >>sys.stderr, "Need a version"
    sys.exit(1)

version = sys.argv[1]
s_version = version.split('~', 1)[0]

for line in symbols.readlines():
    m = re.match('(?P<pre>.*LIBVIRT_(?P<admin>ADMIN_)?PRIVATE_)(?P<v>[a-z0-9.]+) ',
                 line)
    if m:
        if not m.group('admin'):
            symbols_new.write(' *@LIBVIRT_%s %s\n' % (s_version, version))
        symbols_new.write("%s%s %s\n" %
                          (m.group('pre'), s_version, version))
    else:
        symbols_new.write(line)


symbols.close()
symbols_new.close()

os.unlink(symbols_file)
shutil.move(symbols_new_file, symbols_file)
subprocess.call(['git', 'commit', '-m', 'Bump symbol versions', symbols_file])

