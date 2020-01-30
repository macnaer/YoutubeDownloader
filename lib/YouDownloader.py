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
            get_playlist(url)
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


def get_playlist(url):
    print("format code  extension  resolution note"
          "\n249   webm  audio only tiny   53k, opus @ 50k(48000Hz)"
          "\n250   webm  audio only tiny   75k, opus @ 70k(48000Hz)"
          "\n140   m4a   audio only tiny  130k, m4a_dash container, mp4a.40.2@128k(44100Hz)"
          "\n251   webm  audio only tiny  140k, opus @160k(48000Hz)"
          "\n278   webm  256x144    144p   97k, webm container, vp9, 30fps, video only"
          "\n160   mp4   256x144    144p  124k, avc1.4d400c, 30fps, video only"
          "\n242   webm  426x240    240p  192k, vp9, 30fps, video only"
          "\n133   mp4   426x240    240p  265k, avc1.4d4015, 30fps, video only"
          "\n243   webm  640x360    360p  365k, vp9, 30fps, video only"
          "\n134   mp4   640x360    360p  603k, avc1.4d401e, 30fps, video only"
          "\n244   webm  854x480    480p  661k, vp9, 30fps, video only"
          "\n135   mp4   854x480    480p 1125k, avc1.4d401f, 30fps, video only"
          "\n247   webm  1280x720   720p 1167k, vp9, 30fps, video only"
          "\n136   mp4   1280x720   720p 2246k, avc1.4d401f, 30fps, video only"
          "\n248   webm  1920x1080  1080p 2301k, vp9, 30fps, video only"
          "\n137   mp4   1920x1080  1080p 4941k, avc1.640028, 30fps, video only"
          "\n43    webm  640x360    360p, vp8.0, vorbis@128k"
          "\n18    mp4   640x360    360p  345k, avc1.42001E, mp4a.40.2@ 96k(44100Hz)"
          "\n22    mp4   1280x720   720p  736k, avc1.64001F, mp4a.40.2@192k(44100Hz)(best)")
    hq_fotmat = input("Enter video format: ")
    command = "youtube-dl -f " + hq_fotmat + " " + url + " -c"
    os.chdir("Downloads")
    call(command.split(), shell=False)
