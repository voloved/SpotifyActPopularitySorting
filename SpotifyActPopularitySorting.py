import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

PRINT_ARR = True
PRINT_RANKINGs = True
USE_TEST_ARR = False
PRINT_SEARCH_RESULTS = True

junfive= [{'name': 'ACRAZE', 'followers': 127080, 'popularity': 63}, {'name': 'ALLEYCVT', 'followers': 36697, 'popularity': 40}, {'name': 'ATLiens', 'followers': 98358, 'popularity': 44}, {'name': 'AYYBO', 'followers': 52417, 'popularity': 56}, {'name': 'Baggi', 'followers': 4164, 'popularity': 19}, {'name': 'Barclay Crenshaw', 'followers': 31293, 'popularity': 35}, {'name': 'Ben Bohmer', 'followers': 495128, 'popularity': 61}, {'name': 'Black Tiger Sex Machine', 'followers': 167136, 'popularity': 46}, {'name': 'Boogie T', 'followers': 90318, 'popularity': 43}, {'name': 'Brandi Cyrus', 'followers': 0, 'popularity': 0}, {'name': 'Calussa', 'followers': 8533, 'popularity': 45}, {'name': 'CannaBliss', 'followers': 32, 'popularity': 0}, {'name': 'Cannons', 'followers': 361315, 'popularity': 59}, {'name': 'Caspa', 'followers': 68236, 'popularity': 31}, {'name': 'Cassian', 'followers': 56577, 'popularity': 53}, {'name': 'Chaos in CBD', 'followers': 101794, 'popularity': 46}, {'name': 'Charlotte De Witte', 'followers': 938946, 'popularity': 58}, {'name': 'Chase & Status', 'followers': 915827, 'popularity': 67}, {'name': 'Coco & Breezy', 'followers': 19994, 'popularity': 44}, {'name': 'Cuco', 'followers': 2824249, 'popularity': 66}, {'name': 'Dimension', 'followers': 126559, 'popularity': 60}, {'name': 'Dirtwire', 'followers': 96676, 'popularity': 42}, {'name': 'Disco Biscuits', 'followers': 86130, 'popularity': 33}, {'name': "Dixon's Violin", 'followers': 4905, 'popularity': 10}, {'name': 'DJ Susan', 'followers': 32145, 'popularity': 31}, {'name': 'DJ Tennis', 'followers': 40928, 'popularity': 42}, {'name': 'DRAMA', 'followers': 143636, 'popularity': 56}, {'name': 'Dumpstaphunk', 'followers': 51904, 'popularity': 30}, {'name': 'Eggy', 'followers': 10497, 'popularity': 27}, {'name': 'Emo Nite', 'followers': 0, 'popularity': 0}, {'name': 'Equanimous', 'followers': 48805, 'popularity': 46}, {'name': 'EVERYTHING ALWAYS', 'followers': 346948, 'popularity': 69}, {'name': 'Excision', 'followers': 726722, 'popularity': 58}, {'name': 'G jones', 'followers': 91064, 'popularity': 36}, {'name': 'Gigantic NGHTMRE', 'followers': 360115, 'popularity': 52}, {'name': 'Green Velvet', 'followers': 230555, 'popularity': 52}, {'name': 'H&RRY', 'followers': 0, 'popularity': 0}, {'name': 'Hamdi', 'followers': 52588, 'popularity': 54}, {'name': 'hiatus kaiyote', 'followers': 626631, 'popularity': 55}, {'name': 'INZO', 'followers': 154187, 'popularity': 50}, {'name': "it's murph", 'followers': 46979, 'popularity': 58}, {'name': 'Ivy Lab', 'followers': 84738, 'popularity': 40}, {'name': 'Jjuujjuu', 'followers': 8996, 'popularity': 21}, {'name': 'John Summit', 'followers': 298695, 'popularity': 70}, {'name': 'Juelz', 'followers': 31106, 'popularity': 43}, {'name': 'Kenny Beats', 'followers': 204072, 'popularity': 60}, {'name': 'Kiltro', 'followers': 33850, 'popularity': 42}, {'name': 'Knock2', 'followers': 93144, 'popularity': 56}, {'name': 'Layton Giordani', 'followers': 75332, 'popularity': 56}, {'name': 'Le Youth', 'followers': 113193, 'popularity': 51}, {'name': 'Lettuce', 'followers': 212381, 'popularity': 41}, {'name': 'LEVEL UP', 'followers': 35951, 'popularity': 44}, {'name': 'levity', 'followers': 34601, 'popularity': 44}, {'name': 'Libianca', 'followers': 465078, 'popularity': 63}, {'name': 'Little stranger', 'followers': 56698, 'popularity': 49}, {'name': 'LP Giobbi', 'followers': 75190, 'popularity': 58}, {'name': 'LSZEE', 'followers': 168010, 'popularity': 49}, {'name': 'Lucii', 'followers': 67290, 'popularity': 42}, {'name': 'Ludacris', 'followers': 2948966, 'popularity': 75}, {'name': 'LYNY', 'followers': 14143, 'popularity': 41}, {'name': "Maddy O'Neal", 'followers': 18312, 'popularity': 34}, {'name': 'Major League Djz', 'followers': 844668, 'popularity': 49}, {'name': 'marsh', 'followers': 70150, 'popularity': 51}, {'name': 'Mascolo', 'followers': 2364, 'popularity': 37}, {'name': 'MASONIC', 'followers': 101, 'popularity': 0}, {'name': 'Matroda', 'followers': 126282, 'popularity': 57}, {'name': 'Mau P', 'followers': 101957, 'popularity': 62}, {'name': 'Michael Brun', 'followers': 49054, 'popularity': 49}, {'name': 'Mojave Grey', 'followers': 3728, 'popularity': 25}, {'name': 'NEIL FRANCES', 'followers': 208828, 'popularity': 64}, {'name': 'Nelly Furtado', 'followers': 3865810, 'popularity': 75}, {'name': 'Neoma', 'followers': 12643, 'popularity': 27}, {'name': 'odd Mob', 'followers': 72900, 'popularity': 57}, {'name': 'ODEN & Fatzo', 'followers': 36418, 'popularity': 55}, {'name': 'Only fire', 'followers': 40983, 'popularity': 38}, {'name': 'PAPERWATER', 'followers': 1435, 'popularity': 19}, {'name': 'Peach Tree Rascals', 'followers': 227953, 'popularity': 54}, {'name': 'Polyrhythmics', 'followers': 28850, 'popularity': 31}, {'name': 'Pretty Lights', 'followers': 558652, 'popularity': 48}, {'name': 'Proxima Parada', 'followers': 66225, 'popularity': 49}, {'name': 'Ranger Trucco', 'followers': 10525, 'popularity': 32}, {'name': 'Rawayana', 'followers': 659315, 'popularity': 64}, {'name': 'Rayben', 'followers': 41967, 'popularity': 40}, {'name': 'Redrum', 'followers': 2577, 'popularity': 11}, {'name': 'Sammy Virji', 'followers': 107275, 'popularity': 60}, {'name': 'Sara Landry', 'followers': 193991, 'popularity': 50}, {'name': 'Seven lions', 'followers': 487226, 'popularity': 57}, {'name': 'Shae District', 'followers': 2665, 'popularity': 15}, {'name': 'Slayyyter', 'followers': 397488, 'popularity': 53}, {'name': 'String Cheese Incident', 'followers': 226452, 'popularity': 41}, {'name': 'Subtronics', 'followers': 306550, 'popularity': 61}, {'name': 'Sultan + Shepard', 'followers': 125734, 'popularity': 55}, {'name': 'Super Future', 'followers': 13350, 'popularity': 28}, {'name': 'Swaylo', 'followers': 44, 'popularity': 0}, {'name': 'Thought process', 'followers': 8305, 'popularity': 28}, {'name': 'Tripp St.', 'followers': 14874, 'popularity': 29}, {'name': 'TSHA', 'followers': 71642, 'popularity': 48}, {'name': "Umphrey's McGee", 'followers': 201459, 'popularity': 40}, {'name': 'Unusual demont', 'followers': 43517, 'popularity': 41}, {'name': 'venbee', 'followers': 79060, 'popularity': 55}, {'name': 'Vini Vici', 'followers': 526759, 'popularity': 62}, {'name': 'VNSSA B2B Nala', 'followers': 0, 'popularity': 0}, {'name': 'Westend', 'followers': 46739, 'popularity': 56}, {'name': 'Whyte Fang', 'followers': 15116, 'popularity': 27}, {'name': 'Will Clarke', 'followers': 50197, 'popularity': 41}, {'name': 'Wooli', 'followers': 112535, 'popularity': 55}, {'name': 'Zen Selekta', 'followers': 3737, 'popularity': 15}]

