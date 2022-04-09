from typing import Dict, List
import json

#DestDictFormat = dict[str, int] # THIS IS A TYPE HINT, READ MORE:https://docs.python.org/3/library/typing.html
class Server:
    """A class emlating the server which terminals communicate for querry destinations, train and other company authorized modifications to smart cards"""

    destinations: Dict[str, int] = {} # EMULATES DATABASE OF DESTINATIONS AND AVAILABLE TRAINS, INSERT PREDEFINED DESTINAITONS AND NUMBER OF AVAILABLE TRAINS

    def __init__(self, destinations:List[str] = None) -> None:
        """Emulates Initializing a Server 
            Arguments:
            desitinaitons(optional): Adds more destinations aside from the predefined destiantions; the argument only accepts List of strings
        """
        if type(destinations) is list:
            for dest in destinations:
                self.destinations.update({dest: 1})
        elif destinations == None:
            pass
        else:
            raise TypeError('Argument "destinaitons" is type: ' +type(destinations) +'. Must be a list of strings, try enclosing with "[]"')

    def create_valid_card(self, fname: str):
        """Generates .nfo file which emulates a card containing actual data

        Args:
            fname (str): Name of the file.
        """
        if fname.count("."): # IF fname HAS PERIOD OR EXTENTION (".txt")
            fname = fname[:fname.find(".")] # REMOVE EXTENTION
        f = open(fname +".nfo", "w")
        
        data = {
            "Valid": True,
            "Balance": 0
        }

        f.write(json.dumps(data))

        # SOME ENCRYPTION TO FILE...

        f.close

    def card_is_valid(self, nfo_binary: str) -> bool:
        """Checks for validity of a card.

        Args:
            nfo_binary (str): This refers to the data inside the card (.nfo). Note: pass the data inside .nfo not the filename. 

        Returns:
            bool: Returns True if valid, otherwise False
        """
        
        # SOME DECRYPTION TO "nfo_binary"...
        card = None
        try:
            card = json.loads(nfo_binary)
        except: # RETURN FALSE IF CANNOT BE LOADED
            return False
        return True if card["Valid"] else False

    def load_card(self, fname: str, load: int) -> bool:
        """Give Credits to a Card. Requires .nfo file

        Args:
            fname (str): Name of the file.
            load (int): Value of credit

        Returns:
            bool: Returns True if success, otherwise False
        """
        if fname.count("."): # IF fname HAS PERIOD OR EXTENTION (".txt")
            fname = fname[:fname.find(".")] # REMOVE EXTENTION

        f = open(fname +".nfo", "r+")
        nfo_binary = f.read()
        if self.card_is_valid(nfo_binary):

            # SOME DECRYPTION TO "nfo_binary"...

            card = json.loads(nfo_binary)

            if load > 0: # WILL NOT ACCEPT NEGATIVE OR ZERO VALUES 
                card["Balance"] += load    
            else:
                return False
        else:
            return False
        
        
        # SOME ENCRYPTION TO "card"...

        f.seek(0, 0) # RESET CURSOR
        f.write(json.dumps(card))
        f.close
        return True

    def invalidate_card(self, fname: str):
        if fname.count("."): # IF fname HAS PERIOD OR EXTENTION (".txt")
            fname = fname[:fname.find(".")] # REMOVE EXTENTION
        f = open(fname +".nfo", "r+")

        nfo_binary = f.read()

        # SOME DECRYPTION TO "nfo_binary"...
        
        card = json.loads(nfo_binary)
        card["Valid"] = False
        nfo_binary = json.dumps(card)

        # SOME ENCRYPTION TO "nfo_binary"...

        f.seek(0, 0) # RESET CURSOR
        f.write(nfo_binary)
        f.close

    def add_destination(self, destination: str):
        self.destinations.update({destination: 1})

    def add_train(self, destination: str):
        self.destinations[destination] += 1

    def remove_train(self, destination: str):
        self.destinations[destination] -= 1

    def train_is_available(self, destination: str) -> bool:
        return True if self.destinations[destination] else False
