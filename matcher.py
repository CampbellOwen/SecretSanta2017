import json
import random


class Secret_Santa_Matcher:


    def __init__( self, participants, seed ):
        self.people = {}
        for person in participants:
            self.people[ person ] = [ p for p in participants if not p == person and p not in participants[ person ][ 'ban-list' ] ] 


        self.seed = seed

    def set_seed( self, seed ):
        self.seed = seed

    def match( self ):
        random.seed( self.seed )
        givers = [ p for p in self.people ]
        receivers = [ p for p in self.people ]
        matches = {}
        tries = 0
        while givers and tries <= len( self.people ) * 2:
            tries += 1
            index = random.randint( 0, len( givers ) - 1 )
            first = givers.pop( index )

            index = random.randint( 0, len( receivers ) - 1 )

            count = 0
            while receivers[ index ] not in self.people[ first ] and count <= len( self.people ):
                index = random.randint( 0, len( receivers ) - 1 )
                count += 1

            if count > len( self.people ):
                givers.append( first )
                continue

            second = receivers.pop( index )

            matches[ first ] = second
        if tries > len( self.people ) * 2:
           return self.match()

        return matches

    @staticmethod
    def from_file( filepath ):
        participants = {}
        with open( filepath, 'r' ) as participants_file:
            participants = json.loads( participants_file.read() )[ 'participants' ]
        return Secret_Santa_Matcher( participants, None )



