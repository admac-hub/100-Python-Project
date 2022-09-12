from xml.dom.minidom import parse
import xml.dom.minidom
import os

os.chdir('C:\\Users\\a.cuko\\Desktop\\DEV\\100 Projects\\XML parser')
DOMTree = xml.dom.minidom.parse("songs.xml") #Opening the XML document
genre=DOMTree.documentElement
if genre.hasAttribute('catalogue'):
   print(f'Root: {genre.getAttribute("catalogue")}')
Root: Pop
songs=genre.getElementsByTagName('song') #Get all songs in the genre Pop
for song in songs: #Print each song’s details
    print('Song:')
if song.hasAttribute('title'):
    print(f'Title: {song.getAttribute("title")}')
artist=song.getElementsByTagName('artist')[0]
print(f'Artist: {artist.firstChild.data}')
year=song.getElementsByTagName('year')[0]
print(f'Release Year: {year.firstChild.data}')
album=song.getElementsByTagName('album')[0]
print(f'Album: {album.firstChild.data}')