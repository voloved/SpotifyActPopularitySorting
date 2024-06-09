import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from unidecode import unidecode
import json
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import difflib
import pytz

TZ = pytz.timezone('US/Eastern')

PRINT_ARR = 0
PRINT_RANKINGs = 1
USE_TEST_ARR = 0
PRINT_SEARCH_RESULTS = 1
SORT_POP_BY_FOLLOWERS = 0

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
           {'name': 'Sultan + Shepard', 'followers': 126035, 'popularity': 55}, {'name': 'Super Future', 'followers': 13398, 'popularity': 28},
           {'name': 'Swaylo', 'followers': 36, 'popularity': 1}, {'name': 'The Disco Biscuits', 'followers': 86190, 'popularity': 33}, {'name': 'The String Cheese Incident', 'followers': 226655, 'popularity': 41},
           {'name': 'Thought process', 'followers': 8325, 'popularity': 28}, {'name': 'Tripp St.', 'followers': 14917, 'popularity': 29}, {'name': 'TSHA', 'followers': 71776, 'popularity': 48},
           {'name': "Umphrey's McGee", 'followers': 201581, 'popularity': 40}, {'name': 'Unusual demont', 'followers': 43567, 'popularity': 41}, {'name': 'venbee', 'followers': 79249, 'popularity': 55},
           {'name': 'Vini Vici', 'followers': 527349, 'popularity': 62}, {'name': 'Westend', 'followers': 47026, 'popularity': 56}, {'name': 'Whyte Fang', 'followers': 15168, 'popularity': 27},
           {'name': 'Will Clarke', 'followers': 50284, 'popularity': 42}, {'name': 'Wooli', 'followers': 112828, 'popularity': 55}, {'name': 'Zen Selekta', 'followers': 3780, 'popularity': 16},
           {'name': 'Gigantic NGHTMRE', 'followers': 360263, 'popularity': 52}, {'name': 'EVERYTHING ALWAYS', 'followers': 351772, 'popularity': 68}, {'name': 'LSZEE', 'followers': 168478, 'popularity': 49},
           {'name': 'VNSSA B2B Nala', 'followers': 13823, 'popularity': 35}, {'name': 'Hyperbeam', 'followers': 46701, 'popularity': 53}]


