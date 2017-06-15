from . table_io import make_table
from .. reco import nh5           as table_formats


def kr_writer(hdf5_file, *, compression='ZLIB4'):
    kr_table = make_table(hdf5_file,
                          group='DST',
                          name='Events',
                          fformat=table_formats.KrTable,
                          description='KDST Events',
                          compression=compression)
    #kr_table = _make_kr_tables(file, compression)
    def write_kr(kr_event):
        kr_event.store(kr_table)
    return write_kr


def xy_writer(hdf5_file, *, compression='ZLIB4'):
    xy_table = make_table(hdf5_file,
                          group='Corrections',
                          name='XYcorrections',
                          fformat=table_formats.XYfactors,
                          description='x,y corrections',
                          compression=compression)
    
    def write_xy(xs, ys, fs, us, ns):
        row = xy_table.row
        for i, x in enumerate(xs):
            for j, y in enumerate(ys):
                row["x"]           = x
                row["y"]           = y
                row["factor"]      = fs[i,j]
                row["uncertainty"] = us[i,j]
                row["nevt"]        = ns[i,j]
                row.append()
    return write_xy
