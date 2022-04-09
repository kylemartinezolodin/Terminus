# THIS SCRIPT IS A QUICK SAMPLE ON HOW TO RUN THE PROJECT, VERY RECOMENDED TO PASTE EACH LINE TO PYTHON'S INTERACTIVE SHELL
from server.main import Server
from main import Terminal

servr = Server(["Cebu", "Manila", "Labangon"]) # INITIALIZE SERVER
servr.destinations # SAMPLE QUERRY TO SERVER
termnal = Terminal(servr, 5) # SET THE SERVER TO BE USED ON THE MACHINE/TERMINAL
termnal.select_destination("Metro") # SAMPLE INTERACTION TO MACHINE/TERMINAL
termnal.select_destination("Cebu")
servr.remove_train("Manila")
servr.destinations 
termnal.select_destination("Manila")
termnal.check_train_availability()
termnal.select_destination("Cebu")
termnal.check_train_availability()
termnal.destination_fare # SAMPLE QUERRY TO MACHINE/TERMINAL
termnal.paper # SAMPLE QUERRY TO MACHINE/TERMINAL
termnal.insert_card("test")
termnal.check_card_validity()
termnal.check_card_balance()
termnal.debit_card()
termnal.refund_card()
termnal.return_card()
termnal.card
termnal.clear_paper()
termnal.paper
termnal.print_reciept_ticket()
termnal.paper



