#########################################################################
def make_shirt(text,size = "Large"):
    """Make a T_shirt of the collage party"""
    print("\nThe size of my shirt is : " + size.upper())
    print("The text that need to be printed is : "  + text.title() + "!")

make_shirt(text="rock")
make_shirt("go to hell")

#########################################################################


def make_shirt(size ,text="I love Python!"):
    """Make a T_shirt of the collage party"""
    print("\nThe size of my shirt is : " + size.upper())
    print("The text that need to be printed is : "  + text.title() + "!")

make_shirt(size="xxl")
make_shirt("xxxl")


#########################################################################


def make_shirt(size,text):
    """Make a T_shirt of the collage party"""
    print("\nThe size of my shirt is : " + size.upper())
    print("The text that need to be printed is : "  + text.title() + "!")

make_shirt(size="xxl" , text="rock")
make_shirt("xxxl" , "go to hell")
make_shirt(text="rock", size="xxl")


#########################################################################