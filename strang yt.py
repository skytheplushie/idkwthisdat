import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user
            elif login == user.nickname and password != user.password:
                print('its not right password!')
            else:
                print('this user doesnt exist!')

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f'user {nickname} already exist')
                return
        new_user = User(nickname, password, age)
        self.current_user = new_user
        self.users.append(new_user)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, seek_part):
        result = []
        for video in self.videos:
            if seek_part.upper() in video.title.upper():
                result.append(video.title)
            return result

    def watch_videos(self, movie):
        if not self.current_user:
            print('log in your account please!')
            return
        for selected_video in self.videos:
            if selected_video.title == movie:
                if selected_video.adult_mode and self.current_user.age < 18:
                    print('this video is for adults only! please leave the page!')
                    return
                for i in range(selected_video.duration):
                    print(f'{i + 1}', end=' ')
                    time.sleep(1)
                    selected_video.time_now += 1

                selected_video.time_now = 0
                print('video ended')
                time.sleep(3)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_videos('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_videos('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_videos('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_videos('Лучший язык программирования 2024 года!')