test_content = """
<div class="day" data-date="1687406400" data-first-start="32400" data-last-stop="104400"><h2 class="dayName">Thurs&#8203;day 22nd June</h2>
<div class="stage"><h3 class="stageName">Carousel Club</h3>
<div class="actLists"><div class="act id-neighb-1 " data-id="neighb-1" data-start-time="1687471200000" data-end-time="1687475700000" ><span class="actTime">18:00 - 19:15</span><span class="actNm">Neighbor</span></div><div class="act id-cimafu-1 " data-id="cimafu-1" data-start-time="1687479300000" data-end-time="1687483800000" data-mbid="1be1831c-48ac-4adc-aca9-cc4c5b3b6912" ><span class="actTime">20:15 - 21:30</span><span class="actNm">Cimafunk</span></div><div class="act id-sadnig-1 " data-id="sadnig-1" data-start-time="1687486500000" data-end-time="1687491000000" data-mbid="788d1529-8bbd-4e85-9684-7ca58bb4ed92" ><span class="actTime">22:15 - 23:30</span><span class="actNm">Sad Night Dynamite</span></div></div>
</div><div class="stage"><h3 class="stageName">Honeycomb</h3>
<div class="actLists"><div class="act id-lvdy-1 " data-id="lvdy-1" data-start-time="1687472100000" data-end-time="1687475700000" ><span class="actTime">18:15 - 19:15</span><span class="actNm">LVDY</span></div><div class="act id-samuel-1 " data-id="samuel-1" data-start-time="1687476600000" data-end-time="1687480200000" ><span class="actTime">19:30 - 20:30</span><span class="actNm">Samuel J Music</span></div><div class="act id-cid-2 " data-id="cid-2" data-start-time="1687482000000" data-end-time="1687485600000" ><span class="actTime">21:00 - 22:00</span><span class="actNm">CID</span></div><div class="act id-gaship-1 " data-id="gaship-1" data-start-time="1687487400000" data-end-time="1687490100000" ><span class="actTime">22:30 - 23:15</span><span class="actNm">Gashi Presents: Nostalgia 1984</span></div><div class="act id-politi-2 " data-id="politi-2" data-start-time="1687496400000" data-end-time="1687500000000" ><span class="actTime">01:00 - 02:00</span><span class="actNm">Politik</span></div></div>
</div><div class="stage"><h3 class="stageName">Ranch Arena</h3>
<div class="actLists"><div class="act id-eazyba-1 " data-id="eazyba-1" data-start-time="1687460400000" data-end-time="1687464000000" data-mbid="03a772ac-f7cf-4e85-a087-44c6718f52d2" ><span class="actTime">15:00 - 16:00</span><span class="actNm">Eazybaked</span></div><div class="act id-politi-1 " data-id="politi-1" data-start-time="1687465800000" data-end-time="1687469400000" ><span class="actTime">16:30 - 17:30</span><span class="actNm">Politik</span></div><div class="act id-gashi-1 " data-id="gashi-1" data-start-time="1687471200000" data-end-time="1687474800000" ><span class="actTime">18:00 - 19:00</span><span class="actNm">Gashi</span></div><div class="act id-channe-1 " data-id="channe-1" data-start-time="1687477500000" data-end-time="1687482000000" data-mbid="a9d53ca9-6c28-4be9-ab10-6c936a11d70b" ><span class="actTime">19:45 - 21:00</span><span class="actNm">Channel Tres</span></div><div class="act id-sofitu-1 " data-id="sofitu-1" data-start-time="1687483800000" data-end-time="1687487400000" data-mbid="4ac723f4-8be8-4a0d-a3ae-d5dda20f0a9a" ><span class="actTime">21:30 - 22:30</span><span class="actNm">Sofi Tukker</span></div><div class="act id-odesza-1 " data-id="odesza-1" data-start-time="1687491900000" data-end-time="1687497300000" data-mbid="2e222fce-02ae-4221-b1c6-3c3242b423b6" ><span class="actTime">23:45 - 01:15</span><span class="actNm">Odesza</span></div></div>
</div><div class="stage"><h3 class="stageName">Sherwood Court</h3>
<div class="actLists"><div class="act id-cococl-1 " data-id="cococl-1" data-start-time="1687467600000" data-end-time="1687471200000" ><span class="actTime">17:00 - 18:00</span><span class="actNm">Coco & Clair Clair</span></div><div class="act id-emotio-1 " data-id="emotio-1" data-start-time="1687474800000" data-end-time="1687478400000" ><span class="actTime">19:00 - 20:00</span><span class="actNm">Emotional Oranges</span></div><div class="act id-satinj-1 " data-id="satinj-1" data-start-time="1687480200000" data-end-time="1687484700000" ><span class="actTime">20:30 - 21:45</span><span class="actNm">Satin Jackets</span></div><div class="act id-sglewi-1 " data-id="sglewi-1" data-start-time="1687487400000" data-end-time="1687491000000" data-mbid="ab413f29-71af-4f7f-8ca8-5ece68beeaf3" ><span class="actTime">22:30 - 23:30</span><span class="actNm">SG Lewis</span></div><div class="act id-jamiex-1 " data-id="jamiex-1" data-start-time="1687493700000" data-end-time="1687499100000" data-mbid="d1515727-4a93-4c0d-88cb-d7a9fce01879" ><span class="actTime">00:15 - 01:45</span><span class="actNm">Jamie xx</span></div></div>
</div><div class="stage"><h3 class="stageName">Silent Disco (Blue Channel)</h3>
<div class="actLists"><div class="act id-seoulc-1 " data-id="seoulc-1" data-start-time="1687474800000" data-end-time="1687478400000" ><span class="actTime">19:00 - 20:00</span><span class="actNm">Seoul City</span></div><div class="act id-whiteo-1 " data-id="whiteo-1" data-start-time="1687478400000" data-end-time="1687482000000" ><span class="actTime">20:00 - 21:00</span><span class="actNm">White Owl</span></div><div class="act id-samwhi-1 " data-id="samwhi-1" data-start-time="1687482000000" data-end-time="1687485600000" ><span class="actTime">21:00 - 22:00</span><span class="actNm">Sam White</span></div><div class="act id-meking-1 " data-id="meking-1" data-start-time="1687485600000" data-end-time="1687489200000" ><span class="actTime">22:00 - 23:00</span><span class="actNm">Mekington</span></div><div class="act id-ayoo-1 " data-id="ayoo-1" data-start-time="1687489200000" data-end-time="1687492800000" ><span class="actTime">23:00 - 00:00</span><span class="actNm">Ayoo</span></div><div class="act id-xonic-1 " data-id="xonic-1" data-start-time="1687492800000" data-end-time="1687496400000" ><span class="actTime">00:00 - 01:00</span><span class="actNm">Xonic</span></div><div class="act id-tsunam-1 " data-id="tsunam-1" data-start-time="1687496400000" data-end-time="1687500000000" ><span class="actTime">01:00 - 02:00</span><span class="actNm">Tsunami</span></div></div>
</div><div class="stage"><h3 class="stageName">Silent Disco (Green Channel)</h3>
<div class="actLists"><div class="act id-golden-1 " data-id="golden-1" data-start-time="1687474800000" data-end-time="1687479300000" ><span class="actTime">19:00 - 20:15</span><span class="actNm">Golden Goddess</span></div><div class="act id-chayu-1 " data-id="chayu-1" data-start-time="1687479300000" data-end-time="1687483800000" ><span class="actTime">20:15 - 21:30</span><span class="actNm">Chayu</span></div><div class="act id-candl-1 " data-id="candl-1" data-start-time="1687483800000" data-end-time="1687487400000" ><span class="actTime">21:30 - 22:30</span><span class="actNm">CANDL</span></div><div class="act id-michae-1 " data-id="michae-1" data-start-time="1687487400000" data-end-time="1687491000000" ><span class="actTime">22:30 - 23:30</span><span class="actNm">Michael Milano</span></div><div class="act id-motion-1 " data-id="motion-1" data-start-time="1687491000000" data-end-time="1687495500000" ><span class="actTime">23:30 - 00:45</span><span class="actNm">Motion Potion</span></div><div class="act id-pumath-1 " data-id="pumath-1" data-start-time="1687495500000" data-end-time="1687500000000" ><span class="actTime">00:45 - 02:00</span><span class="actNm">Puma Thurman</span></div></div>
</div><div class="stage"><h3 class="stageName">The Brainery</h3>
<div class="actLists"><div class="act id-ground-1 " data-id="ground-1" data-start-time="1687439700000" data-end-time="1687442400000" ><span class="actTime">09:15 - 10:00</span><span class="actNm">Grounding Into The Forest</span></div><div class="act id-intent-1 " data-id="intent-1" data-start-time="1687444200000" data-end-time="1687446900000" ><span class="actTime">10:30 - 11:15</span><span class="actNm">Intention Setting For A Magical Weekend</span></div><div class="act id-wallyt-1 " data-id="wallyt-1" data-start-time="1687447800000" data-end-time="1687449600000" ><span class="actTime">11:30 - 12:00</span><span class="actNm">Wally Talks: The Health of the Forest</span></div><div class="act id-polyam-1 " data-id="polyam-1" data-start-time="1687450500000" data-end-time="1687454100000" ><span class="actTime">12:15 - 13:15</span><span class="actNm">Polyamory 101</span></div><div class="act id-wallyt1-1 " data-id="wallyt1-1" data-start-time="1687455000000" data-end-time="1687456800000" ><span class="actTime">13:30 - 14:00</span><span class="actNm">Wally Talks: ft. The Festival Dad</span></div><div class="act id-reddit1-1 " data-id="reddit1-1" data-start-time="1687457700000" data-end-time="1687459500000" ><span class="actTime">14:15 - 14:45</span><span class="actNm">Reddit Meet-up</span></div><div class="act id-colorm-1 " data-id="colorm-1" data-start-time="1687461300000" data-end-time="1687467600000" ><span class="actTime">15:15 - 17:00</span><span class="actNm">Color Meditation: Spirit Painting</span></div><div class="act id-sethwa-1 " data-id="sethwa-1" data-start-time="1687503600000" data-end-time="1687510800000" ><span class="actTime">03:00 - 05:00</span><span class="actNm">Sethward's Show & Tell Spectacular</span></div></div>
</div><div class="stage"><h3 class="stageName">The Observatory</h3>
<div class="actLists"><div class="act id-dixons-1 " data-id="dixons-1" data-start-time="1687460400000" data-end-time="1687464000000" data-mbid="2cc0c42d-a27a-43fe-bee4-ea12b8572322" ><span class="actTime">15:00 - 16:00</span><span class="actNm">Dixon's Violin</span></div><div class="act id-daniel-1 " data-id="daniel-1" data-start-time="1687466700000" data-end-time="1687470300000" data-mbid="e7765329-e8ed-4f84-a69b-394212b631dd" ><span class="actTime">16:45 - 17:45</span><span class="actNm">Danielle Ponder</span></div><div class="act id-masane-1 " data-id="masane-1" data-start-time="1687473000000" data-end-time="1687477500000" ><span class="actTime">18:30 - 19:45</span><span class="actNm">Masane</span></div><div class="act id-embrz-1 " data-id="embrz-1" data-start-time="1687477500000" data-end-time="1687482000000" ><span class="actTime">19:45 - 21:00</span><span class="actNm">Embrz</span></div><div class="act id-nilsho-1 " data-id="nilsho-1" data-start-time="1687482000000" data-end-time="1687485600000" ><span class="actTime">21:00 - 22:00</span><span class="actNm">Nils Hoffman</span></div><div class="act id-cosmic-1 " data-id="cosmic-1" data-start-time="1687487400000" data-end-time="1687492800000" data-mbid="5f3b32e5-efb5-4096-9260-587c155e50b7" ><span class="actTime">22:30 - 00:00</span><span class="actNm">Cosmic Gate</span></div><div class="act id-infect-1 " data-id="infect-1" data-start-time="1687492800000" data-end-time="1687498200000" data-mbid="eab76c9f-ff91-4431-b6dd-3b976c598020" ><span class="actTime">00:00 - 01:30</span><span class="actNm">Infected Mushroom</span></div></div>
</div><div class="stage"><h3 class="stageName">Tripolee</h3>
<div class="actLists"><div class="act id-cocoro-1 " data-id="cocoro-1" data-start-time="1687458600000" data-end-time="1687462200000" ><span class="actTime">14:30 - 15:30</span><span class="actNm">Coco Robano</span></div><div class="act id-missdr-1 " data-id="missdr-1" data-start-time="1687462200000" data-end-time="1687465800000" ><span class="actTime">15:30 - 16:30</span><span class="actNm">Miss Dre</span></div><div class="act id-cid-1 " data-id="cid-1" data-start-time="1687465800000" data-end-time="1687470300000" ><span class="actTime">16:30 - 17:45</span><span class="actNm">CID</span></div><div class="act id-hugel-1 " data-id="hugel-1" data-start-time="1687470300000" data-end-time="1687474800000" ><span class="actTime">17:45 - 19:00</span><span class="actNm">Hugel</span></div><div class="act id-jworra-1 " data-id="jworra-1" data-start-time="1687474800000" data-end-time="1687479300000" data-mbid="32c9d11e-a63f-483f-8bed-b51fee2a81c5" ><span class="actTime">19:00 - 20:15</span><span class="actNm">J. Worra</span></div><div class="act id-leefos-1 " data-id="leefos-1" data-start-time="1687479300000" data-end-time="1687483800000" data-mbid="ec6477a4-94e4-43ac-b6dc-b205e38a6a6e" ><span class="actTime">20:15 - 21:30</span><span class="actNm">Lee Foss</span></div><div class="act id-totall-1 " data-id="totall-1" data-start-time="1687483800000" data-end-time="1687488300000" data-mbid="bd075a82-b196-4752-a1bb-3d87be3236a0" ><span class="actTime">21:30 - 22:45</span><span class="actNm">Totally Enormous Extinct Dinosaurs</span></div><div class="act id-walker-1 " data-id="walker-1" data-start-time="1687488300000" data-end-time="1687492800000" data-mbid="cb592bc3-6c4d-4ac1-b429-a67017910051" ><span class="actTime">22:45 - 00:00</span><span class="actNm">Walker & Royce</span></div><div class="act id-gorgon-1 " data-id="gorgon-1" data-start-time="1687492800000" data-end-time="1687498200000" data-mbid="ba8aaa28-2de4-4d5c-824e-1e9d49235c55" ><span class="actTime">00:00 - 01:30</span><span class="actNm">Gorgon City</span></div></div>
</div></div><div class="day" data-date="1687492800" data-first-start="32400" data-last-stop="104400"><h2 class="dayName">Fri&#8203;day 23rd June</h2>
<div class="stage"><h3 class="stageName">Carousel Club</h3>
<div class="actLists"><div class="act id-pawpaw-1 " data-id="pawpaw-1" data-start-time="1687555800000" data-end-time="1687559400000" ><span class="actTime">17:30 - 18:30</span><span class="actNm">Paw Paw Rod</span></div><div class="act id-tkayma-1 " data-id="tkayma-1" data-start-time="1687561200000" data-end-time="1687564800000" ><span class="actTime">19:00 - 20:00</span><span class="actNm">Tkay Maidza</span></div><div class="act id-kerala-1 " data-id="kerala-1" data-start-time="1687566600000" data-end-time="1687570200000" ><span class="actTime">20:30 - 21:30</span><span class="actNm">Kerala Dust</span></div><div class="act id-jupite-1 " data-id="jupite-1" data-start-time="1687572000000" data-end-time="1687576500000" data-mbid="a03e478a-a8b4-46e6-9c8f-239cb8e62823" ><span class="actTime">22:00 - 23:15</span><span class="actNm">Jupiter & Okwess</span></div><div class="act id-discol-1 " data-id="discol-1" data-start-time="1687579200000" data-end-time="1687583700000" ><span class="actTime">00:00 - 01:15</span><span class="actNm">Disco Lines</span></div></div>
</div><div class="stage"><h3 class="stageName">Honeycomb</h3>
<div class="actLists"><div class="act id-femmei-1 " data-id="femmei-1" data-start-time="1687546800000" data-end-time="1687550400000" ><span class="actTime">15:00 - 16:00</span><span class="actNm">Femme Indentifying Circle</span></div><div class="act id-rumble-1 " data-id="rumble-1" data-start-time="1687554000000" data-end-time="1687561200000" ><span class="actTime">17:00 - 19:00</span><span class="actNm">Rumble in the Bumble</span></div><div class="act id-lvdy-2 " data-id="lvdy-2" data-start-time="1687562100000" data-end-time="1687565700000" ><span class="actTime">19:15 - 20:15</span><span class="actNm">LVDY</span></div><div class="act id-therap-1 " data-id="therap-1" data-start-time="1687568400000" data-end-time="1687572000000" ><span class="actTime">21:00 - 22:00</span><span class="actNm">Therapy Gecko</span></div><div class="act id-samuel-2 " data-id="samuel-2" data-start-time="1687573800000" data-end-time="1687577400000" ><span class="actTime">22:30 - 23:30</span><span class="actNm">Samuel J Music</span></div><div class="act id-robbie-1 " data-id="robbie-1" data-start-time="1687579200000" data-end-time="1687582800000" ><span class="actTime">00:00 - 01:00</span><span class="actNm">Robbie Fitzsimmons</span></div><div class="act id-daveya-1 " data-id="daveya-1" data-start-time="1687584600000" data-end-time="1687588200000" ><span class="actTime">01:30 - 02:30</span><span class="actNm">Dave Yaden + Danny Asadi</span></div></div>
</div><div class="stage"><h3 class="stageName">Ranch Arena</h3>
<div class="actLists"><div class="act id-austin-1 " data-id="austin-1" data-start-time="1687555800000" data-end-time="1687560300000" ><span class="actTime">17:30 - 18:45</span><span class="actNm">Austin Millz</span></div><div class="act id-fletch-1 " data-id="fletch-1" data-start-time="1687563000000" data-end-time="1687566600000" data-mbid="a66091aa-e093-46bb-916a-387aba16e15c" ><span class="actTime">19:30 - 20:30</span><span class="actNm">FLETCHER</span></div><div class="act id-string1-1 " data-id="string1-1" data-start-time="1687568400000" data-end-time="1687575600000" data-mbid="cff95140-6d57-498a-8834-10eb72865b29" ><span class="actTime">21:00 - 23:00</span><span class="actNm">The String Cheese Incident</span></div><div class="act id-illeni-1 " data-id="illeni-1" data-start-time="1687580100000" data-end-time="1687585500000" data-mbid="5f43abf6-92a5-468a-a633-b73f94627972" ><span class="actTime">00:15 - 01:45</span><span class="actNm">Illenium</span></div></div>
</div><div class="stage"><h3 class="stageName">Sherwood Court</h3>
<div class="actLists"><div class="act id-forest-1 " data-id="forest-1" data-start-time="1687561200000" data-end-time="1687564800000" ><span class="actTime">19:00 - 20:00</span><span class="actNm">Forester</span></div><div class="act id-070sha-1 " data-id="070sha-1" data-start-time="1687568400000" data-end-time="1687572300000" data-mbid="741dbc8e-1cd5-4a66-b2b8-43bbad87ae12" ><span class="actTime">21:00 - 22:05</span><span class="actNm">070 Shake</span></div><div class="act id-lane8-1 " data-id="lane8-1" data-start-time="1687575600000" data-end-time="1687581000000" data-mbid="bd052b81-353a-4bce-8cd8-72ba9d4ce414" ><span class="actTime">23:00 - 00:30</span><span class="actNm">Lane 8</span></div><div class="act id-gryffi-1 " data-id="gryffi-1" data-start-time="1687584600000" data-end-time="1687590000000" data-mbid="f1348139-efb5-43c7-9204-199827efad3c" ><span class="actTime">01:30 - 03:00</span><span class="actNm">Gryffin</span></div></div>
</div><div class="stage"><h3 class="stageName">Silent Disco (Blue Channel)</h3>
<div class="actLists"><div class="act id-qurl-1 " data-id="qurl-1" data-start-time="1687561200000" data-end-time="1687564800000" ><span class="actTime">19:00 - 20:00</span><span class="actNm">QURL</span></div><div class="act id-alexwo-1 " data-id="alexwo-1" data-start-time="1687564800000" data-end-time="1687568400000" ><span class="actTime">20:00 - 21:00</span><span class="actNm">Alex Wood</span></div><div class="act id-vourte-1 " data-id="vourte-1" data-start-time="1687568400000" data-end-time="1687572000000" ><span class="actTime">21:00 - 22:00</span><span class="actNm">Vourteque</span></div><div class="act id-celest-1 " data-id="celest-1" data-start-time="1687572000000" data-end-time="1687575600000" ><span class="actTime">22:00 - 23:00</span><span class="actNm">Celestica</span></div><div class="act id-bishpl-1 " data-id="bishpl-1" data-start-time="1687575600000" data-end-time="1687579200000" ><span class="actTime">23:00 - 00:00</span><span class="actNm">Bish Plz</span></div><div class="act id-candl-2 " data-id="candl-2" data-start-time="1687579200000" data-end-time="1687582800000" ><span class="actTime">00:00 - 01:00</span><span class="actNm">Candl</span></div><div class="act id-michae-2 " data-id="michae-2" data-start-time="1687582800000" data-end-time="1687586400000" ><span class="actTime">01:00 - 02:00</span><span class="actNm">Michael Milano</span></div><div class="act id-tombz-1 " data-id="tombz-1" data-start-time="1687586400000" data-end-time="1687590000000" ><span class="actTime">02:00 - 03:00</span><span class="actNm">Tombz</span></div></div>
</div><div class="stage"><h3 class="stageName">Silent Disco (Green Channel)</h3>
<div class="actLists"><div class="act id-discov-1 " data-id="discov-1" data-start-time="1687561200000" data-end-time="1687564800000" ><span class="actTime">19:00 - 20:00</span><span class="actNm">Discovery Project</span></div><div class="act id-stack-1 " data-id="stack-1" data-start-time="1687564800000" data-end-time="1687568400000" ><span class="actTime">20:00 - 21:00</span><span class="actNm">Stack</span></div><div class="act id-pumath-2 " data-id="pumath-2" data-start-time="1687568400000" data-end-time="1687572000000" ><span class="actTime">21:00 - 22:00</span><span class="actNm">Puma Thurman</span></div><div class="act id-motion1-1 " data-id="motion1-1" data-start-time="1687572000000" data-end-time="1687576500000" ><span class="actTime">22:00 - 23:15</span><span class="actNm">Motion Potiom</span></div><div class="act id-keithk-1 " data-id="keithk-1" data-start-time="1687576500000" data-end-time="1687581000000" ><span class="actTime">23:15 - 00:30</span><span class="actNm">Keith KacKenzie</span></div><div class="act id-teddyb-1 " data-id="teddyb-1" data-start-time="1687581000000" data-end-time="1687585500000" ><span class="actTime">00:30 - 01:45</span><span class="actNm">Teddy Beats</span></div><div class="act id-krushe-1 " data-id="krushe-1" data-start-time="1687585500000" data-end-time="1687590000000" ><span class="actTime">01:45 - 03:00</span><span class="actNm">Krushendo</span></div></div>
</div><div class="stage"><h3 class="stageName">The Brainery</h3>
<div class="actLists"><div class="act id-powero-1 " data-id="powero-1" data-start-time="1687526100000" data-end-time="1687528800000" ><span class="actTime">09:15 - 10:00</span><span class="actNm">The Power of Sound Healing Frequency</span></div><div class="act id-mornin-1 " data-id="mornin-1" data-start-time="1687529700000" data-end-time="1687531500000" ><span class="actTime">10:15 - 10:45</span><span class="actNm">Morning Mindfulness: Guided Mediation Journey</span></div><div class="act id-deathr-1 " data-id="deathr-1" data-start-time="1687532400000" data-end-time="1687535100000" ><span class="actTime">11:00 - 11:45</span><span class="actNm">Death & Rebirth Meditation</span></div><div class="act id-erotic-1 " data-id="erotic-1" data-start-time="1687536000000" data-end-time="1687539600000" ><span class="actTime">12:00 - 13:00</span><span class="actNm">Erotic Blueprint Experience</span></div><div class="act id-clowni-1 " data-id="clowni-1" data-start-time="1687540500000" data-end-time="1687544100000" ><span class="actTime">13:15 - 14:15</span><span class="actNm">The Clown In You: Creativity Through Movement</span></div><div class="act id-herfor-1 " data-id="herfor-1" data-start-time="1687545000000" data-end-time="1687546800000" ><span class="actTime">14:30 - 15:00</span><span class="actNm">Her Forest Pres. Female Ravers United</span></div><div class="act id-braine-1 " data-id="braine-1" data-start-time="1687547700000" data-end-time="1687551300000" ><span class="actTime">15:15 - 16:15</span><span class="actNm">The Brainery Panel</span></div><div class="act id-braine-2 " data-id="braine-2" data-start-time="1687551600000" data-end-time="1687555200000" ><span class="actTime">16:20 - 17:20</span><span class="actNm">The Brainery Panel</span></div><div class="act id-sethwa-2 " data-id="sethwa-2" data-start-time="1687590000000" data-end-time="1687597200000" ><span class="actTime">03:00 - 05:00</span><span class="actNm">Sethward's Show & Tell Spectacular</span></div></div>
</div><div class="stage"><h3 class="stageName">The Observatory</h3>
<div class="actLists"><div class="act id-dixons-2 " data-id="dixons-2" data-start-time="1687546800000" data-end-time="1687550400000" data-mbid="2cc0c42d-a27a-43fe-bee4-ea12b8572322" ><span class="actTime">15:00 - 16:00</span><span class="actNm">Dixon's Violin</span></div><div class="act id-n3ptun-1 " data-id="n3ptun-1" data-start-time="1687552200000" data-end-time="1687555800000" ><span class="actTime">16:30 - 17:30</span><span class="actNm">N3ptune + Rusty Steve</span></div><div class="act id-azztec-1 " data-id="azztec-1" data-start-time="1687557600000" data-end-time="1687562100000" ><span class="actTime">18:00 - 19:15</span><span class="actNm">Azztecca</span></div><div class="act id-miane-1 " data-id="miane-1" data-start-time="1687562100000" data-end-time="1687566600000" ><span class="actTime">19:15 - 20:30</span><span class="actNm">Miane</span></div><div class="act id-malone-1 " data-id="malone-1" data-start-time="1687566600000" data-end-time="1687572000000" ><span class="actTime">20:30 - 22:00</span><span class="actNm">Malone</span></div><div class="act id-bontan1-1 " data-id="bontan1-1" data-start-time="1687572000000" data-end-time="1687577400000" ><span class="actTime">22:00 - 23:30</span><span class="actNm">Bontan</span></div><div class="act id-ameme1-1 " data-id="ameme1-1" data-start-time="1687577400000" data-end-time="1687582800000" ><span class="actTime">23:30 - 01:00</span><span class="actNm">Ameme</span></div><div class="act id-blondi1-1 " data-id="blondi1-1" data-start-time="1687582800000" data-end-time="1687588200000" ><span class="actTime">01:00 - 02:30</span><span class="actNm">Blond:ish</span></div></div>
</div><div class="stage"><h3 class="stageName">Tripolee</h3>
<div class="actLists"><div class="act id-yoga-1 " data-id="yoga-1" data-start-time="1687536000000" data-end-time="1687540500000" data-mbid="409b911e-1496-4238-a63a-25bcefe0f872" ><span class="actTime">12:00 - 13:15</span><span class="actNm">YOGA</span></div><div class="act id-fury-1 " data-id="fury-1" data-start-time="1687543200000" data-end-time="1687546800000" ><span class="actTime">14:00 - 15:00</span><span class="actNm">Fury</span></div><div class="act id-blackc-1 " data-id="blackc-1" data-start-time="1687546800000" data-end-time="1687550400000" ><span class="actTime">15:00 - 16:00</span><span class="actNm">Black Carl!</span></div><div class="act id-tapeb-1 " data-id="tapeb-1" data-start-time="1687550400000" data-end-time="1687554000000" data-mbid="cdee470d-8167-4c15-808e-c4ce7fa3d6e7" ><span class="actTime">16:00 - 17:00</span><span class="actNm">Tape B</span></div><div class="act id-zingar-1 " data-id="zingar-1" data-start-time="1687554000000" data-end-time="1687558500000" ><span class="actTime">17:00 - 18:15</span><span class="actNm">Zingara</span></div><div class="act id-truth-1 " data-id="truth-1" data-start-time="1687558500000" data-end-time="1687562100000" ><span class="actTime">18:15 - 19:15</span><span class="actNm">Truth</span></div><div class="act id-champa-1 " data-id="champa-1" data-start-time="1687562100000" data-end-time="1687566600000" ><span class="actTime">19:15 - 20:30</span><span class="actNm">Champagne Drip</span></div><div class="act id-jantse-1 " data-id="jantse-1" data-start-time="1687566600000" data-end-time="1687570200000" ><span class="actTime">20:30 - 21:30</span><span class="actNm">Jantsen</span></div><div class="act id-ruskob-1 " data-id="ruskob-1" data-start-time="1687570200000" data-end-time="1687573800000" ><span class="actTime">21:30 - 22:30</span><span class="actNm">Rusko b2b Dirt Monkey</span></div><div class="act id-virtua-1 " data-id="virtua-1" data-start-time="1687573800000" data-end-time="1687578300000" ><span class="actTime">22:30 - 23:45</span><span class="actNm">Virtual Riot</span></div><div class="act id-peekab-1 " data-id="peekab-1" data-start-time="1687578300000" data-end-time="1687581900000" ><span class="actTime">23:45 - 00:45</span><span class="actNm">Peekaboo</span></div><div class="act id-diesel-1 " data-id="diesel-1" data-start-time="1687581900000" data-end-time="1687586400000" ><span class="actTime">00:45 - 02:00</span><span class="actNm">Diesel</span></div><div class="act id-ganjaw1-1 " data-id="ganjaw1-1" data-start-time="1687586400000" data-end-time="1687590900000" data-mbid="014abfeb-cdfe-46dc-90fb-e192473ce252" ><span class="actTime">02:00 - 03:15</span><span class="actNm">Ganja White Night</span></div></div>
</div></div><div class="day" data-date="1687579200" data-first-start="32400" data-last-stop="104400"><h2 class="dayName">Sat&#8203;urday 24th June</h2>
<div class="stage"><h3 class="stageName">Carousel Club</h3>
<div class="actLists"><div class="act id-tba-2 " data-id="tba-2" data-start-time="1687644000000" data-end-time="1687647600000" data-mbid="6ee649c3-b301-474a-a98f-527ef2cf064a" ><span class="actTime">18:00 - 19:00</span><span class="actNm">TBA</span></div><div class="act id-yunpin-1 " data-id="yunpin-1" data-start-time="1687649400000" data-end-time="1687653900000" data-mbid="b4075123-ef13-4fc0-ac15-7bc7c1d761f0" ><span class="actTime">19:30 - 20:45</span><span class="actNm">yunè pinku</span></div><div class="act id-mobley-1 " data-id="mobley-1" data-start-time="1687655700000" data-end-time="1687659300000" ><span class="actTime">21:15 - 22:15</span><span class="actNm">Mobley</span></div><div class="act id-elohim-1 " data-id="elohim-1" data-start-time="1687662000000" data-end-time="1687665600000" data-mbid="1734fde8-6396-409e-97b0-d14c5fc614fb" ><span class="actTime">23:00 - 00:00</span><span class="actNm">Elohim</span></div><div class="act id-twofee-1 " data-id="twofee-1" data-start-time="1687667400000" data-end-time="1687671000000" data-mbid="07d0e0b3-dea4-4892-bee7-eaad19d093ec" ><span class="actTime">00:30 - 01:30</span><span class="actNm">Two Feet</span></div><div class="act id-chrome1-1 " data-id="chrome1-1" data-start-time="1687672800000" data-end-time="1687677300000" ><span class="actTime">02:00 - 03:15</span><span class="actNm">Chromeo DJ Set</span></div></div>
</div><div class="stage"><h3 class="stageName">Honeycomb</h3>
<div class="actLists"><div class="act id-humani-1 " data-id="humani-1" data-start-time="1687629600000" data-end-time="1687633200000" ><span class="actTime">14:00 - 15:00</span><span class="actNm">Humanity Circle</span></div><div class="act id-plugin-1 " data-id="plugin-1" data-start-time="1687635000000" data-end-time="1687638600000" ><span class="actTime">15:30 - 16:30</span><span class="actNm">Plug In Performer Showcase</span></div><div class="act id-datura-1 " data-id="datura-1" data-start-time="1687640400000" data-end-time="1687644000000" ><span class="actTime">17:00 - 18:00</span><span class="actNm">Datura</span></div><div class="act id-rumble-2 " data-id="rumble-2" data-start-time="1687645800000" data-end-time="1687651200000" ><span class="actTime">18:30 - 20:00</span><span class="actNm">Rumble in the Bumble</span></div><div class="act id-therap-2 " data-id="therap-2" data-start-time="1687652100000" data-end-time="1687655700000" ><span class="actTime">20:15 - 21:15</span><span class="actNm">Therapy Gecko</span></div><div class="act id-robbie-2 " data-id="robbie-2" data-start-time="1687657500000" data-end-time="1687660200000" ><span class="actTime">21:45 - 22:30</span><span class="actNm">Robbie Fitzsimmons</span></div><div class="act id-daveya-2 " data-id="daveya-2" data-start-time="1687662000000" data-end-time="1687665600000" ><span class="actTime">23:00 - 00:00</span><span class="actNm">Dave Yaden + Danny Asadi</span></div><div class="act id-djbrow-2 " data-id="djbrow-2" data-start-time="1687667400000" data-end-time="1687671000000" ><span class="actTime">00:30 - 01:30</span><span class="actNm">DJ Brownie</span></div><div class="act id-djmarb-1 " data-id="djmarb-1" data-start-time="1687672800000" data-end-time="1687676400000" ><span class="actTime">02:00 - 03:00</span><span class="actNm">DJ Marb Menthols</span></div></div>
</div><div class="stage"><h3 class="stageName">Ranch Arena</h3>
<div class="actLists"><div class="act id-jellyb-1 " data-id="jellyb-1" data-start-time="1687636800000" data-end-time="1687640400000" ><span class="actTime">16:00 - 17:00</span><span class="actNm">Jellybean Benitez</span></div><div class="act id-chrome-1 " data-id="chrome-1" data-start-time="1687642200000" data-end-time="1687646700000" data-mbid="647221d0-f6b1-4e03-924c-c59b8059536f" ><span class="actTime">17:30 - 18:45</span><span class="actNm">Chromeo</span></div><div class="act id-string1-2 " data-id="string1-2" data-start-time="1687649400000" data-end-time="1687663800000" data-mbid="cff95140-6d57-498a-8834-10eb72865b29" ><span class="actTime">19:30 - 23:30</span><span class="actNm">The String Cheese Incident</span></div><div class="act id-zedsde-1 " data-id="zedsde-1" data-start-time="1687666500000" data-end-time="1687671900000" data-mbid="f9fdca15-1bef-43a0-8213-758b6ee0aa91" ><span class="actTime">00:15 - 01:45</span><span class="actNm">Zeds Dead</span></div></div>
</div><div class="stage"><h3 class="stageName">Sherwood Court</h3>
<div class="actLists"><div class="act id-spacew-1 " data-id="spacew-1" data-start-time="1687641300000" data-end-time="1687645800000" ><span class="actTime">17:15 - 18:30</span><span class="actNm">Space Wizard</span></div><div class="act id-isoxo-1 " data-id="isoxo-1" data-start-time="1687648500000" data-end-time="1687652100000" ><span class="actTime">19:15 - 20:15</span><span class="actNm">ISOxo</span></div><div class="act id-kaiwac-1 " data-id="kaiwac-1" data-start-time="1687656600000" data-end-time="1687660200000" ><span class="actTime">21:30 - 22:30</span><span class="actNm">Kai Wachi</span></div><div class="act id-svdden-1 " data-id="svdden-1" data-start-time="1687662900000" data-end-time="1687667400000" ><span class="actTime">23:15 - 00:30</span><span class="actNm">SVDDEN DEATH Presents: Voyd</span></div><div class="act id-sts9-1 " data-id="sts9-1" data-start-time="1687671900000" data-end-time="1687676400000" ><span class="actTime">01:45 - 03:00</span><span class="actNm">STS9</span></div></div>
</div><div class="stage"><h3 class="stageName">Silent Disco (Blue Channel)</h3>
<div class="actLists"><div class="act id-joshbr-1 " data-id="joshbr-1" data-start-time="1687647600000" data-end-time="1687654800000" ><span class="actTime">19:00 - 21:00</span><span class="actNm">Josh Brooks</span></div><div class="act id-zenasw-1 " data-id="zenasw-1" data-start-time="1687654800000" data-end-time="1687658400000" ><span class="actTime">21:00 - 22:00</span><span class="actNm">Zenas White</span></div><div class="act id-arvima-1 " data-id="arvima-1" data-start-time="1687658400000" data-end-time="1687662000000" ><span class="actTime">22:00 - 23:00</span><span class="actNm">Arvi Mala</span></div><div class="act id-crybb-1 " data-id="crybb-1" data-start-time="1687662000000" data-end-time="1687665600000" ><span class="actTime">23:00 - 00:00</span><span class="actNm">CRYBB</span></div><div class="act id-alexki-1 " data-id="alexki-1" data-start-time="1687665600000" data-end-time="1687669200000" ><span class="actTime">00:00 - 01:00</span><span class="actNm">Alex Kislov</span></div><div class="act id-djcros-1 " data-id="djcros-1" data-start-time="1687669200000" data-end-time="1687672800000" ><span class="actTime">01:00 - 02:00</span><span class="actNm">DJ Cross</span></div><div class="act id-goodse-1 " data-id="goodse-1" data-start-time="1687672800000" data-end-time="1687676400000" ><span class="actTime">02:00 - 03:00</span><span class="actNm">Goodsex</span></div></div>
</div><div class="stage"><h3 class="stageName">Silent Disco (Green Channel)</h3>
<div class="actLists"><div class="act id-motion-2 " data-id="motion-2" data-start-time="1687647600000" data-end-time="1687655700000" ><span class="actTime">19:00 - 21:15</span><span class="actNm">Motion Potion</span></div><div class="act id-meking-2 " data-id="meking-2" data-start-time="1687655700000" data-end-time="1687659300000" ><span class="actTime">21:15 - 22:15</span><span class="actNm">Mekington</span></div><div class="act id-ayoo-2 " data-id="ayoo-2" data-start-time="1687659300000" data-end-time="1687662900000" ><span class="actTime">22:15 - 23:15</span><span class="actNm">Ayoo</span></div><div class="act id-pumath-3 " data-id="pumath-3" data-start-time="1687662900000" data-end-time="1687666500000" ><span class="actTime">23:15 - 00:15</span><span class="actNm">Puma Thurman</span></div><div class="act id-gaff-1 " data-id="gaff-1" data-start-time="1687666500000" data-end-time="1687671000000" ><span class="actTime">00:15 - 01:30</span><span class="actNm">THE GAFF</span></div><div class="act id-keithm-1 " data-id="keithm-1" data-start-time="1687671000000" data-end-time="1687676400000" ><span class="actTime">01:30 - 03:00</span><span class="actNm">Keith MacKenzie</span></div></div>
</div><div class="stage"><h3 class="stageName">The Brainery</h3>
<div class="actLists"><div class="act id-rhythm-1 " data-id="rhythm-1" data-start-time="1687612500000" data-end-time="1687616100000" ><span class="actTime">09:15 - 10:15</span><span class="actNm">Rhythmetrix 360 Soundbath Experience</span></div><div class="act id-somati-1 " data-id="somati-1" data-start-time="1687617000000" data-end-time="1687619700000" ><span class="actTime">10:30 - 11:15</span><span class="actNm">Somatic Therapy for Neck and Shoulders</span></div><div class="act id-guided-1 " data-id="guided-1" data-start-time="1687620600000" data-end-time="1687622400000" ><span class="actTime">11:30 - 12:00</span><span class="actNm">Guided Meditation & Breathwork to Energize & Connect</span></div><div class="act id-accept-1 " data-id="accept-1" data-start-time="1687623300000" data-end-time="1687626000000" ><span class="actTime">12:15 - 13:00</span><span class="actNm">Accepting Neurodiversity</span></div><div class="act id-herfor1-1 " data-id="herfor1-1" data-start-time="1687629600000" data-end-time="1687633200000" ><span class="actTime">14:00 - 15:00</span><span class="actNm">Her Forest Panel</span></div><div class="act id-braine-3 " data-id="braine-3" data-start-time="1687634100000" data-end-time="1687637700000" ><span class="actTime">15:15 - 16:15</span><span class="actNm">The Brainery Panel</span></div><div class="act id-braine-4 " data-id="braine-4" data-start-time="1687638000000" data-end-time="1687641600000" ><span class="actTime">16:20 - 17:20</span><span class="actNm">The Brainery Panel</span></div><div class="act id-sethwa-3 " data-id="sethwa-3" data-start-time="1687676400000" data-end-time="1687683600000" ><span class="actTime">03:00 - 05:00</span><span class="actNm">Sethward's Show & Tell Spectacular</span></div></div>
</div><div class="stage"><h3 class="stageName">The Observatory</h3>
<div class="actLists"><div class="act id-kainal-1 " data-id="kainal-1" data-start-time="1687635000000" data-end-time="1687638600000" ><span class="actTime">15:30 - 16:30</span><span class="actNm">Kainalu</span></div><div class="act id-veryni-1 " data-id="veryni-1" data-start-time="1687641300000" data-end-time="1687644000000" ><span class="actTime">17:15 - 18:00</span><span class="actNm">Very Nice Person</span></div><div class="act id-djbrow-1 " data-id="djbrow-1" data-start-time="1687645800000" data-end-time="1687649400000" ><span class="actTime">18:30 - 19:30</span><span class="actNm">DJ Brownie</span></div><div class="act id-ford-1 " data-id="ford-1" data-start-time="1687650300000" data-end-time="1687653900000" ><span class="actTime">19:45 - 20:45</span><span class="actNm">Ford.</span></div><div class="act id-phanto-1 " data-id="phanto-1" data-start-time="1687654800000" data-end-time="1687658400000" data-mbid="ba8140f6-8074-4c85-b57d-26d11677866f" ><span class="actTime">21:00 - 22:00</span><span class="actNm">Phantoms</span></div><div class="act id-kasbo-1 " data-id="kasbo-1" data-start-time="1687659300000" data-end-time="1687662900000" ><span class="actTime">22:15 - 23:15</span><span class="actNm">Kasbo</span></div><div class="act id-devaul-1 " data-id="devaul-1" data-start-time="1687663800000" data-end-time="1687667400000" ><span class="actTime">23:30 - 00:30</span><span class="actNm">Devault</span></div><div class="act id-memba-1 " data-id="memba-1" data-start-time="1687668300000" data-end-time="1687672800000" ><span class="actTime">00:45 - 02:00</span><span class="actNm">Memba</span></div><div class="act id-golden1-1 " data-id="golden1-1" data-start-time="1687672800000" data-end-time="1687677300000" data-mbid="64bdfb5e-cbf4-4b4d-b939-1086fb4673f2" ><span class="actTime">02:00 - 03:15</span><span class="actNm">Golden Features</span></div></div>
</div><div class="stage"><h3 class="stageName">Tripolee</h3>
<div class="actLists"><div class="act id-yoga-2 " data-id="yoga-2" data-start-time="1687622400000" data-end-time="1687626900000" data-mbid="409b911e-1496-4238-a63a-25bcefe0f872" ><span class="actTime">12:00 - 13:15</span><span class="actNm">YOGA</span></div><div class="act id-tba-1 " data-id="tba-1" data-start-time="1687636800000" data-end-time="1687640400000" data-mbid="6ee649c3-b301-474a-a98f-527ef2cf064a" ><span class="actTime">16:00 - 17:00</span><span class="actNm">TBA</span></div><div class="act id-raecol-1 " data-id="raecol-1" data-start-time="1687640400000" data-end-time="1687644900000" ><span class="actTime">17:00 - 18:15</span><span class="actNm">Rae Cola</span></div><div class="act id-djtopg-1 " data-id="djtopg-1" data-start-time="1687644900000" data-end-time="1687649400000" ><span class="actTime">18:15 - 19:30</span><span class="actNm">DJ Topgun</span></div><div class="act id-sanpac-1 " data-id="sanpac-1" data-start-time="1687649400000" data-end-time="1687653000000" ><span class="actTime">19:30 - 20:30</span><span class="actNm">San Pacho</span></div><div class="act id-drfres-1 " data-id="drfres-1" data-start-time="1687653000000" data-end-time="1687657500000" ><span class="actTime">20:30 - 21:45</span><span class="actNm">Dr. Fresch</span></div><div class="act id-noizu-1 " data-id="noizu-1" data-start-time="1687657500000" data-end-time="1687662000000" ><span class="actTime">21:45 - 23:00</span><span class="actNm">Noizu</span></div><div class="act id-bobmos-1 " data-id="bobmos-1" data-start-time="1687662000000" data-end-time="1687667400000" ><span class="actTime">23:00 - 00:30</span><span class="actNm">Bob Moses Club Set</span></div><div class="act id-chrisl-1 " data-id="chrisl-1" data-start-time="1687667400000" data-end-time="1687672800000" data-mbid="f491ebd7-5e18-4961-aaaf-e6210f387f1f" ><span class="actTime">00:30 - 02:00</span><span class="actNm">Chris Lorenzo</span></div><div class="act id-chrisl1-1 " data-id="chrisl1-1" data-start-time="1687672800000" data-end-time="1687677300000" data-mbid="fca94d64-9ada-4264-9373-4158e2f7c7e7" ><span class="actTime">02:00 - 03:15</span><span class="actNm">Chris Lake</span></div></div>
</div></div><div class="day" data-date="1687665600" data-first-start="34200" data-last-stop="93600"><h2 class="dayName">Sun&#8203;day 25th June</h2>
<div class="stage"><h3 class="stageName">Carousel Club</h3>
<div class="actLists"><div class="act id-exclus-1 " data-id="exclus-1" data-start-time="1687712400000" data-end-time="1687717800000" ><span class="actTime">13:00 - 14:30</span><span class="actNm">EXCLUSIVE 6 IN THE FOREST CELEBRATION</span></div><div class="act id-snakes-1 " data-id="snakes-1" data-start-time="1687730400000" data-end-time="1687734900000" ><span class="actTime">18:00 - 19:15</span><span class="actNm">Snakes & Stars</span></div><div class="act id-fliptu-1 " data-id="fliptu-1" data-start-time="1687736700000" data-end-time="1687741200000" ><span class="actTime">19:45 - 21:00</span><span class="actNm">flipturn</span></div><div class="act id-tba-3 " data-id="tba-3" data-start-time="1687743000000" data-end-time="1687746600000" data-mbid="6ee649c3-b301-474a-a98f-527ef2cf064a" ><span class="actTime">21:30 - 22:30</span><span class="actNm">TBA</span></div><div class="act id-thumpa-1 " data-id="thumpa-1" data-start-time="1687748400000" data-end-time="1687752000000" ><span class="actTime">23:00 - 00:00</span><span class="actNm">Thumpasaurus</span></div><div class="act id-jellyb-2 " data-id="jellyb-2" data-start-time="1687753800000" data-end-time="1687759200000" ><span class="actTime">00:30 - 02:00</span><span class="actNm">Jellybean Benitez</span></div></div>
</div><div class="stage"><h3 class="stageName">Honeycomb</h3>
<div class="actLists"><div class="act id-pridep-1 " data-id="pridep-1" data-start-time="1687723200000" data-end-time="1687728600000" ><span class="actTime">16:00 - 17:30</span><span class="actNm">PRIDE PARTY</span></div><div class="act id-datura-2 " data-id="datura-2" data-start-time="1687730400000" data-end-time="1687733100000" ><span class="actTime">18:00 - 18:45</span><span class="actNm">Datura</span></div><div class="act id-daveya-3 " data-id="daveya-3" data-start-time="1687734900000" data-end-time="1687738500000" ><span class="actTime">19:15 - 20:15</span><span class="actNm">Dave Yaden + Danny Asadi</span></div><div class="act id-couped-1 " data-id="couped-1" data-start-time="1687740300000" data-end-time="1687743000000" ><span class="actTime">20:45 - 21:30</span><span class="actNm">COUPE DVLLE</span></div><div class="act id-brandi-1 " data-id="brandi-1" data-start-time="1687744800000" data-end-time="1687749300000" ><span class="actTime">22:00 - 23:15</span><span class="actNm">Brandi Cyrus</span></div><div class="act id-robbie-3 " data-id="robbie-3" data-start-time="1687750200000" data-end-time="1687753800000" ><span class="actTime">23:30 - 00:30</span><span class="actNm">Robbie Fitzsimmons</span></div></div>
</div><div class="stage"><h3 class="stageName">Ranch Arena</h3>
<div class="actLists"><div class="act id-dogsin-1 " data-id="dogsin-1" data-start-time="1687728600000" data-end-time="1687733100000" data-mbid="a05236ee-3fac-45d7-96f5-b2cd6d03fda9" ><span class="actTime">17:30 - 18:45</span><span class="actNm">Dogs in a Pile</span></div><div class="act id-opiuo-1 " data-id="opiuo-1" data-start-time="1687735800000" data-end-time="1687740300000" data-mbid="d768c6d7-cbb6-4089-a0ce-76186d314dd7" ><span class="actTime">19:30 - 20:45</span><span class="actNm">OPIUO</span></div><div class="act id-goose-1 " data-id="goose-1" data-start-time="1687742100000" data-end-time="1687747500000" data-mbid="6849ebec-b385-4b41-b5a1-125f91e46119" ><span class="actTime">21:15 - 22:45</span><span class="actNm">Goose</span></div><div class="act id-aboveb-1 " data-id="aboveb-1" data-start-time="1687750200000" data-end-time="1687755600000" data-mbid="370bd5a3-4abf-4356-8576-3a8fc0c11d65" ><span class="actTime">23:30 - 01:00</span><span class="actNm">Above & Beyond</span></div></div>
</div><div class="stage"><h3 class="stageName">Sherwood Court</h3>
<div class="actLists"><div class="act id-dailyb-1 " data-id="dailyb-1" data-start-time="1687732200000" data-end-time="1687735800000" data-mbid="2d29a448-718d-45fb-a283-3a98d3ca6e1e" ><span class="actTime">18:30 - 19:30</span><span class="actNm">Daily Bread</span></div><div class="act id-apashe-1 " data-id="apashe-1" data-start-time="1687737600000" data-end-time="1687742100000" ><span class="actTime">20:00 - 21:15</span><span class="actNm">Apashe (Live Brass Ensemble!!)</span></div><div class="act id-madeon-1 " data-id="madeon-1" data-start-time="1687745700000" data-end-time="1687750200000" data-mbid="fa1de503-aba7-41fa-a1ed-371b3e87a717" ><span class="actTime">22:15 - 23:30</span><span class="actNm">Madeon</span></div><div class="act id-rezz1-1 " data-id="rezz1-1" data-start-time="1687753800000" data-end-time="1687758300000" data-mbid="2eaf4267-4dd6-412a-9bb0-596afb90215b" ><span class="actTime">00:30 - 01:45</span><span class="actNm">Rezz</span></div></div>
</div><div class="stage"><h3 class="stageName">Silent Disco (Blue Channel)</h3>
<div class="actLists"><div class="act id-samwhi-2 " data-id="samwhi-2" data-start-time="1687734000000" data-end-time="1687737600000" ><span class="actTime">19:00 - 20:00</span><span class="actNm">Sam White</span></div><div class="act id-stack-2 " data-id="stack-2" data-start-time="1687737600000" data-end-time="1687741200000" ><span class="actTime">20:00 - 21:00</span><span class="actNm">Stack</span></div><div class="act id-whiteo-2 " data-id="whiteo-2" data-start-time="1687741200000" data-end-time="1687745700000" ><span class="actTime">21:00 - 22:15</span><span class="actNm">White Owl</span></div><div class="act id-tsunam-2 " data-id="tsunam-2" data-start-time="1687745700000" data-end-time="1687749300000" ><span class="actTime">22:15 - 23:15</span><span class="actNm">Tsunami</span></div><div class="act id-tombz-2 " data-id="tombz-2" data-start-time="1687749300000" data-end-time="1687752900000" ><span class="actTime">23:15 - 00:15</span><span class="actNm">Tombz</span></div><div class="act id-xonic-2 " data-id="xonic-2" data-start-time="1687752900000" data-end-time="1687757400000" ><span class="actTime">00:15 - 01:30</span><span class="actNm">Xonic</span></div></div>
</div><div class="stage"><h3 class="stageName">Silent Disco (Green Channel)</h3>
<div class="actLists"><div class="act id-chayu-2 " data-id="chayu-2" data-start-time="1687734000000" data-end-time="1687738500000" ><span class="actTime">19:00 - 20:15</span><span class="actNm">Chayu</span></div><div class="act id-jugoe-1 " data-id="jugoe-1" data-start-time="1687738500000" data-end-time="1687742100000" ><span class="actTime">20:15 - 21:15</span><span class="actNm">Jugoe</span></div><div class="act id-golden-2 " data-id="golden-2" data-start-time="1687742100000" data-end-time="1687746600000" ><span class="actTime">21:15 - 22:30</span><span class="actNm">Golden Goddess</span></div><div class="act id-pumath-4 " data-id="pumath-4" data-start-time="1687746600000" data-end-time="1687752000000" ><span class="actTime">22:30 - 00:00</span><span class="actNm">Puma Thurman</span></div><div class="act id-motion-3 " data-id="motion-3" data-start-time="1687752000000" data-end-time="1687757400000" ><span class="actTime">00:00 - 01:30</span><span class="actNm">Motion Potion</span></div></div>
</div><div class="stage"><h3 class="stageName">The Brainery</h3>
<div class="actLists"><div class="act id-energy-1 " data-id="energy-1" data-start-time="1687699800000" data-end-time="1687702500000" ><span class="actTime">09:30 - 10:15</span><span class="actNm">Energy Alchemy w/ Ayurveda & Sacred Sound</span></div><div class="act id-progre-1 " data-id="progre-1" data-start-time="1687703400000" data-end-time="1687706100000" ><span class="actTime">10:30 - 11:15</span><span class="actNm">Progressive Muscle Relaxation & Guided Meditation</span></div><div class="act id-herfor2-1 " data-id="herfor2-1" data-start-time="1687707000000" data-end-time="1687709700000" ><span class="actTime">11:30 - 12:15</span><span class="actNm">Her Forest Pres. Menstrual Cycle Literacy</span></div><div class="act id-creati-1 " data-id="creati-1" data-start-time="1687711500000" data-end-time="1687715100000" ><span class="actTime">12:45 - 13:45</span><span class="actNm">Creating Collage</span></div><div class="act id-sweets-1 " data-id="sweets-1" data-start-time="1687716000000" data-end-time="1687719600000" ><span class="actTime">14:00 - 15:00</span><span class="actNm">Sweets Kendama Jam</span></div><div class="act id-braine-5 " data-id="braine-5" data-start-time="1687720500000" data-end-time="1687724100000" ><span class="actTime">15:15 - 16:15</span><span class="actNm">The Brainery Panel</span></div><div class="act id-braine-6 " data-id="braine-6" data-start-time="1687724400000" data-end-time="1687728000000" ><span class="actTime">16:20 - 17:20</span><span class="actNm">The Brainery Panel</span></div></div>
</div><div class="stage"><h3 class="stageName">The Observatory</h3>
<div class="actLists"><div class="act id-chmura-1 " data-id="chmura-1" data-start-time="1687726800000" data-end-time="1687730400000" ><span class="actTime">17:00 - 18:00</span><span class="actNm">Chmura</span></div><div class="act id-rohaan-1 " data-id="rohaan-1" data-start-time="1687731300000" data-end-time="1687734900000" ><span class="actTime">18:15 - 19:15</span><span class="actNm">Rohaan</span></div><div class="act id-saka-1 " data-id="saka-1" data-start-time="1687735800000" data-end-time="1687739400000" ><span class="actTime">19:30 - 20:30</span><span class="actNm">Saka</span></div><div class="act id-freddy-1 " data-id="freddy-1" data-start-time="1687740300000" data-end-time="1687743900000" ><span class="actTime">20:45 - 21:45</span><span class="actNm">Freddy Todd</span></div><div class="act id-rossy-1 " data-id="rossy-1" data-start-time="1687744800000" data-end-time="1687748400000" ><span class="actTime">22:00 - 23:00</span><span class="actNm">Rossy</span></div><div class="act id-eazyba-2 " data-id="eazyba-2" data-start-time="1687749300000" data-end-time="1687752900000" data-mbid="03a772ac-f7cf-4e85-a087-44c6718f52d2" ><span class="actTime">23:15 - 00:15</span><span class="actNm">Eazybaked</span></div><div class="act id-dixons-3 " data-id="dixons-3" data-start-time="1687754700000" data-end-time="1687758300000" data-mbid="2cc0c42d-a27a-43fe-bee4-ea12b8572322" ><span class="actTime">00:45 - 01:45</span><span class="actNm">Dixon's Violin</span></div></div>
</div><div class="stage"><h3 class="stageName">Tripolee</h3>
<div class="actLists"><div class="act id-yoga-3 " data-id="yoga-3" data-start-time="1687708800000" data-end-time="1687713300000" data-mbid="409b911e-1496-4238-a63a-25bcefe0f872" ><span class="actTime">12:00 - 13:15</span><span class="actNm">YOGA</span></div><div class="act id-discov-2 " data-id="discov-2" data-start-time="1687726800000" data-end-time="1687731300000" ><span class="actTime">17:00 - 18:15</span><span class="actNm">Discovery Project</span></div><div class="act id-daniel1-1 " data-id="daniel1-1" data-start-time="1687731300000" data-end-time="1687735800000" ><span class="actTime">18:15 - 19:30</span><span class="actNm">Daniel Allan</span></div><div class="act id-aluna-1 " data-id="aluna-1" data-start-time="1687735800000" data-end-time="1687740300000" data-mbid="f07b993e-fc7b-4c8f-a5d5-ff42844ac955" ><span class="actTime">19:30 - 20:45</span><span class="actNm">Aluna</span></div><div class="act id-kasabl-1 " data-id="kasabl-1" data-start-time="1687740300000" data-end-time="1687744800000" ><span class="actTime">20:45 - 22:00</span><span class="actNm">Kasablanca</span></div><div class="act id-hayden-1 " data-id="hayden-1" data-start-time="1687744800000" data-end-time="1687748400000" data-mbid="af3d88d4-ba94-44b4-9a78-87976f1acd42" ><span class="actTime">22:00 - 23:00</span><span class="actNm">Hayden James</span></div><div class="act id-dabin-1 " data-id="dabin-1" data-start-time="1687748400000" data-end-time="1687752900000" data-mbid="6d539d7d-454b-44b1-b7de-881a987d4edd" ><span class="actTime">23:00 - 00:15</span><span class="actNm">Dabin</span></div><div class="act id-sanhol-1 " data-id="sanhol-1" data-start-time="1687752900000" data-end-time="1687757400000" data-mbid="23101701-cecf-4c9b-9b4c-d6a249eac118" ><span class="actTime">00:15 - 01:30</span><span class="actNm">San Holo</span></div></div>
</div></div></div>
"""

