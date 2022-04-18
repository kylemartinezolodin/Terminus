# UNIT TEST SCENARIO 2 HERE 
import sys
sys.path.append('../')

from Server.main import Server
from main import Terminal
import unittest

class TestTerminal(unittest.TestCase):
    def test_scenario1(self):
        servr = Server(["Cebu", "Manila", "Labangon"])
        servr.create_valid_card("test")
        servr.load_card("test", 200)
        termnal = Terminal(servr, 5)

        # c1. Is the destination chosen?
        c1 = termnal.select_destination("Manila")
        self.assertEqual(c1, True)
        # c2. There are available trains.
        c2 = termnal.check_train_availability()
        self.assertEqual(c2, True)
        # c3. Is the card inserted?
        c3 = termnal.insert_card("test")
        self.assertEqual(c3, True)
        # c4. Is the card valid?
        c4 = termnal.check_card_validity()
        self.assertEqual(c4, True)
        # c5. The card has enough balance.
        c5 = termnal.check_card_balance()
        self.assertEqual(c5, True)

        if c1 and c2 and c3 and c4 and c5:
            # a1. The card is debited.
            a1 = termnal.debit_card()
            self.assertEqual(a1, True)
            # a2. Is the receipt/ticket printed?
            a2 = termnal.print_reciept_ticket()
            self.assertEqual(a2, True)
            # a3. The card is returned.
            a3 = termnal.return_card()
            self.assertEqual(a3, True)
            # a4. The terminal is reseted.
            a4 = termnal.reset()
            self.assertEqual(a4, True)


    def test_scenario2(self):
        servr = Server(["Cebu", "Manila", "Labangon"])
        servr.create_valid_card("test")
        termnal = Terminal(servr, 5)

        # c1. Is the destination chosen?
        c1 = termnal.select_destination("Manila")
        self.assertEqual(c1, True)
        # c2. There are available trains.
        c2 = termnal.check_train_availability()
        self.assertEqual(c2, True)
        # c3. Is the card inserted?
        c3 = termnal.insert_card("test")
        self.assertEqual(c3, True)
        # c4. Is the card valid?
        c4 = termnal.check_card_validity()
        self.assertEqual(c4, True)
        # c5. The card has enough balance.
        c5 = termnal.check_card_balance()
        self.assertEqual(c5, False)

        if c1 and c2 and c3 and c4 and not c5:
            # a1. The card is debited.
            # a2. Is the receipt/ticket printed?
            a2 = termnal.print_reciept_ticket()
            self.assertEqual(a2, False)
            # a3. The card is returned.
            a3 = termnal.return_card()
            self.assertEqual(a3, True)
            # a4. The terminal is reseted.
            a4 = termnal.reset()
            self.assertEqual(a4, True)


    def test_scenario3(self):
        servr = Server(["Cebu", "Manila", "Labangon"])
        servr.create_valid_card("test")
        servr.invalidate_card("test")
        termnal = Terminal(servr, 5)

        # c1. Is the destination chosen?
        c1 = termnal.select_destination("Manila")
        self.assertEqual(c1, True)
        # c2. There are available trains.
        c2 = termnal.check_train_availability()
        self.assertEqual(c2, True)
        # c3. Is the card inserted?
        c3 = termnal.insert_card("test")
        self.assertEqual(c3, True)
        # c4. Is the card valid?
        c4 = termnal.check_card_validity()
        self.assertEqual(c4, False)
        # c5. The card has enough balance.

        if c1 and c2 and c3 and not c4:
            # a1. The card is debited.
            # a2. Is the receipt/ticket printed?
            a2 = termnal.print_reciept_ticket()
            self.assertEqual(a2, False)
            # a3. The card is returned.
            a3 = termnal.return_card()
            self.assertEqual(a3, True)
            # a4. The terminal is reseted.
            a4 = termnal.reset()
            self.assertEqual(a4, True)


    def test_scenario4(self):
        servr = Server(["Cebu", "Manila", "Labangon"])
        servr.create_valid_card("test")
        servr.remove_trains("Cebu")
        servr.remove_trains("Manila")
        servr.remove_trains("Labangon")
        termnal = Terminal(servr, 5)

        # c1. Is the destination chosen?
        c1 = termnal.select_destination("Manila")
        self.assertEqual(c1, True)
        # c2. There are available trains.
        c2 = termnal.check_train_availability()
        self.assertEqual(c2, False)
        # c3. Is the card inserted?
        c3 = termnal.insert_card("test")
        self.assertEqual(c3, True)
        # c4. Is the card valid?
        c4 = termnal.check_card_validity()
        self.assertEqual(c4, True)
        # c5. The card has enough balance.

        if c1 and c2 and c3 and not c4:
            # a1. The card is debited.
            # a2. Is the receipt/ticket printed?
            a2 = termnal.print_reciept_ticket()
            self.assertEqual(a2, False)
            # a3. The card is returned.
            a3 = termnal.return_card()
            self.assertEqual(a3, True)
            # a4. The terminal is reseted.
            a4 = termnal.reset()
            self.assertEqual(a4, True)


    def test_scenario5(self):
        servr = Server(["Cebu", "Manila", "Labangon"])
        servr.create_valid_card("test")
        servr.load_card("test", 200)
        termnal = Terminal(servr, 0)

        # c1. Is the destination chosen?
        c1 = termnal.select_destination("Manila")
        self.assertEqual(c1, True)
        # c2. There are available trains.
        c2 = termnal.check_train_availability()
        self.assertEqual(c2, True)
        # c3. Is the card inserted?
        c3 = termnal.insert_card("test")
        self.assertEqual(c3, True)
        # c4. Is the card valid?
        c4 = termnal.check_card_validity()
        self.assertEqual(c4, True)
        # c5. The card has enough balance.

        if c1 and c2 and c3 and not c4:
            # a1. The card is debited.
            a1 = termnal.debit_card()
            self.assertEqual(a1, True)
            # a2. Is the receipt/ticket printed?
            a2 = termnal.print_reciept_ticket()
            self.assertEqual(a2, False)
            # a3. The card is returned.
            a3 = termnal.return_card()
            self.assertEqual(a3, True)
            # a4. The terminal is reseted.
            a4 = termnal.reset()
            self.assertEqual(a4, True)


if __name__ == '__main__':
    unittest.main()