def coffee(flavour):
    
    if flavour not in ['masala', 'ginger']:
        raise ValueError (f'This flavour {flavour }is not available')
    
coffee("") # ValueError: This flavour is not available

class FlavourOutageErr(Exception):
    pass

def mocha(flavour):
    if flavour not in ['masala', 'ginger']:
        raise FlavourOutageErr("flavour is not available")
