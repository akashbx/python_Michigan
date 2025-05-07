
# FreeCell Game

from cards import Deck, Card

NUM_FREECELLS = 4
NUM_FOUNDATIONS = 4
NUM_TABLEAU = 8

class FreeCellGame:
    def __init__(self):
        self.tableau = [[] for _ in range(NUM_TABLEAU)]
        self.freecells = [None] * NUM_FREECELLS
        self.foundations = [[] for _ in range(NUM_FOUNDATIONS)]
        self.deck = Deck()
        self.deck.shuffle()
        self.deal_cards()

    def deal_cards(self):
        for i in range(52):
            self.tableau[i % NUM_TABLEAU].append(self.deck.deal())

    def display(self):
      print("\nFree Cells:")
      for i, cell in enumerate(self.freecells):
        print(f"{i}: {str(cell) if cell else 'Empty'}", end="  ")
        print("\n\nFoundations:")
      for i, pile in enumerate(self.foundations):
          top = pile[-1] if pile else "Empty"
          print(f"{i}: {top}", end="  ")
          print("\n\nTableau:")
          max_height = max(len(col) for col in self.tableau)
      for i in range(max_height):
        for col in self.tableau:
            card_str = str(col[i]) if i < len(col) else ''
            print(f"{card_str:8}", end=" ")
        print()
    print()


    def move_t2f(self, t, f):
        if not self.tableau[t]:
            print("Invalid move: Tableau column is empty.")
            return False
        card = self.tableau[t][-1]
        if self.valid_foundation_move(card, f):
            self.foundations[f].append(self.tableau[t].pop())
            return True
        print("Invalid move: Cannot move to foundation.")
        return False

    def move_t2c(self, t, c):
        if not self.tableau[t]:
            print("Invalid move: Tableau column is empty.")
            return False
        if self.freecells[c] is None:
            self.freecells[c] = self.tableau[t].pop()
            return True
        print("Invalid move: Free cell is occupied.")
        return False

    def move_t2t(self, t1, t2):
        if not self.tableau[t1]:
            print("Invalid move: Source tableau is empty.")
            return False
        card = self.tableau[t1][-1]
        if self.valid_tableau_move(card, t2):
            self.tableau[t2].append(self.tableau[t1].pop())
            return True
        print("Invalid move: Cannot move to target tableau.")
        return False

    def move_c2t(self, c, t):
        card = self.freecells[c]
        if card is None:
            print("Invalid move: Free cell is empty.")
            return False
        if self.valid_tableau_move(card, t):
            self.tableau[t].append(card)
            self.freecells[c] = None
            return True
        print("Invalid move: Cannot move to tableau.")
        return False

    def move_c2f(self, c, f):
        card = self.freecells[c]
        if card is None:
            print("Invalid move: Free cell is empty.")
            return False
        if self.valid_foundation_move(card, f):
            self.foundations[f].append(card)
            self.freecells[c] = None
            return True
        print("Invalid move: Cannot move to foundation.")
        return False

    def valid_foundation_move(self, card, f):
        pile = self.foundations[f]
        if not pile:
            return card.rank() == 1
        top = pile[-1]
        return card.suit() == top.suit() and card.rank() == top.rank() + 1

    def valid_tableau_move(self, card, t):
        pile = self.tableau[t]
        if not pile:
            return True
        top = pile[-1]
        return card.opposite_color(top) and card.rank() == top.rank() - 1

    def check_win(self):
        return all(len(foundation) == 13 for foundation in self.foundations)

def print_help():
    print("""
Commands:
  t2f T F   → move from tableau T to foundation F
  t2c T C   → move from tableau T to free cell C
  t2t T1 T2 → move from tableau T1 to tableau T2
  c2t C T   → move from cell C to tableau T
  c2f C F   → move from cell C to foundation F
  h         → help
  q         → quit
""")

def main():
    game = FreeCellGame()
    print("Welcome to FreeCell!\n")
    game.display()
    print_help()

    while True:
        command = input("\nEnter command: ").lower().split()
        if not command:
            continue
        if command[0] == 'q':
            print("Thanks for playing FreeCell!")
            break
        elif command[0] == 'h':
            print_help()
        elif command[0] == 't2f' and len(command) == 3:
            game.move_t2f(int(command[1]), int(command[2]))
        elif command[0] == 't2c' and len(command) == 3:
            game.move_t2c(int(command[1]), int(command[2]))
        elif command[0] == 't2t' and len(command) == 3:
            game.move_t2t(int(command[1]), int(command[2]))
        elif command[0] == 'c2t' and len(command) == 3:
            game.move_c2t(int(command[1]), int(command[2]))
        elif command[0] == 'c2f' and len(command) == 3:
            game.move_c2f(int(command[1]), int(command[2]))
        else:
            print("Invalid command. Type 'h' for help.")

        game.display()
        if game.check_win():
            print("Congratulations! You won!")
            break

if __name__ == "__main__":
    main()
