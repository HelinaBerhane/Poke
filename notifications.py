import requests
import json
from math import *

# def foo( bar ):
#     '''this function foos some bars'''
#     # automatic documentation parsers pick up triple quotes at the start of the function
#
#     return 2 * bar

def getDistance(baseLat, baseLon, Lat, Lon):
    radLat = baseLat * pi / 180
    deltaLat = Lat - baseLat
    deltaLon = Lon - baseLon
    baseDist = 69
    distLat = deltaLat * baseDist
    distLon = deltaLon * cos(radLat) * baseDist
    return sqrt(distLat**2 + distLon**2)

if __name__ == "__main__":

    # source
    source = "http://londonpogomap.com/query2.php"
    payload = {
        "token":"pleaseDontStealOurData",
        "since":"0",
        "mons":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251"}
    headers = {
        "accept":"*/*",
        "accept-encoding":"gzip, deflate, sdch, br",
        "cookie":"__cfduid=db493e874b54016a3cdd37b168690d21d1489148727; _ga=GA1.2.1137458859.1495275444",
        "referer":"http://londonpogomap.com/",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "x-requested-with":"XMLHttpRequest"}

    # get pokemon
    r = requests.get( source, params = payload, headers = headers )
    r.encoding = 'utf-8'
    r_json = r.json()
    poke = r_json["pokemons"]
    names = [
        "Bulbasaur", "Ivysaur", "Venusaur",
        "Charmander", "Charmeleon", "Charizard",
        "Squirtle", "Wartortle", "Blastoise",
        "Caterpie", "Metapod", "Butterfree",
        "Weedle", "Kakuna", "Beedrill",
        "Pidgey", "Pidgeotto", "Pidgeot",
        "Rattata", "Raticate",
        "Spearow", "Fearow",
        "Ekans", "Arbok",
        "Pikachu", "Raichu",
        "Sandshrew", "Sandslash",
        "Nidoran(F)", "Nidorina", "Nidoqueen",
        "Nidoran(M)", "Nidorino", "Nidoking",
        "Clefairy", "Clefable",
        "Vulpix", "Ninetales",
        "Jigglypuff", "Wigglytuff",
        "Zubat", "Golbat",
        "Oddish", "Gloom", "Vileplume",
        "Paras", "Parasect",
        "Venonat", "Venomoth",
        "Diglett", "Dugtrio",
        "Meowth", "Persian",
        "Psyduck", "Golduck",
        "Mankey", "Primeape",
        "Growlithe", "Arcanine",
        "Poliwag", "Poliwhirl", "Poliwrath",
        "Abra", "Kadabra", "Alakazam",
        "Machop", "Machoke", "Machamp",
        "Bellsprout", "Weepinbell", "Victreebel",
        "Tentacool", "Tentacruel",
        "Geodude", "Graveler", "Golem",
        "Ponyta", "Rapidash",
        "Slowpoke", "Slowbro",
        "Magnemite", "Magneton",
        "Farfetch'd",
        "Doduo", "Dodrio",
        "Seel", "Dewgong",
        "Grimer", "Muk",
        "Shellder", "Cloyster",
        "Gastly", "Haunter",
        "Gengar", "Onix",
        "Drowzee", "Hypno",
        "Krabby", "Kingler",
        "Voltorb", "Electrode",
        "Exeggcute", "Exeggutor",
        "Cubone", "Marowak",
        "Hitmonlee", "Hitmonchan",
        "Lickitung",
        "Koffing", "Weezing",
        "Rhyhorn", "Rhydon",
        "Chansey",
        "Tangela",
        "Kangaskhan",
        "Horsea", "Seadra",
        "Goldeen", "Seaking",
        "Staryu", "Starmie",
        "Mr. Mime",
        "Scyther",
        "Jynx",
        "Electabuzz",
        "Magmar",
        "Pinsir",
        "Tauros",
        "Magikarp", "Gyarados",
        "Lapras",
        "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon",
        "Porygon",
        "Omanyte", "Omastar",
        "Kabuto", "Kabutops",
        "Aerodactyl",
        "Snorlax",
        "Articuno", "Zapdos", "Moltres",
        "Dratini", "Dragonair", "Dragonite",
        "Mewtwo", "Mew",
        "Chikorita", "Bayleef", "Meganium",
        "Cyndaquil", "Quilava", "Typhlosion",
        "Totodile", "Croconaw", "Feraligatr",
        "Sentret", "Furret",
        "Hoothoot", "Noctowl",
        "Ledyba", "Ledian",
        "Spinarak", "Ariados",
        "Crobat",
        "Chinchou", "Lanturn",
        "Pichu", "Cleffa", "Igglybuff",
        "Togepi", "Togetic",
        "Natu", "Xatu",
        "Mareep", "Flaaffy", "Ampharos",
        "Bellossom",
        "Marill", "Azumarill",
        "Sudowoodo",
        "Politoed",
        "Hoppip", "Skiploom", "Jumpluff",
        "Aipom",
        "Sunkern", "Sunflora",
        "Yanma",
        "Wooper", "Quagsire",
        "Espeon", "Umbreon",
        "Murkrow",
        "Slowking",
        "Misdreavus",
        "Unown",
        "Wobbuffet",
        "Girafarig",
        "Pineco", "Forretress",
        "Dunsparce", "Gligar",
        "Steelix",
        "Snubbull", "Granbull",
        "Qwilfish",
        "Scizor",
        "Shuckle",
        "Heracross",
        "Sneasel",
        "Teddiursa", "Ursaring",
        "Slugma", "Magcargo",
        "Swinub", "Piloswine",
        "Corsola",
        "Remoraid", "Octillery",
        "Delibird",
        "Mantine",
        "Skarmory",
        "Houndour", "Houndoom",
        "Kingdra", "Phanpy",
        "Donphan",
        "Porygon2",
        "Stantler",
        "Smeargle",
        "Tyrogue", "Hitmontop",
        "Smoochum", "Elekid", "Magby",
        "Miltank",
        "Blissey",
        "Raikou", "Entei", "Suicune",
        "Larvitar", "Pupitar", "Tyranitar",
        "Lugia", "Ho-oh", "Celebi"]
    maxDistance = [
        1.5, 1.9, 2.9, 1.5, 1.9, 2.9, 1.2, 1.1, 1.2, 1.1, 1.0, 0.7, 1.2, 1.2, 1.1, 1.1, 1.0, 0.6, 1.0,
        0.9, 0.9, 0.0, 1.6, 1.2, 1.4, 1.7, 1.3, 1.7, 1.2, 1.1, 1.3, 1.1, 1.1, 1.2, 1.3, 1.6, 1.8, 1.8,
        1.2, 1.6, 1.0, 1.1, 1.0, 1.4, 1.8, 1.1, 0.6, 1.2, 1.1, 1.0, 1.2, 1.2, 1.1, 1.0, 0.6, 1.2, 1.3,
        1.5, 1.9, 1.1, 1.4, 1.9, 1.2, 1.6, 1.9, 1.2, 1.5, 2.0, 0.6, 0.6, 1.1, 1.0, 1.3, 1.3, 1.6, 2.0,
        1.7, 1.7, 1.3, 1.6, 1.7, 2.1, 2.5, 1.2, 1.3, 1.2, 1.3, 1.6, 2.1, 1.2, 1.5, 1.2, 1.2, 1.3, 2.0,
        1.2, 1.2, 1.2, 1.2, 1.4, 1.7, 2.4, 2.9, 1.2, 1.2, 2.1, 2.1, 1.3, 1.3, 1.6, 1.6, 1.6, 6.0, 3.2,
        2.5, 1.2, 1.3, 1.2, 1.2, 1.2, 1.2, 1.2, 1.6, 1.2, 1.4, 1.2, 1.2, 2.5, 1.6, 2.1, 1.6, 1.3, 2.1,
        1.2, 1.2, 1.2, 1.3, 1.2, 1.3, 1.2, 1.3, 1.3, 2.6, 4.0, 4.0, 4.0, 2.7, 3.2, 4.7, 4.0, 4.0, 1.3,
        2.3, 3.3, 1.9, 1.9, 3.3, 1.9, 2.3, 3.3, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.3, 1.6, 1.8, 2.2,
        1.3, 1.3, 1.3, 1.3, 1.6, 1.2, 1.2, 2.7, 3.7, 4.2, 2.5, 1.2, 1.3, 1.2, 2.8, 1.2, 1.2, 1.3, 1.2,
        1.6, 2.1, 1.3, 1.2, 1.2, 3.0, 2.8, 1.2, 2.5, 1.2, 5.0, 1.2, 1.6, 1.6, 2.8, 1.3, 1.2, 2.9, 1.2,
        1.6, 1.2, 2.5, 1.6, 2.9, 1.2, 1.5, 1.8, 1.3, 1.6, 1.8, 2.2, 2.5, 1.2, 1.3, 2.5, 1.2, 1.2, 1.6,
        1.2, 2.5, 1.6, 2.5, 2.4, 1.2, 2.1, 2.1, 1.3, 1.2, 1.2, 1.2, 1.2, 6.5, 4.0, 4.0, 4.0, 2.3, 3.3,
        3.8, 4.0, 4.0, 3.5]

    # filter pokemon
    baseLat = 51.461439
    baseLong = -0.125234
    for i in poke:
        distance = getDistance(baseLat, baseLong, float(i["lat"]), float(i["lng"]))
        if distance < maxDistance[int(i["pokemon_id"])-1]:
            print("ID: " + str(i["pokemon_id"]) + " - Name: " + names[int(i["pokemon_id"])-1] + " - Distance: " + str(distance))
