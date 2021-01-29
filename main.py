import os
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

apiKey = "AIzaSyBGXMVIWz3d6gHwtHu6yEAEVYTqfjOXK-g"
channels = [
    ("Aqua", "UC1opHUrw8rvnsadT-iGp7Cg"),
    ("Marine", "UCCzUftO8KOVkV4wQG1vkUvg"),
    ("Haachama", "UC1CfXB_kRs3C-zaeTG3oGyg"),
    ("Watame", "UCqm3BQLlJfvkTsX_hvm0UmA"),
    ("Rushia", "UCl_gCybOJRIgOXw6Qb4qJzQ"),
    ("Suisei", "UC5CwaMl1eIgY8h02uZw7u8A"),
    ("Okayu", "UCvaTdHTWBGv3MKj3KVqJVCw"),
    ("Pekora", "UC1DCedRgGHBdm81E1llLhOQ"),
    ("Calliope", "UCL_qhgtOy0dy1Agp8vkySQg")
]

youtube = build('youtube', 'v3', developerKey=apiKey)

someoneStreaming = False
for (key, value) in channels:
    request = youtube.search().list(
        part='snippet',
        channelId=value,
        eventType='live',
        type='video'
    )
    response = request.execute()
    if response['pageInfo']['totalResults'] != 0:
        print(f'{key} is streaming!')
        someoneStreaming = True
    # else:
    #     print(f'{key} isnt streaming :(')
if not someoneStreaming:
    print('Noone is streaming :(')
    
input('\nPress any button to continue..')