# https://old.reddit.com/r/ElectricForest/comments/1bqbwlv/electric_forest_2024_lineup_broken_down_by_genre/
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
                   "Pretty Pink",],
         "DANCE": ["Coco & Breezy",
                   "DRAMA",
                   "it's murph",
                   "LP Giobbi",
                   "Michaël Brun",
                   "DJ Susan",
                   "Jason Leech",
                   "Shaun Ross",],
         "TECHNO" :["Charlotte De Witte",
                    "Sara Landry",
                    "Layton Giordani",
                    "Blastoyz",],
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
                 "Boogie T.rio",],
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
                 "Little stranger",],
         "SOUL": ["Dixon's Violin",
                  "Rawayana",
                  "Hiatus Kaiyote",
                  "Polyrhythmics",
                  "Moontricks"]
         }


duoActs = {"Gigantic NGHTMRE" : ["Big Gigantic","NGHTMRE"],
              "EVERYTHING ALWAYS" : ["Dom Dolla","John Summit"],
              "LSZEE": ["CloZee","LSDREAM"],
              "VNSSA B2B Nala" : ["VNSSA","Nala"],
              "Hyperbeam" : ["odd Mob", "Omnom"]}


STAGES = [ "RANCH_ARENA", "SHERWOOD_COURT", "TRIPOLEE", "CAROUSEL_CLUB", "OBSERVATORY", "HONEYCOMB"]


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

