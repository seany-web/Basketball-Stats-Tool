import constants

TEAMS = constants.TEAMS
PLAYERS = constants.PLAYERS

cleaned_player_data = []

team_1 = {
    'name': 'Panthers',
    'total_squad_size': 0,
    'total_experienced_players': 0,
    'total_inexperienced_players': 0,
    'total_height': 0,
    'players': [],
    'guardians': []
}

team_2 = {
    'name': 'Bandits',
    'total_squad_size': 0,
    'total_experienced_players': 0,
    'total_inexperienced_players': 0,
    'total_height': 0,
    'players': [],
    'guardians': []
}

team_3 = {
    'name': 'Warriors',
    'total_squad_size': 0,
    'total_experienced_players': 0,
    'total_inexperienced_players': 0,
    'total_height': 0,
    'players': [],
    'guardians': []
}


def clean_data():
    for player in PLAYERS:
        cleaned_player = {
            'name': player['name'],
            'guardians': player['guardians'].split(' and ')
        }
        if player['experience'] == 'YES':
            cleaned_player['experience'] = True
        else:
            cleaned_player['experience'] = False
        cleaned_player['height'] = int(player['height'].split(' ')[0])
        cleaned_player_data.append(cleaned_player)


def balance_teams():
    max_squad_size = len(PLAYERS) / len(TEAMS)
    experienced_players_per_team = get_num_of_experienced_players()
    inexperienced_players_per_team = get_num_of_inexperienced_players()
    
    for player in cleaned_player_data:
        if team_1['total_squad_size'] < max_squad_size:
            if player['experience'] is True and team_1['total_experienced_players'] < experienced_players_per_team:
                add_player_to_team(player, team_1)
                continue
            elif player['experience'] is False and team_1['total_inexperienced_players'] < inexperienced_players_per_team:
                add_player_to_team(player, team_1)
                continue
        if team_2['total_squad_size'] < max_squad_size:
            if player['experience'] is True and team_2['total_experienced_players'] < experienced_players_per_team:
                add_player_to_team(player, team_2)
                continue
            elif player['experience'] is False and team_2['total_inexperienced_players'] < inexperienced_players_per_team:
                add_player_to_team(player, team_2)
                continue
        if team_3['total_squad_size'] < max_squad_size:
            if player['experience'] is True and team_3['total_experienced_players'] < experienced_players_per_team:
                add_player_to_team(player, team_3)
                continue
            elif player['experience'] is False and team_3['total_inexperienced_players'] < inexperienced_players_per_team:
                add_player_to_team(player, team_3)
                continue

# This function takes a player and a team and adds the given player to the team while updated team stats
def add_player_to_team(player, team):
    team['total_squad_size'] += 1
    team['players'].append(player['name'])
    team['total_height'] += player['height']
    if player['experience'] is True:
        team['total_experienced_players'] += 1
    else:
        team['total_inexperienced_players'] += 1
    for guardian in player['guardians']:
        team['guardians'].append(guardian)


# This function gets the max number of experienced players allowed on a team
def get_num_of_experienced_players():
    sum = 0
    for player in cleaned_player_data:
        if player['experience'] is True:
            sum += 1
    return sum / len(TEAMS)


# This function gets the max number of inexperienced players allowed on a team
def get_num_of_inexperienced_players():
    sum = 0
    for player in cleaned_player_data:
        if player['experience'] is False:
            sum += 1
    return sum / len(TEAMS)


def display_main_menu():
    print('\n----MENU----\n')
    print('Here are you choices:')
    print(' 1) Display Team Stats')
    print(' 2) Quit')


def display_submenu():
    print('\nPlease select a team from the menu below\n')
    print(' 1) Panthers')
    print(' 2) Bandits')
    print(' 3) Warriors')


# This function takes in a team and displays the teams stats on screen
def display_team_stats(team):
    players_string = ', '.join(team['players'])
    guardians_string = ', '.join(team['guardians'])
    print('\nTeam: {0} Stats'.format(team['name']))
    print('-' * 20)
    print('Total Players: {0}'.format(team['total_squad_size']))
    print('Total experienced: {0}'.format(team['total_experienced_players']))
    print('Total inexperienced: {0}'.format(team['total_inexperienced_players']))
    print('Average height: {0}\n'.format(team['total_height'] / team['total_squad_size']))
    print('Players on Team:\n  {0}\n'.format(players_string))
    print('Guardians:\n  {0}\n'.format(guardians_string))
    input('Press any key to continue...')


if __name__ == "__main__":
    clean_data()
    balance_teams()

    print('BASKETBALL TEAM STATS TOOL\n')

    # Main Menu loop starts here
    while(True):
        display_main_menu()
        mainmenu_selection = input('\nEnter an option > ')
        if mainmenu_selection == '1':
            # Submenu loop starts here
            while (True):
                display_submenu()
                submenu_selection = input('\nEnter an option > ')
                if submenu_selection == '1':
                    display_team_stats(team_1)
                    break
                elif submenu_selection == '2':
                    display_team_stats(team_2)
                    break
                elif submenu_selection == '3':
                    display_team_stats(team_3)
                    break
                else:
                    print('\nThat is not a valid selection. Please try again\n')
            # end of submenu loop
        elif mainmenu_selection == '2':
            print('\nExiting application. Goodbye!\n')
            break
        else:
            print('\nThat is not a valid selection. Please try again\n')
        # end of main menu loop
