"""
# without using inheritance


class ChineseChef:
    def make_chicken( self ):
        print(" The Chef makes chicken.")

    def make_salad( self ):
        print(" The Chef makes Salad.")

    def make_special_dish( self ):
        print(" The Chef makes Sheek Kababs.")

    def make_friedRice( self ):
        print(" The Chef makes Fried Rice. ")


"""

# with INHERITANCE


from Chef import Chef


class ChineseChef ( Chef ):

    def make_special_dish ( self ):
        print ( " The Chef makes Sheek Kababs." )

    def make_friedRice ( self ):
        print ( " The Chef makes Fried Rice. " )
