# function for creation console menu
import actual

SMALL_SPACE = ' ' * 10
BIG_SPACE = ' ' * 20
clear = lambda : print( ' \n')


def menu( data ) :
    while True :
        title( )
        ch = input( )
        clear( )
        if ch == '1' :
            if data == [ [ ] , { } ] :
                print( SMALL_SPACE + 'Database is empty.' )
            else :
                print( BIG_SPACE + SMALL_SPACE + 'Database' )
                print( SMALL_SPACE + '_' * 46 )
                print( SMALL_SPACE + '| Name of the theater  |  Session start time |' )
                print( SMALL_SPACE + '_' * 46 )
                for item in data[ 0 ] :
                    item.print( beg = SMALL_SPACE + '| ' , ends = ' | ' )
                    print( '%20d|' % data[ 1 ][ item.get_id( ) ] )
                print( SMALL_SPACE + '_' * 46 )
                # print(SMALL_SPACE + 'Last id used is equal to: %d.' % actual.last_id_used)
                print( '\n\n\n' )
        elif ch == '3' :
            session( data )
        elif ch == '4' :
            return [ 'EXT' ]
        elif ch == '2' :
            clear( )
            while True :
                print(
                        BIG_SPACE + 'Change database\n' + SMALL_SPACE + '1. Add new theater\n' + SMALL_SPACE + '2. \
Delete current theater\n' + SMALL_SPACE + '3. Change sessions\n' + SMALL_SPACE + '4. Back to main menu\n' + ' \
Please, choose one of this options(enter the correct number): ' )
                ch = input( )
                clear( )
                if ch == '4' :
                    break
                elif ch == '1' :
                    val = [ 'ADD' , data ]
                    val += plus( )
                    return val
                elif data == [ [ ] , { } ] and ch != '1' :
                    print(
                            SMALL_SPACE + 'While database is empty this option is not available. \
Please, choose the first option.' )
                elif ch == '2' :
                    val = [ 'SUB' ]
                    val += minus( data , False )
                    return val
                elif ch == '3' :
                    val = [ 'CHG' ]
                    val += minus( data )
                    return val
                else :
                    print( '\nYou have entered wrong number!\nPlease, choose more carefully this time.\n' )
        else :
            print( '\nYou have entered wrong number!\nPlease, choose more carefully this time.\n' )


def title( ) :
    print(
            BIG_SPACE + 'Main menu\n' + SMALL_SPACE + '1. Print database\n' + SMALL_SPACE + '2. \
Change database\n' + SMALL_SPACE + '3. \
Print the list of theaters where sessions begins from %d o\'clock.\n' % actual.TIME + SMALL_SPACE + '4. \
Exit\n' + 'Please, choose one of this options(enter the correct number): ' )


def plus( ) :
    clear( )
    print( BIG_SPACE + 'Adding new database element\n' + SMALL_SPACE + 'Enter the name of movie theater: ' )
    name = input( )
    clear( )
    while True :
        print( BIG_SPACE + 'Enter the session time for "%s".' % name )
        print( 'Sessions starts at(enter number from 0 to 24 hours):' )
        try :
            time = int( input( ) )
            if time not in range( 0 , 24 ) :
                raise ValueError( 'shit happens' )
        except :
            clear( )
            print( '\nYou have entered wrong time! Please, enter correct time value.\n' )
        else :
            return [ name , time ]


def minus( data , flag = True ) :
    clear( )
    if flag :
        sym = ' change'
    else :
        sym = ' delete'
    while True :
        print( SMALL_SPACE + 'Choose element which you want to' + sym + '(enter number):' )
        print( SMALL_SPACE + '_' * 49 )
        i = 1
        for item in data[ 0 ] :
            print( SMALL_SPACE + '%d.' % i , end = ' ' )
            item.print( beg = '| ' , ends = ' | ' )
            print( '%20d|' % data[ 1 ][ item.get_id( ) ] )
            i += 1
        print( SMALL_SPACE + '_' * 49 )
        try :
            num = int( input( ) )
            if num not in range( 0 , i ) :
                raise ValueError( 'shit happens' )
        except :
            clear( )
            print( '\nYou have entered wrong number! Please, enter correct value.\n' )
        else :
            if not flag :
                return [ data , num - 1 , None ]
            while True :
                print( SMALL_SPACE + 'Enter the new value of time(enter number from 0 to 24 hours):' )
                try :
                    time = int( input( ) )
                    if time not in range( 0 , 24 ) :
                        raise ValueError( 'shit happens' )
                except :
                    clear( )
                    print( '\nYou have entered wrong number! Please, enter correct value.\n' )
                else :
                    return [ data , num - 1 , time ]


def session( data ) :
    f = True
    print( SMALL_SPACE + 'Print the list of theaters where sessions begins from %d o\'clock.\n' % actual.TIME )
    print( SMALL_SPACE + '_' * 46 )
    print( SMALL_SPACE + '| Name of the theater  |  Session start time |' )
    print( SMALL_SPACE + '_' * 46 )
    for item in data[ 0 ] :
        if data[ 1 ][ item.get_id( ) ] >= actual.TIME :
            item.print( beg = SMALL_SPACE + '| ' , ends = ' | ' )
            print( '%20d|' % data[ 1 ][ item.get_id( ) ] )
            if f :
                f = not f
    if not f :
        print( SMALL_SPACE + '_' * 46 )
    else :
        print( SMALL_SPACE + 'There is no theaters where sessions began from %d o\'clock.' % actual.TIME )
    print( '\n\n\n' )
