
# todays assignment A12
# Extract all bird species from website- https://xeno-canto.org
#  and generate the csv file or the JSON file format for the bird species, family and more

# Endpoint for this server is https://xeno-canto.org/api/2/recordings
# Extract all bird songs from this website use this API TO get data

# Extract all bird species 
from bs4 import BeautifulSoup
import requests
import json


# scrapping function

def webscraping(url):
    response = requests.get(url)
    if (response.status_code==200):
    #youre checking if your request was accepted
    # the content of the webpage is in Bytes so Beautiful soup converts it into HTML code
        soup = BeautifulSoup(response.content,"html.parser")
    # fetch links as list of tag elements
        birdtable= soup.find('table',attrs={'class': 'results'})
        species_list= []

        if birdtable:
            rows=birdtable.find_all('tr')
            for row in rows:
                columns= row.find_all('td')
                for column in columns:
                    birdlink= column.find('a')
                    if birdlink:
                        birdspecies= birdlink.text.strip()
                        # strip function removes all the white spaces
                        species_list.append(birdspecies)
        return species_list

    else:
        print(f"Your request was rejected with statuscode: {response.status_code}")
        return []
    

def songs_webscraping(api_url):
    response= requests.get(api_url)

    if response.status_code==200:
        data= response.json()
        song_list= []
        birdsongs=[]

        if 'recordings' in data:
            for recording in data['recordings']:
                song_list.append(recording['en'])
            return song_list
        else:
            print(f"Your request was rejected to the url {api_url} with statuscode: {response.status_code}")
            return []
    
if __name__=="__main__":
 # Species
    url = 'https://xeno-canto.org/collection/species/all'
    species= webscraping(url)
    

    # Changing the species_list to dict
    species_dict= {"BirdSpecies" : species}


    # Creating a JSON file for bird species
    with open("birdspecies.json","w") as json_file:
        json.dump(species_dict,json_file)
        print("Species have successfully been obtained")

# songs
    url2 = 'https://xeno-canto.org/api/2/recordings?query=type:song'
    songs= songs_webscraping(url2)

 # Changing the songs to dict
    songs_dict= {"BirdSongs" : songs}

    # Creating a JSON file
    with open("birdsongs.json","w") as json_file1:
        json.dump(songs_dict,json_file1)
        print("Songs have successfully been obtained")   