dicto = {"BASS": ["ALLEYCVT",
                  "ATLiens",
                  "Barclay Crenshaw",
                  "Black Tiger Sex Machine",
                  "Caspa",
                  "Chase & Status",
                  "Dimension",
                  "Excision",
                  "Gigantic NGHTMRE",
                  "Hamdi",
                  "LEVEL UP",
                  "Lucii",
                  "LYNY",
                  "LSZEE",
                  "Sammy Virji",
                  "Subtronics",
                  "venbee",
                  "Whyte Fang",
                  "Wooli",
                  "Seven lions",
                  "G jones",
                  "Boogie T",
                  "CanaBliss",
                  "Ivy Lab",
                  "levity",
                  "Super Future",
                  "Zen Selekta",],
         "HOUSE": ["ACRAZE",
                   "AYYBO",
                   "Ben Bohmer",
                   "Calussa",
                   "Cassian",
                   "Charlotte De Witte",
                   "Coco & Breezy",
                   "DJ Tennis",
                   "DRAMA",
                   "EVERYTHING ALWAYS",
                   "Green Velvet",
                   "it's murph",
                   "John Summit",
                   "Knock2",
                   "Le Youth",
                   "LP Giobbi",
                   "Major League Djz",
                   "Matroda",
                   "Mau P",
                   "Michael Brun",
                   "ODEN & Fatzo",
                   "Ranger Trucco",
                   "Sultan + Shepard",
                   "TSHA",
                   "Vini Vici",
                   "VNSSA B2B Nala",
                   "Westend",
                   "Will Clarke",
                   "Sara Landry",
                   "Baggi",
                   "Brandi Cyrus",
                   "Chaos in CBD",
                   "DJ Susan",
                   "H&RRY",
                   "Layton Giordani",
                   "marsh",
                   "MASONIC",
                   "Mojave Grey",
                   "odd Mob",
                   "Only fire",
                   "Rayben",
                   "Shae District",
                   "Swaylo",],
         "INDIE": ["Cuco",
                   "NEIL FRANCES",
                   "Peach Tree Rascals",
                   "Emo Nite",
                   "Equanimous",
                   "Kiltro",],
         "POP": ["Cannons",
                 "Mascolo",
                 "Nelly Furtado",
                 "Slayyyter",
                 "Neoma",
                 "Unusual demont",],
         "JAM": ["Dirtwire",
                 "Dumpstaphunk",
                 "Eggy",
                 "Lettuce",
                 "Pretty Lights",
                 "Disco Biscuits",
                 "String Cheese Incident",
                 "Umphrey's McGee",
                 "Jjuujjuu",
                 "Proxima Parada",],
         "TRAP": ["INZO",
                  "Juelz",
                  "Maddy O'Neal",
                  "Redrum",
                  "Thought process",
                  "Tripp St.",],
         "RAP": ["Kenny Beats",
                 "Libianca",
                 "Ludacris",
                 "PAPERWATER",
                 "hiatus kaiyote",
                 "Little stranger",],
         "SOUL": ["Dixon's Violin",
                  "Rawayana",
                  "Polyrhythmics",]
         }


