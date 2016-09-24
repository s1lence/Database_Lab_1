import actual
import visual

file_name = 'info.dtb'

if __name__ == "__main__" :
    database = actual.initialise( file_name )
    ans = visual.menu( database )
    while (ans[ 0 ] != 'EXT') :
        if ans[ 0 ] == 'ADD' :
            actual.addition( ans[ 1 ] , ans[ 2 ] , ans[ 3 ] )
        else :
            actual.subtraction( ans[ 1 ] , ans[ 2 ] , ans[ 3 ] )
        ans = visual.menu( database )
    actual.go_save( database , file_name )
