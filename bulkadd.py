from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json

client = Elasticsearch(HOST="https://localhost", PORT=9200)
GLOBAL_INDEX = 'metaphor1'


def read_all_songs():
    with open('corpus/data.json', 'r', encoding='utf-8-sig') as f:
        all_songs = json.loads("[" +
                          f.read().replace("}\n{", "},\n{") +"]")
        # all_songs = json.loads(f.read())
        res_list = [i for n, i in enumerate(all_songs) if i not in all_songs[n + 1:]]
        return res_list

def genData(song_array):
    for song in song_array:
        # Fields-capturing
        # print(song)
        #Name,Lyrics,Composer,Lyricist,Album,Singer,Year,Metaphor,Source Domain,Target Domain,Type of Metaphor,Interpretation
        name = song.get("Name", None)
        lyrics = song.get("Lyrics", None)
        composer = song.get("Composer", None)
        lyricist = song.get("Lyricist", None)
        album = song.get("Album",None)
        singer = song.get("Singer", None)
        year = song.get("Year", None)
        metaphor = song.get("Metaphor",None)
        Source = song.get("Source Domain",None)
        Target = song.get("Target Domain",None)
        type_of_metaphor = song.get("Type of Metaphor", None)
        interpretations = song.get("Interpretation",None)

        yield {
            "_index": "metaphor1",
            "_source": {
                "Name": name,
                "Lyrics": lyrics,
                "Composer": composer,
                "Lyricist": lyricist,
                "Album": album,
                "Singer": singer,
                "Year": year,
                "Metaphor": metaphor,
                "Source": Source,
                "Target": Target,
                "Type of Metaphor":type_of_metaphor,
                "Interpretations":interpretations,
            },
        }

all_songs = read_all_songs()
helpers.bulk(client,genData(all_songs))

