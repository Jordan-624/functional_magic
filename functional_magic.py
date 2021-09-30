'''
Goblins Magical Loan System

A sophisticated system for approving loans to wizards starting businesses.
This is an INDIVIDUAL project. Do not consult with others or share code.
Refer to the instructions on Canavs for more information.

When you pass all tests, remember to clean and document your code.
'''

## 1) Define main function
# Most students find it easier to implement this function last.
def main():
    """
    Main function that calls all the other functions and provides
    an interactive loan processing experience.
    """
    print_introduction()
    name = input_name()
    rating = calculate_rating(name)
    print_rating(rating)
    loan_amount = input_loan_amount()
    print_loan_availability(rating, loan_amount)
    print_conclusion()

## 2) Define print_introduction function

def print_introduction():
    print("* 1) Introduction ********************************")
    print("Welcome to the Goblins Magical Loan System!")
    print("Please answer the following questions truthfully,")
    print("and we will process your loan request.")
    print("Imposters will be fed to the dragons.")

## 3) Define input_name function

def input_name():
    print("* 2) Name ****************************************")
    print("Please enter your full, legal name.")
    print("Magical verification will verify your identity.")
    name = input("Write your name and press enter: ")
    print("Welcome,", name+"!")
    return name

## 5) Define print_rating function
    
def print_rating(rating):
    print("* 3) Rating **************************************")
    print("Your user rating has been calculated.")
    print("Your rating is:", str(rating)+"/10 points.")
    
    
## 6) Define input_loan_amount function

def input_loan_amount():
    print("* 4) Loan ****************************************")
    print("Loans are made based on your customer rating.")
    print("However, you can request a loan of any size.")
    print("How many galleons do you want?")
    loan_amount = input("Write your loan amount: ")
    return int(loan_amount)

## 8) Define test_loan function

def test_loan(rating, loan_amount):
    return ((rating**2) * (100)) >= loan_amount

## 7) Define print_loan_availability function

def print_loan_availability(rating, loan_amount):
    print("* 5) Available? **********************************")
    print("Your loan request has been evaluated.")
    print("Loan available: "+str(test_loan(rating, loan_amount)))

## 9) Define print_conclusion function
    
def print_conclusion():
    print("* 6) Conclusion **********************************")
    print("Thanks for using Goblins Magical Loan System!")
    print("Best of luck with your new small business.")
    print("We hope you'll use Goblins for all your future")
    print("banking needs. Remember: Fortius Quo Fidelius!")
    print("**************************************************")

## 4) Calculating Rating (already complete!)
# The following is Grindlehook's function. Do not modify it.
# You should not worry about HOW it works, but instead think of its
# arguments and return value. Remember you can only call it once!
# Do not worry that it is below the rest of your code (why does it work?).
# Do NOT change the following function definition
def calculate_rating(name):
    '''
    Returns the customer's credit rating, according to the bank's current
    status, the customer, and the alignment of the stars. This function
    is delicate, and will break after being called once.

    Notes:
        (ghook@1/15/2018): DO NOT TOUCH THIS, I FINALLY GOT IT WORKING.

    Args:
        name (str): A string representing the user's full name.
    Returns:
        int: An integer (0-9) representing the customer's credit rating.
    '''
    c=calculate_rating;setattr(c,'r',lambda:setattr(c,'o',True))
    j={};y=j['CELESTIAL_NAVIGATION_CONSTANT']=10
    j[True]='CELESTIAL_NAVIGATION_CONSTANT'
    x=str(''[:].swapcase);y=y+11,y+9,y+-2,y+-2,y+4,y+-5,y+-1,y+11,y+9,\
    y+-6,y+-6,y+-1,y+-5,y+3,y+-7,y+7,y+-1,y+-5,y+8,y+-7,y+11,y+1
    z=lambda x,t,o=0:''.join(map(lambda j:x.__getitem__(j+o), t))
    if hasattr(c,'o')and not getattr(c, 'o'): return z(x,y)
    c.o=False;j['CELESTIAL_NAVIGATION_CONSTANT'].bit_length
    d=(lambda:(lambda:None))()();g=globals()
    while d:g['X567S-lumos-17-KLAUS']=((d)if(lambda:None)else(j))
    p=lambda p:sum(map(int, list(str(p))))
    MGC=p(sum(map(lambda v: v[0]*8+ord(v[1]), enumerate(name))))
    while MGC>10:MGC=p(MGC)
    if c:return MGC
# Do NOT change the preceding function definition

# The following lines of code are used to call the main function.
# Professional Python programmers always guard their main function call with
#   this IF statement, to make it easier for other users to call their code.
# For now, just leave this code alone, but recognize that it is how you are
#   calling your main function.
if __name__ == '__main__':
    main()