def convert_timestamp(ts):
    ts = datetime.fromtimestamp(ts / 1000, TZ)
    return ts

def get_html_data(content):
    fullData = {}
    # Parsing the HTML
    soup = BeautifulSoup(content, 'html.parser')
    day_div = soup.find_all('div', class_='day')
    for day in day_div:
        # Extracting stages and acts
        stages = day.find_all('div', class_='stage')
        for stage in stages:
            stage_name = stage.find('h3', class_='stageName').text.strip()
            acts = stage.find_all('div', class_='act')
            for act in acts:
                artist = act.find('span', class_='actNm').text.strip()
                
                start_time = convert_timestamp(int(act['data-start-time']))
                end_time = convert_timestamp(int(act['data-end-time']))
                act_info = {"stage" : stage_name, "start_time" : start_time, "end_time" : end_time}
                fullData[artist] = act_info
    return fullData

def get_url_content(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def getFullArray(listActs):
    # Spits out the array of acts in alphabetically order
    duo_pop_mult = 1.05  # Since duos are more hype, add a multiplier to their popularity and follower averages
    duo_follower_mult = 1.2
    listActsPop = []
    client_id, client_secret = get_client_credentials()
    for act in listActs:
        act_spot = duoActs.get(act, act)
        if isinstance(act_spot,list):
            continue # We'll get and average the duos later.
        followers, popularity = get_artist_followers_popularity(act_spot, client_id, client_secret)
        listActsPop.append({'name':act, 'followers' : followers, "popularity" : popularity})
    # This logic is to average duos
    for duo in duoActs:
        artists = duoActs[duo]
        if not isinstance(artists,list):
            continue
        followers = 0
        popularity = 0
        for artist in artists:
            fol, pop = get_artist_followers_popularity(artist, client_id, client_secret)
            followers += fol
            popularity += pop
        followers = int((followers / len(artists)) * duo_follower_mult)
        popularity = int((popularity / len(artists)) * duo_pop_mult)
        listActsPop.append({'name':duo, 'followers' : followers, "popularity" : popularity})
    listActsPop = set_pop_follow_manually(listActsPop, "Cuco", 32, 1059)  # Wrong Cuco is the first option.
    return listActsPop

def dates_to_act(act, day_info):
    defaultStart = datetime(2024, 6, 20, 15, 0)
    defaultEnd = datetime(2024, 6, 20, 16, 0)
    for actInDates in day_info:
        if act.lower() == actInDates.lower():
            datInfoAct = day_info[actInDates]
            stageToSearch = datInfoAct["stage"].upper()
            try:
                stage = difflib.get_close_matches(stageToSearch, STAGES)[0]
            except IndexError:
                stage = f"{{{stageToSearch}}}"  # Returns the stage found, around curly brackets if it couldn't be matched in the list
            return stage, datInfoAct["start_time"], datInfoAct["end_time"]
    return "NO_STAGE", defaultStart, defaultEnd
    

def print_md_lst(sorted_listing):
    longestNum = 5
    longestAct = 27
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


def print_array_for_watch(listActs, sorted_listing, day_info):
    artistDateNotFound = []
    print('#include "festival_schedule_face.h"')
    print("")
    print("const schedule_t festival_acts[NUM_ACTS + 1]=")
    print("{")
    for act in listActs:
        stage, start, end = dates_to_act(act, day_info)
        if stage == "STAGE_COUNT":
            artistDateNotFound.append(act)
        actToDisp = unidecode(act)
        actToDisp = strip_word(actToDisp,["The"])
        actToDisp = f"{actToDisp.upper()[:6]: <6}"
        print("    {")
        print(f'        .artist = "{actToDisp}",')
        print(f'        .stage = {stage.upper()},')
        print(f"        .start_time = {{.unit.year = {start.year - 2020}, .unit.month = {start.month}, .unit.day = {start.day}, .unit.hour = {start.hour}, .unit.minute = {start.minute}}},")
        print(f"        .end_time = {{.unit.year = {end.year - 2020}, .unit.month = {end.month}, .unit.day = {end.day}, .unit.hour = {end.hour}, .unit.minute = {end.minute}}},")
        print(f'        .genre = {findGenre(act)},')
        print(f'        .popularity = {get_ranking(sorted_listing, act, "overall")}')
        print("    },")
    print('    [NUM_ACTS]  = { //Fall back')
    print('        .artist = "No Act",')
    print('        .stage = STAGE_COUNT,')
    print('        .start_time = {.unit.year = 0, .unit.month = 0, .unit.day = 0, .unit.hour = 0, .unit.minute = 0},')
    print('        .end_time = {.unit.year = 63, .unit.month = 15, .unit.day = 31, .unit.hour = 31, .unit.minute = 63},')
    print('        .genre = GENRE_COUNT,')
    print('        .popularity = 0')
    print('    }')
    print('};')
    
    if PRINT_SEARCH_RESULTS:
        print("")
        print(f"FAILED TO FIND DATE INFO FOR {artistDateNotFound}")
    


if __name__ == "__main__":
    url = "https://clashfinder.com/m/electricforest23/?user=152rg1.te"
    listActs = []
    for key in dicto:
        for i in dicto[key]:
            listActs.append(i)
    listActs = sorted(listActs, key=lambda x: x.lower().replace("the ",""))

    listActsPop = junNine if USE_TEST_ARR else getFullArray(listActs)

    if SORT_POP_BY_FOLLOWERS:  
        sortKey = lambda x: (x['followers'])
    else:
        sortKey = lambda x: (x['popularity'], x['followers']) # Sort by Spotify popularity w/ followers being the tie-breaker
    sorted_listing = sorted(listActsPop, key=sortKey, reverse=True)
    for i, artist in enumerate(sorted_listing):
        artist['overall'] = i + 1
        
    if PRINT_RANKINGs: 
        print_md_lst(sorted_listing)
        
    if PRINT_ARR:
        html_str = test_content if USE_TEST_ARR else get_url_content(url)
        day_info = get_html_data(html_str)
        print_array_for_watch(listActs, sorted_listing, day_info)