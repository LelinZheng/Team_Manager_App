from player import Player


class Team:
    """A class representing a dodgeball team"""

    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        """Set up the team name"""
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        """
        Create a new player object, then add that
        player object to the team's players list
        """
        player = Player(player_name, player_number, player_position)
        self.players.append(player)

    def cut_player(self, player_name):
        """
        Remove a new player object
        from the team's players list
        """
        for player in self.players:
            if player_name == player.get_name():
                self.players.remove(player)

    def is_position_filled(self, position):
        """
        Checks whether there is currently at least
        one player on the team occupying the
        requested position
        """
        for player in self.players:
            if position == player.get_position():
                return True
        return False

    def show_player_roster(self):
        """Display the full team roster"""

        print(f"The lineup for {self.name} is:")

        if not self.players:
            print("The team currently has no players")
            return

        for player in self.players:
            line = player.get_number() + \
                "\t" + player.get_name() + \
                "\t" + player.get_position()

            print(line)
