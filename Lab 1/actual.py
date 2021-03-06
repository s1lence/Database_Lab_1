import pickle

TIME = 16
last_id_used = 0


# ABOUT *values
# *************
# values contains:
# list, name, sessions time
# list structure:
# [                                         # values[0] lvl
#   [   Theater(first_name,first_id),       #values[0][0] lvl[...]
#       Theater(second_name,second_id)   ],
#   {   first_id  : first_time,             #values[0][1] lvl[...]
#       second_id : second_time   }
# ]
# *************

class Theater( object ) :
    def __init__( self , name , id ) :
        self.name = name
        self.id = id

    def print( self , beg = '' , ends = '\n' ) :
        print( beg + '%20s' % (self.name) , end = ends )
        # print(beg+'%17s %2d' %(self.name,self.get_id()),end=ends)
    def get_id( self ) :
        return self.id


def initialise( filename ) :
    global last_id_used
    try :
        with open( filename , 'rb' ) as f :
            last_id_used = pickle.load(f)
            theaters = pickle.load( f )
            sessions = pickle.load( f )
        f.close( )
        return [ theaters , sessions ]
    except :
        last_id_used = 0
        return [ [ ] , { } ]


def go_save( *values ) :
    global last_id_used
    with open( values[ 1 ] , 'wb' ) as f :
        pickle.dump(last_id_used,f)
        pickle.dump( values[ 0 ][ 0 ] , f , pickle.HIGHEST_PROTOCOL )
        pickle.dump( values[ 0 ][ 1 ] , f , pickle.HIGHEST_PROTOCOL )
    f.close( )


def addition( *values ) :
    global last_id_used
    last_id_used += 1
    values[ 0 ][ 1 ][ last_id_used ] = values[ 2 ]
    values[ 0 ][ 0 ].append( Theater( values[ 1 ] , last_id_used ) )


def subtraction( *values ) :
    if values[ 2 ] is not None :
        values[ 0 ][ 1 ][ values[ 0 ][ 0 ][ values[ 1 ] ].get_id( ) ] = values[ 2 ]
    else :
        del values[ 0 ][ 1 ][ values[ 0 ][ 0 ][ values[ 1 ] ].get_id( ) ]
        values[ 0 ][ 0 ].remove( values[ 0 ][ 0 ][ values[ 1 ] ] )
