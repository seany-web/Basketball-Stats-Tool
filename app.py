import constants

DIRTY_PLAYER_DATA = constants.PLAYERS
cleaned_player_data = []

def clean_data():
    for player in DIRTY_PLAYER_DATA:
        cleaned_player = {
            'name': player['name'],
            'guardians': player['guardians']
        }
        if player['experience'] == 'YES':
            cleaned_player['experience'] = True
        else:
            cleaned_player['experience'] = False
        cleaned_player['height'] = int(player['height'].split(' ')[0])
        cleaned_player_data.append(cleaned_player)

def balance_teams():
    pass

# if __name__ == "__main__":
#     clean_data()

#     for player in cleaned_player_data:
#         print(f"Player Name: {player['name']}\nGuardian(s): {player['guardians']}\nExperienced? {player['experience']}\nHeight: {player['height']} inches")