for_spotify ={ "Chaos in CBD" : "Chaos In The CBD",
              "Disco Biscuits": "The Disco Biscuits",
              "Proxima Parada" : "Próxima Parada",
              "String Cheese Incident" : "The String Cheese Incident",
              "Gigantic NGHTMRE" : ["Big Gigantic","NGHTMRE"],
              "EVERYTHING ALWAYS" : ["Dom Dolla","John Summit"],
              "LSZEE": ["CloZee","LSDREAM"],
              "VNSSA B2B Nala" : ["VNSSA","Nala"],
              "Michael Brun" : "Michaël Brun",
              "Ben Bohmer" : "Ben Böhmer"}


STAGES = [ "RANCH_ARENA", "SHERWOOD_COURT", "TRIPOLEE", "CAROUSEL_CLUB", "OBSERVATORY", "HONEYCOMB"]

'''
    {
        .artist = "EZBK  ",
        .stage = RANCH_ARENA,
        .start_time = {.unit.year = 4, .unit.month = 6, .unit.day = 20, .unit.hour = 15, .unit.minute = 0},
        .end_time = {.unit.year = 4, .unit.month = 6, .unit.day = 20, .unit.hour = 16, .unit.minute = 0},
        .genre = TRAP,
    },


'''

def get_client_credentials(file_path="creds.json"):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            client_id = data['client_id']
            client_secret = data['client_secret']
            return client_id, client_secret
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except KeyError as e:
        raise KeyError(f"The key {e} was not found in the JSON file.")

