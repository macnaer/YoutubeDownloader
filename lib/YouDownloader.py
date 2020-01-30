from subprocess import call
import os

if __name__ == "__main__":
    start


def start():

    exit = False

    while not exit:
        choice = int(
            input("1. Download movie\n2. Download playlist\n0. Exit\n===> "))
        if choice == 1:
            url = input("Enter movie URL ===> ")
            get_movie(url)
        elif choice == 2:
            url = input("Enter playlist URL ===> ")
            print("Download playlist")
        elif choice == 0:
            exit = True
        else:
            print("Use -h --help ")


def get_movie(url):
    movie_info = "youtube-dl " + url + " -F"
    call(movie_info.split(), shell=False)
    hq_fotmat = input("Enter video format: ")
    command = "youtube-dl -f " + hq_fotmat + " " + url + " -c"
    os.chdir("Downloads")
    call(command.split(), shell=False)
