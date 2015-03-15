
import struct
import sys

#-------------------------------------------------------------------------------

def bytes_per_record(record_type):

    if record_type == 'f': return 4
    if record_type == 'd': return 8
    if record_type == 'i': return 4

    sys.stderr.write('unknown record_type\n')
    sys.exit(-1)

#-------------------------------------------------------------------------------

def read_record(f, record_type, length):

    # starting marker
    struct.unpack('i', f.read(4))

    x = []
    for i in range(length):
        x.append(struct.unpack(record_type, fin.read(bytes_per_record(record_type)))[0])

    # end marker
    struct.unpack('i', f.read(4))

    return x

#-------------------------------------------------------------------------------

def write_record(f, record_type, array):

    # starting marker
    f.write(struct.pack('i', bytes_per_record(record_type)*len(array)))

    for b in array:
        f.write(struct.pack(record_type, b))

    # read end marker
    f.write(struct.pack('i', bytes_per_record(record_type)*len(array)))

#-------------------------------------------------------------------------------

with open('double.dat', mode='rb') as fin:
    with open('single.dat', mode='wb') as fout:

        x = read_record(f=fin, record_type='d', length=4)
        write_record(f=fout, record_type='f', array=x)

        x = read_record(f=fin, record_type='i', length=4)
        write_record(f=fout, record_type='i', array=x)

        x = read_record(f=fin, record_type='d', length=4)
        write_record(f=fout, record_type='f', array=x)
