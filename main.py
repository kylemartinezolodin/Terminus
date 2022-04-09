from server.main import Server 
from pathlib import Path
import secrets
import json

class Terminal:
    """A class emulating the machine that accepts the card, calculates fare, prints reciepts/tickets and communicates to the operation's server"""

    main_server: Server
    card: str
    paper: int # EMAULATES PAPER FOR PRINTING, THIS PROPERTY ACCOUNTS N TRANSACTIONS CAN BE COMPLETED UNTIL PAPER RUNS OUT
    selected_destination: str
    destination_fare: int # MAXIMUM VALUE OF 150
    
    def __init__(self, server: Server = Server(), paper: int = 10) -> None:
        self.main_server = server
        self.paper = paper
        self.selected_destination = ""
        self.card = ""
        self.destination_fare = 0

    def select_destination(self, destination: str) -> bool:
        if destination in self.main_server.destinations:
            self.selected_destination = destination
            return True
        return False

    def check_train_availability(self) -> bool:
        # ASSUMES DESTINAITON IS SELECTED
        if self.selected_destination:
            if self.main_server.train_is_available(self.selected_destination):
                self.destination_fare = secrets.randbelow(150) # 150 IS THE MAX POSSIBLE FARE
                return True 
        return False

    def reset(self) -> bool:
        self.selected_destination = ""
        self.destination_fare = 0
        self.card = ""
        return True

    def insert_card(self, fname: str) -> bool:
        if fname.count("."): # IF fname HAS PERIOD OR EXTENTION (".txt")
            fname = fname[:fname.find(".")] # REMOVE EXTENTION

        if Path(fname+".nfo").is_file():
            self.card = fname
            return True

        return False

    def check_card_validity(self) -> bool:
        # ASSUMES CARD IS INSERTED
        card = open(self.card +".nfo", "r")
        # SOME DECRYPTION ...

        return self.main_server.card_is_valid(card.read())

    def check_card_balance(self) -> bool:
        # ASSUMES CARD IS INSERTED
        # ASSUMES CARD IS VALID
        # ASSUMES FARE ALREADY CALCULATED
        card_ic = open(self.card +".nfo", "r")
        # SOME DECRYPTION ...

        card = json.loads(card_ic.read())
        return card["Balance"] >= self.destination_fare

    def debit_card(self) -> bool:
        # ASSUMES CARD IS INSERTED
        # ASSUMES CARD IS VALID
        # ASSUMES FARE ALREADY CALCULATED
        # ASSUMES CARD HAS ENOUGH BALANCE
        card_ic = open(self.card +".nfo", "r+")
        # SOME DECRYPTION ...

        card = json.loads(card_ic.read())
        card["Balance"] -= self.destination_fare

        # SOME ENCRYPTION ...
        card_ic.truncate(0) # CLEAR BINARY DATA
        card_ic.seek(0, 0) # RESET CURSOR
        card_ic.write(json.dumps(card))
        card_ic.close()
        return True
    
    def refund_card(self) -> bool:
        # ASSUMES CARD IS INSERTED
        # ASSUMES CARD IS VALID
        # ASSUMES FARE ALREADY CALCULATED
        return self.main_server.load_card(self.card, self.destination_fare) # NOTE: the machine has the authority to deduct balances, but needs server's authority to load a balance 
        

    def return_card(self) -> bool:
        self.card = "" # EMULATED EJECTION
        return True if self.card == "" else False

    def print_reciept_ticket(self) -> bool:
        if self.paper > 0:
            self.paper -= 1 # EMULATED PRINT
            return True
        return False

    def clear_paper(self):
        self.paper = 0 # EMULATED EMPTY SPOOL

