from yandex_music import Client


class YandexMusicApi:
    def __init__(self):
        self.client = Client.from_credentials('only.for.music.api@yandex.com', 'Master2004rus')
        print(self.client.token)

    def get_quest(self, quest):
        if quest.startswith('http'):
            a = quest.split('/')
            track, alb = a[-1], a[-3]
            return self.load_some_track(alb, track)
        else:
            alb, track = self.search(quest)
            print('from get_quest:', alb, track)
            return self.load_some_track(alb, track)

    def load_some_track(self, album_id, track_id):
        self.client.tracks([f'{track_id}:{album_id}'])[0].download(f'songs/{track_id}-{album_id}.mp3')
        return f'songs/{track_id}-{album_id}.mp3'

    def search(self, text):  # returns album_id and track id
        res = self.client.search(text).tracks['results'][0]
        album_id = str(res['albums'][0]['id'])
        track_id = str(res['id'])
        print(album_id, track_id)
        return album_id, track_id


# client = YandexMusicApi()
# song = 'A Different World'
# a, t = [str(i) for i in client.search(song)]
# print(a + ':' + t)