def get_artist(artist_name, client_id, client_secret):
    first_match = False
    if "'" in artist_name:
        first_match = True
        artist_name = artist_name.replace("'", "")
            
    # Authenticate with Spotify
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    
    # Search for the artist
    result = sp.search(q='artist:' + artist_name, type='artist')
    artist_results = result['artists']['items']
    if not artist_results:
        if PRINT_SEARCH_RESULTS:
            print(f"FAILED TO FIND: {artist_name}")
        return None
    artist_info = None
    names_in_search = []
    for option in artist_results:
        names_in_search.append(option['name'] )
    dupes = names_in_search.count(artist_name)
    if PRINT_SEARCH_RESULTS and dupes > 1:
        print(f"MULTIPLE FOUND FOR: {artist_name}: {names_in_search}")
    for option in artist_results:
        name = option['name'] 
        if first_match:
            if PRINT_SEARCH_RESULTS:
                print(f"Best for {artist_name} is {name} | Choices were {names_in_search}")
            artist_info = option
            break
        if name.upper() == artist_name.upper():
            if PRINT_SEARCH_RESULTS and dupes <= 1:
                print(f"Found {name} | Choices were {names_in_search}")
            artist_info = option
            break
    if artist_info is None:
        if PRINT_SEARCH_RESULTS:
            print(f"FAILED TO FIND: {artist_name}, BUT FOUND {names_in_search}")
        return None   
    return artist_info

def get_artist_followers_popularity(artist_name, client_id, client_secret):
    artist_info = get_artist(artist_name, client_id, client_secret)
    if artist_info is None:
        return 0,0
    followers = artist_info['followers']['total']
    popularity = artist_info['popularity']
    return followers, popularity


def rank_artists_by_popularity(artists):
    # Sort artists by popularity in descending order
    sorted_artists = sorted(artists, key=lambda x: x['followers'], reverse=True)
    
    # Create a dictionary to store the ranks
    artist_ranks = {}
    
    # Assign ranks starting from 1
    for rank, artist in enumerate(sorted_artists, start=1):
        artist_ranks[artist['name']] = rank
    
    return artist_ranks

