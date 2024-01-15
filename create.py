import sys


url = sys.argv[1]
fn = url.split('/')[-3].replace('-', '_') + '.py'
with open(fn, 'wt') as f:
    f.write('"""\n')
    f.write(url + '\n')
    f.write('"""\n')
