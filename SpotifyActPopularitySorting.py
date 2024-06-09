import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from unidecode import unidecode
import json

PRINT_ARR = 1
PRINT_RANKINGs = 0
USE_TEST_ARR = 0
PRINT_SEARCH_RESULTS = 1

junNine = [{'name': 'ACRAZE', 'followers': 127443, 'popularity': 63}, {'name': 'AK Sports', 'followers': 3331, 'popularity': 19}, {'name': 'ALLEYCVT', 'followers': 36877, 'popularity': 41}, 
           {'name': 'ATLiens', 'followers': 98615, 'popularity': 45}, {'name': 'AYYBO', 'followers': 52905, 'popularity': 56}, {'name': 'Baggi', 'followers': 4166, 'popularity': 19}, 
           {'name': 'Barclay Crenshaw', 'followers': 31378, 'popularity': 35}, {'name': 'Ben Böhmer', 'followers': 497133, 'popularity': 62}, {'name': 'Black Tiger Sex Machine', 'followers': 167306, 'popularity': 46},
           {'name': 'Blastoyz', 'followers': 112539, 'popularity': 44}, {'name': 'Boogie T', 'followers': 90501, 'popularity': 43}, {'name': 'Boogie T', 'followers': 90501, 'popularity': 43}, 
           {'name': 'Boogie T.rio', 'followers': 19338, 'popularity': 28}, {'name': 'Brandi Cyrus', 'followers': 0, 'popularity': 0}, {'name': 'Calussa', 'followers': 8622, 'popularity': 45}, 
           {'name': 'CanaBliss', 'followers': 13432, 'popularity': 33}, {'name': 'Cannons', 'followers': 362225, 'popularity': 59}, {'name': 'Caspa', 'followers': 68293, 'popularity': 31}, 
           {'name': 'Cassian', 'followers': 56932, 'popularity': 53}, {'name': 'Chaos in the CBD', 'followers': 101956, 'popularity': 46}, {'name': 'Charlotte De Witte', 'followers': 940142, 'popularity': 59}, 
           {'name': 'Chase & Status', 'followers': 918048, 'popularity': 68}, {'name': 'Coco & Breezy', 'followers': 20131, 'popularity': 44}, {'name': 'Cuco', 'followers': 1059, 'popularity': 32}, 
           {'name': 'Dimension', 'followers': 127046, 'popularity': 60}, {'name': 'Dirtwire', 'followers': 96771, 'popularity': 42}, {'name': "Dixon's Violin", 'followers': 4923, 'popularity': 10}, 
           {'name': 'DJ Brownie', 'followers': 247, 'popularity': 5}, {'name': 'DJ Susan', 'followers': 32209, 'popularity': 31}, {'name': 'DJ Tennis', 'followers': 40984, 'popularity': 42}, 
           {'name': 'DRAMA', 'followers': 143969, 'popularity': 56}, {'name': 'Dumpstaphunk', 'followers': 51936, 'popularity': 30}, {'name': 'Eggy', 'followers': 10580, 'popularity': 27}, 
           {'name': 'Emo Nite', 'followers': 0, 'popularity': 0}, {'name': 'Equanimous', 'followers': 48934, 'popularity': 46}, {'name': 'Excision', 'followers': 727394, 'popularity': 59}, 
           {'name': 'G jones', 'followers': 91165, 'popularity': 36}, {'name': 'Goodboys', 'followers': 66372, 'popularity': 66}, {'name': 'Green Velvet', 'followers': 230796, 'popularity': 52}, 
           {'name': 'H&RRY', 'followers': 0, 'popularity': 0}, {'name': 'Hamdi', 'followers': 52981, 'popularity': 54}, {'name': 'hiatus kaiyote', 'followers': 627658, 'popularity': 56}, 
           {'name': 'INZO', 'followers': 154464, 'popularity': 50}, {'name': "it's murph", 'followers': 47270, 'popularity': 58}, {'name': 'Ivy Lab', 'followers': 84934, 'popularity': 40}, 
           {'name': 'Jason Leech', 'followers': 7195, 'popularity': 25}, {'name': 'Jjuujjuu', 'followers': 9013, 'popularity': 21}, {'name': 'John Summit', 'followers': 301175, 'popularity': 70}, 
           {'name': 'Juelz', 'followers': 31169, 'popularity': 43}, {'name': 'Kallaghan', 'followers': 477, 'popularity': 15}, {'name': 'Kenny Beats', 'followers': 204250, 'popularity': 60}, 
           {'name': 'Kiltro', 'followers': 33964, 'popularity': 42}, {'name': 'Knock2', 'followers': 93766, 'popularity': 56}, {'name': 'Layton Giordani', 'followers': 75628, 'popularity': 56}, 
           {'name': 'Le Youth', 'followers': 113340, 'popularity': 51}, {'name': 'League of Sound Disciples', 'followers': 0, 'popularity': 0}, {'name': 'Lettuce', 'followers': 212505, 'popularity': 41}, 
           {'name': 'LEVEL UP', 'followers': 36127, 'popularity': 44}, {'name': 'levity', 'followers': 34961, 'popularity': 45}, {'name': 'Libianca', 'followers': 466472, 'popularity': 64}, 
           {'name': 'Little stranger', 'followers': 56964, 'popularity': 49}, {'name': 'LP Giobbi', 'followers': 75423, 'popularity': 59}, {'name': 'Lucii', 'followers': 67333, 'popularity': 42}, 
           {'name': 'Ludacris', 'followers': 2956027, 'popularity': 75}, {'name': 'LYNY', 'followers': 14268, 'popularity': 42}, {'name': "Maddy O'Neal", 'followers': 18376, 'popularity': 34}, 
           {'name': 'Major League Djz', 'followers': 847150, 'popularity': 49}, {'name': 'marsh', 'followers': 70340, 'popularity': 51}, {'name': 'Mascolo', 'followers': 2369, 'popularity': 37}, 
           {'name': 'MASONIC', 'followers': 101, 'popularity': 0}, {'name': 'Matroda', 'followers': 126533, 'popularity': 57}, {'name': 'Mau P', 'followers': 102798, 'popularity': 62}, 
           {'name': 'Michaël Brun', 'followers': 49131, 'popularity': 49}, {'name': 'Mojave Grey', 'followers': 3749, 'popularity': 25}, {'name': 'Moontricks', 'followers': 58562, 'popularity': 43},
           {'name': 'NEIL FRANCES', 'followers': 209504, 'popularity': 64}, {'name': 'Nelly Furtado', 'followers': 3872513, 'popularity': 75}, {'name': 'Neoma', 'followers': 12651, 'popularity': 27},
           {'name': 'odd Mob', 'followers': 73335, 'popularity': 58}, {'name': 'ODEN & Fatzo', 'followers': 36752, 'popularity': 55}, {'name': 'Only fire', 'followers': 41118, 'popularity': 38},
           {'name': 'PAPERWATER', 'followers': 1441, 'popularity': 19}, {'name': 'Peach Tree Rascals', 'followers': 228168, 'popularity': 54}, {'name': 'Politik', 'followers': 330, 'popularity': 6},
           {'name': 'Polyrhythmics', 'followers': 28886, 'popularity': 31}, {'name': 'Pretty Lights', 'followers': 558920, 'popularity': 49}, {'name': 'Pretty Pink', 'followers': 45387, 'popularity': 46},
           {'name': 'Próxima Parada', 'followers': 66440, 'popularity': 49}, {'name': 'Ranger Trucco', 'followers': 10617, 'popularity': 32}, {'name': 'Rawayana', 'followers': 661921, 'popularity': 64},
           {'name': 'Rayben', 'followers': 42063, 'popularity': 40}, {'name': 'Redrum', 'followers': 2589, 'popularity': 11}, {'name': 'Sammy Virji', 'followers': 108236, 'popularity': 60},
           {'name': 'Sara Landry', 'followers': 197232, 'popularity': 51}, {'name': 'Seven lions', 'followers': 487783, 'popularity': 58}, {'name': 'Shae District', 'followers': 2666, 'popularity': 15},
           {'name': 'Shaun Ross', 'followers': 5623, 'popularity': 41}, {'name': 'Slayyyter', 'followers': 398088, 'popularity': 53}, {'name': 'Subtronics', 'followers': 307465, 'popularity': 61},
           {'name': 'Subtronics', 'followers': 307465, 'popularity': 61}, {'name': 'Sultan + Shepard', 'followers': 126035, 'popularity': 55}, {'name': 'Super Future', 'followers': 13398, 'popularity': 28},
           {'name': 'Swaylo', 'followers': 36, 'popularity': 1}, {'name': 'The Disco Biscuits', 'followers': 86190, 'popularity': 33}, {'name': 'The String Cheese Incident', 'followers': 226655, 'popularity': 41},
           {'name': 'Thought process', 'followers': 8325, 'popularity': 28}, {'name': 'Tripp St.', 'followers': 14917, 'popularity': 29}, {'name': 'TSHA', 'followers': 71776, 'popularity': 48},
           {'name': "Umphrey's McGee", 'followers': 201581, 'popularity': 40}, {'name': 'Unusual demont', 'followers': 43567, 'popularity': 41}, {'name': 'venbee', 'followers': 79249, 'popularity': 55},
           {'name': 'Vini Vici', 'followers': 527349, 'popularity': 62}, {'name': 'Westend', 'followers': 47026, 'popularity': 56}, {'name': 'Whyte Fang', 'followers': 15168, 'popularity': 27},
           {'name': 'Will Clarke', 'followers': 50284, 'popularity': 42}, {'name': 'Wooli', 'followers': 112828, 'popularity': 55}, {'name': 'Zen Selekta', 'followers': 3780, 'popularity': 16},
           {'name': 'Gigantic NGHTMRE', 'followers': 360263, 'popularity': 52}, {'name': 'EVERYTHING ALWAYS', 'followers': 351772, 'popularity': 68}, {'name': 'LSZEE', 'followers': 168478, 'popularity': 49},
           {'name': 'VNSSA B2B Nala', 'followers': 13823, 'popularity': 35}, {'name': 'Hyperbeam', 'followers': 46701, 'popularity': 53}]

