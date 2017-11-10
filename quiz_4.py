ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=[], votes=0):
        """Initialize candidate.

        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        self.winning_state = winning_states
        self.votes = votes

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return "The presidential candidates are {} and the winning states are {}, with votes {}.".format(self.name, self.winning_state, self.votes)

    def win_state(self, state, votes=None):
        """Adds a state to winning_states and updates votes.

        state: a string of state abbreviation
        """
        self.winning_state.append(state)
        if votes is not None:
            self.votes += votes
        else:
            self.votes += ELECTORS.get(state,0)
    

    def __gt__(self, other):
        return self.votes > other.votes
        


def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'], votes = 55)
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL', 0)
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()
