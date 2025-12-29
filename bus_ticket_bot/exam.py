from abc import ABC, abstractmethod
from random import choice


class RuleSet:
    def __init__(self, rules):
        self._rules = rules

    def check_who_won(self, first, second):
        if first == second:
            return "draw"

        if self._rules[first] == second:
            return "first"

        return "second"


class Player(ABC):
    @abstractmethod
    def choose(self):
        raise NotImplementedError


class HumanChoice(Player):
    def choose(self):
        while True:
            user_choice = input("Pick a choice [r, p, s]: ")
            if user_choice in ("r", "p", "s"):
                return user_choice
            print("Invalid input, pick a valid choice.")

class ComputerChoice(Player):
    def choose(self):
        return choice(("r", "p", "s"))


class Game:
    def __init__(self, player_one, player_two, rules, hands=3):
        self._player_one = player_one
        self._player_two = player_two
        self._rules = rules
        self._hands = hands
        self.__scores = {
            "first": 0,
            "second": 0
        }

    def _add_score(self, winner):
        if winner == "draw":
            return
        self.__scores[winner] += 1

    def _any_player_won(self):
        for key, value in self.__scores.items():
            if value >= self._hands:
                return key
        return None

    @staticmethod
    def _winner_label(winner):
        return "User" if winner == "first" else "Computer" if winner == "second" else "Draw no"

    def _play_round(self):
        user_choice = self._player_one.choose()
        computer_choice = self._player_two.choose()
        winner = self._any_player_won()
        if winner:
            return self._winner_label(winner)

        result = self._rules.check_who_won(user_choice, computer_choice)

        print(f"Player One: {user_choice} | Player Two: {computer_choice}")

        self._add_score(result)
        print(f"{self._winner_label(result)} player won this round.")

    def play(self):
        while True:
            winner = self._play_round()
            if winner:
                print(f"Winner is {winner}")
                break


def main():
    rules = RuleSet(
        rules={
            "p": "r",
            "r": "s",
            "s": "p"
        }
    )
    game = Game(
        HumanChoice(),
        ComputerChoice(),
        rules,
        hands=3
    )

    game.play()



if __name__ == "__main__":
    main()