dicto = {"DUBSTEP": ["ALLEYCVT",
                    "ATLiens",
                    "Barclay Crenshaw",
                    "Black Tiger Sex Machine",
                    "Caspa",
                    "Excision",
                    "Gigantic NGHTMRE",
                    "Hamdi",
                    "LEVEL UP",
                    "Lucii",
                    "LYNY",
                    "LSZEE",             
                    "Subtronics",           
                    "Whyte Fang",
                    "Seven lions",
                    "Boogie T",
                    "CanaBliss",
                    "levity",
                    "Hyperbeam",
                    ],
        "DnB":   ["Chase & Status",
                  "Dimension",
                  "AK Sports",
                  "Sammy Virji",
                  "Subtronics",
                  "venbee",
                  "Wooli",
                  "G jones",
                  "Boogie T",
                  "Ivy Lab",
                  "Super Future",
                  "Zen Selekta",],
         "HOUSE": ["ACRAZE",
                   "AYYBO",
                   "Ben Böhmer",
                   "Calussa",
                   "Cassian",
                   "EVERYTHING ALWAYS",
                   "Green Velvet",
                   "John Summit",
                   "Knock2",
                   "Le Youth",
                   "Major League Djz",
                   "Matroda",
                   "Mau P",
                   "ODEN & Fatzo",
                   "Ranger Trucco",
                   "Sultan + Shepard",
                   "TSHA",
                   "Vini Vici",
                   "VNSSA B2B Nala",
                   "Westend",
                   "Will Clarke",
                   "Baggi",
                   "Brandi Cyrus",
                   "Chaos in the CBD",
                   "H&RRY",
                   "marsh",
                   "MASONIC",
                   "Mojave Grey",
                   "odd Mob",
                   "Only fire",
                   "Rayben",
                   "Shae District",
                   "Swaylo",
                   "DJ Brownie",
                   "Kallaghan",
                   "Pretty Pink",              
                   ],
         "DANCE": ["Coco & Breezy",
                   "DJ Tennis",
                   "DRAMA",
                   "it's murph",
                   "LP Giobbi",
                   "Michaël Brun",
                   "DJ Susan",
                   "Boogie T.rio",
                   "Jason Leech",
                   "Shaun Ross",],
         "TECHNO" :["Charlotte De Witte",
                    "Sara Landry",
                    "Layton Giordani",
                    "Blastoyz",
                    ],
         "INDIE": ["Cuco",
                   "NEIL FRANCES",
                   "Peach Tree Rascals",
                   "Emo Nite",
                   "Equanimous",
                   "Kiltro",
                   "Goodboys",],
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
                 "The Disco Biscuits",
                 "The String Cheese Incident",
                 "Umphrey's McGee",
                 "Jjuujjuu",
                 "Próxima Parada",
                 "League of Sound Disciples",
                 ],
         "TRAP": ["INZO",
                  "Juelz",
                  "Maddy O'Neal",
                  "Redrum",
                  "Thought process",
                  "Tripp St.",
                  "Politik",
                  ],
         "RAP": ["Kenny Beats",
                 "Libianca",
                 "Ludacris",
                 "PAPERWATER",
                 "hiatus kaiyote",
                 "Little stranger",],
         "SOUL": ["Dixon's Violin",
                  "Rawayana",
                  "Polyrhythmics",
                  "Moontricks"]
         }