def findGenre(act):
    for key in dicto:
        for i in dicto[key]:
            if i.upper() == act.upper():
                return key.upper()
    return -1

def get_ranking(artists, name, item):
    for artist in artists:
        if artist['name'].lower() == name.lower():
            return artist[item]
    return None

def set_pop_follow_manually(artists, name, pop, follower):
    for artist in artists:
        if artist['name'].lower() == name.lower():
            artist['popularity'] = pop
            artist['followers'] = follower
    return artists

def getFullArray(listActs):
    # Spits out the array of acts in alphabetically order.
    listActsPop = []
    client_id, client_secret = get_client_credentials()
    for act in listActs:
        act = for_spotify.get(act, act)
        if isinstance(act,list):
            continue # We'll get and average the duos later.
        followers, popularity = get_artist_followers_popularity(act, client_id, client_secret)
        listActsPop.append({'name':act, 'followers' : followers, "popularity" : popularity})
    # This logic is to average duos
    for duo in for_spotify:
        artists = for_spotify[duo]
        if not isinstance(artists,list):
            continue
        followers = 0
        popularity = 0
        for artist in artists:
            fol, pop = get_artist_followers_popularity(artist, client_id, client_secret)
            followers += fol
            popularity += pop
        followers = int(followers / len(artists))
        popularity = int(popularity / len(artists))
        listActsPop.append({'name':duo, 'followers' : followers, "popularity" : popularity})
        listActsPop = set_pop_follow_manually(listActsPop, "Cuco", 32, 1059)  # Wrong Cuco is the first option.
    return listActsPop

def print_md_lst(sorted_listing):
    longestAct = 25
    longestPop = 15
    longestFol = 10
    actTitle = "Act"
    popTitle = "Popularity"
    folTitle = "Followers"
    print(f"| {actTitle: ^{longestAct}} | {popTitle : ^{longestPop}} | {folTitle : ^{longestFol}} |")
    print(f"| {'-' * longestAct} | {'-' * longestPop} | {'-' * longestFol} |")
    for item in sorted_listing:
        act = item['name']
        popularity = item['popularity']
        followers = f"{item['followers']:,}"
        print(f"| {act : ^{longestAct}} | {popularity : ^{longestPop}} | {followers : ^{longestFol}} |")


def print_array_for_watch(listActs, sorted_listing):
    for i, act in enumerate(listActs):
        print("    {")
        print(f'        .artist = "{act.upper()[:6]: <6}",')
        print(f'        .stage = {STAGES[i % len(STAGES)]},')
        print("        .start_time = {.unit.year = 4, .unit.month = 6, .unit.day = 20, .unit.hour = 15, .unit.minute = 0},")
        print("        .end_time = {.unit.year = 4, .unit.month = 6, .unit.day = 20, .unit.hour = 16, .unit.minute = 0},")
        print(f'        .genre = {findGenre(act)},')
        print(f'        .popularity = {get_ranking(sorted_listing, act, "overall")}')
        print("    },")


if __name__ == "__main__":
    listActs = []
    for key in dicto:
        for i in dicto[key]:
            listActs.append(i)
    listActs = sorted(listActs, key=str.casefold)

    listActsPop = junfive if USE_TEST_ARR else getFullArray(listActs)

    # sorted(listActsPop, key=lambda x: (x['popularity'], x['followers']), reverse=True) If you want to first sort by popularity and followers as the tie-breaker
    sorted_listing = sorted(listActsPop, key=lambda x: (x['followers']), reverse=True)
    for i, artist in enumerate(sorted_listing):
        artist['overall'] = i + 1
        
    if PRINT_RANKINGs: 
        print_md_lst(sorted_listing)
        
    if PRINT_ARR:
        print_array_for_watch(listActs, sorted_listing)