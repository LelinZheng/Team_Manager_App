from team import Team
from bench import Bench
import re


# This is a team management system
# Coaches can add/remove player, send/retrieve players to/from bench
def main():
    print("Welcome to the team manager.")
    the_team = Team()
    the_bench = Bench()

    while True:
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    """set team name"""
    name = input("What do you want to name the team?\n")
    if is_alphanumeric(name):
        team.set_team_name(name)
    else:
        print("Invalid team name input.")


def do_show_team_roster(team):
    """displays the roster"""
    team.show_player_roster()


def do_check_position_filled(team):
    """check is the position is filled"""
    position = input("What position are you checking for?\n")
    if is_alphanumeric(position):
        if team.is_position_filled(position):
            print(f"Yes, the {position} position is filled")
        else:
            print(f"No, the {position} position is not filled")
    else:
        print("Invalid position input.")


def do_add_player_to_team(team):
    """Add player to the team"""
    player_name = input("What's the player's name?\n")
    if not is_alphanumeric(player_name):
        print("Invalid name input.")
        return
    player_number = input("What's " + player_name + "'s number?\n")
    if not is_numeric(player_number):
        print("Invalid number input.")
        return
    player_position = input("What's " + player_name + "'s position?\n")
    if not is_alphanumeric(player_position):
        print("Invalid position input.")
        return
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_send_player_to_bench(team, bench):
    """Send the player to bench"""
    name = input("Who do you want to send to the bench?\n")
    if not is_alphanumeric(name):
        print("Invalid name input.")
        return
    for player in team.players:
        if name == player.get_name():
            bench.send_to_bench(player)
            return
    print(f"{name} isn't on the team")


def do_get_player_from_bench(bench):
    """get the best-rested player by name from the bench"""
    if not bench.get_player_list():
        print("The bench is empty.")
        return

    print(f"Got {bench.get_from_bench()} from the bench")


def do_cut_player(team, bench):
    """cut a player from the team"""
    name = input("What's player's name?\n")
    if not is_alphanumeric(name):
        print("Invalid name input.")
        return
    for player in team.players:
        if name == player.get_name() and not bench.is_benched(player):
            team.cut_player(name)
            return
        elif name == player.get_name() and bench.is_benched(player):
            print(f"{name} cannot be cut because they are benched.")
            return

    print(f"{name} isn't on the team")


def do_show_bench(bench):
    """show the list of players on the bench"""
    bench.show_bench_roster()


def do_not_understand():
    print("I didn't understand that command")


def is_alphanumeric(text):
    """
    To find out if a text is alphanumeric or space
    String -> bool
    """
    alpha_pattern = r"^[\w ]+$"
    return bool(re.match(alpha_pattern, text))


def is_numeric(text):
    """
    To find out if a text is numeric
    String -> bool
    """
    numeric_pattern = r"^[0-9]+$"
    return bool(re.match(numeric_pattern, text))


main()