for_spotify ={"Gigantic NGHTMRE" : ["Big Gigantic","NGHTMRE"],
              "EVERYTHING ALWAYS" : ["Dom Dolla","John Summit"],
              "LSZEE": ["CloZee","LSDREAM"],
              "VNSSA B2B Nala" : ["VNSSA","Nala"],
              "Hyperbeam" : ["odd Mob", "Omnom"]}


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
        print(f"{dupes} EXACT MATCHES FOUND FOR: {artist_name}: {names_in_search}")
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

def strip_word(text, words_to_remove):
    words = text.split()
    stripped_words = [word for word in words if word.lower() not in map(str.lower, words_to_remove)]
    stripped_text = ' '.join(stripped_words)
    return stripped_text

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
                return key
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
        act_spot = for_spotify.get(act, act)
        if isinstance(act_spot,list):
            continue # We'll get and average the duos later.
        followers, popularity = get_artist_followers_popularity(act_spot, client_id, client_secret)
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
    longestNum = 5
    longestAct = 25
    longestPop = 15
    longestFol = 10
    numTitle = "Num"
    actTitle = "Act"
    popTitle = "Popularity"
    folTitle = "Followers"
    print(f"| {numTitle: ^{longestNum}} | {actTitle: ^{longestAct}} | {popTitle : ^{longestPop}} | {folTitle : ^{longestFol}} |")
    print(f"| {'-' * longestNum} | {'-' * longestAct} | {'-' * longestPop} | {'-' * longestFol} |")
    for num, item in enumerate(sorted_listing):
        act = item['name']
        popularity = item['popularity']
        followers = f"{item['followers']:,}"
        print(f"| {num + 1 : ^{longestNum}} | {act : ^{longestAct}} | {popularity : ^{longestPop}} | {followers : ^{longestFol}} |")


def print_array_for_watch(listActs, sorted_listing):
    for i, act in enumerate(listActs):
        actToDisp = unidecode(act)
        actToDisp = strip_word(actToDisp,["The"])
        actToDisp = f"{actToDisp.upper()[:6]: <6}"
        print("    {")
        print(f'        .artist = "{actToDisp}",')
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

    listActsPop = junNine if USE_TEST_ARR else getFullArray(listActs)

    # sorted(listActsPop, key=lambda x: (x['popularity'], x['followers']), reverse=True) If you want to first sort by popularity and followers as the tie-breaker
    sorted_listing = sorted(listActsPop, key=lambda x: (x['followers']), reverse=True)
    for i, artist in enumerate(sorted_listing):
        artist['overall'] = i + 1
        
    if PRINT_RANKINGs: 
        print_md_lst(sorted_listing)
        
    if PRINT_ARR:
        print_array_for_watch(listActs, sorted_listing)