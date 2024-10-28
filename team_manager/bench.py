class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        """Initialize the bench"""
        self.bench_players = []

    def send_to_bench(self, player):
        """Put the player onto the bench"""
        self.bench_players.insert(0, player)

    def get_from_bench(self):
        """
        Return the name of the player who has
        been on the bench longest
        """
        return self.bench_players.pop().get_name()

    def show_bench_roster(self):
        """Display the bench roster"""
        print("The bench currently includes:")

        if not self.bench_players:
            print("The bench is empty.")
            return
        for player in self.bench_players:
            print(player.get_name())

    def get_player_list(self):
        """A getter for the bench player list"""
        return self.bench_players

    def is_benched(self, player):
        """checks if a player is benched"""
        if player in self.bench_players:
            return True

        return False
