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
            if player['experience'] == True and team_1['total_experienced_players'] < experienced_players_per_team:            
                add_player_to_team(player, team_1)
                continue
            elif player['experience'] == False and team_1['total_inexperienced_players'] < inexperienced_players_per_team:
                add_player_to_team(player, team_1)
                continue
        if team_2['total_squad_size'] < max_squad_size:
            if player['experience'] == True and team_2['total_experienced_players'] < experienced_players_per_team:            
                add_player_to_team(player, team_2)
                continue
            elif player['experience'] == False and team_2['total_inexperienced_players'] < inexperienced_players_per_team:
                add_player_to_team(player, team_2)
                continue
        if team_3['total_squad_size'] < max_squad_size:
            if player['experience'] == True and team_3['total_experienced_players'] < experienced_players_per_team:            
                add_player_to_team(player, team_3)
                continue
            elif player['experience'] == False and team_3['total_inexperienced_players'] < inexperienced_players_per_team:
                add_player_to_team(player, team_3)
                continue



def add_player_to_team(player, team):
    team['total_squad_size'] += 1
    team['players'].append(player['name'])
    team['total_height'] += player['height']
    if player['experience'] == True:
        team['total_experienced_players'] += 1
    else:
        team['total_inexperienced_players'] += 1
    for guardian in player['guardians']:
        team['guardians'].append(guardian)


def get_num_of_experienced_players():
    sum = 0
    for player in cleaned_player_data:
        if player['experience'] == True:
            sum += 1
    return sum / len(TEAMS)


def get_num_of_inexperienced_players():
    sum = 0
    for player in cleaned_player_data:
        if player['experience'] == False:
            sum += 1
    return sum / len(TEAMS)

def display_main_menu():
    print('---- MENU----')
    print('Here are you choices:\n')
    print('1) Display Team Stats')
    print('2) Quit')


def display_submenu():
    print('1) Panthers')
    print('2) Bandits')
    print('3) Warriors')


def display_team_stats(team):
    #show team name
    print('Team: {0} Stats'.format(team['name']))
    print('-' * 20)
    #show total players
    print('Total Players: {0}'.format(team['total_squad_size']))
    #show total experienced players
    print('Total experienced: {0}'.format(team['total_experienced_players']))
    #show total inexperienced players
    print('Total inexperienced: {0}'.format(team['total_inexperienced_players']))
    #calcuate and show average height
    print('Average height: {0}'.format(team['total_height'] / team['total_squad_size']))
    #show players on team
    print(', '.join(team['players']))
    #show guardians of players on team
    print(', '.join(team['guardians']))


    input('Press any key to continue...')


if __name__ == "__main__":
    clean_data()
    balance_teams()

    print('BASKETBALL TEAM STATS TOOL\n')
    
    #Main Menu loop starts here
    while(True):
        display_main_menu()
        #prompt user for selection
        mainmenu_selection = input('Enter an option > ')
        #if submenu selected
        if mainmenu_selection == '1':
            #show submenu
            while (True):   
                display_submenu()
                #prompt user for selection
                submenu_selection = input('Enter an option > ')
                #if valid selection
                    #display team info
                    #exit sub menu
                if submenu_selection == '1':
                    display_team_stats(team_1)
                    break
                elif submenu_selection == '2':
                    display_team_stats(team_2)
                    break
                elif submenu_selection == '3':
                    display_team_stats(team_3)
                    break    
                #else
                else:
                    #prompt user for valid selection
                    print('That is not a valid selection. Please try again')
        #if quit selected
        elif mainmenu_selection == '2':
            #exit gracefully
            print('Exiting application. Goodbye!')
            break
        #else
        else:
            #prompt user for valid selection
            print('That is not a valid selection. Please try again')
