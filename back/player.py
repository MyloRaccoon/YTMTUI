import subprocess

from back.song import Song, get_song

def play(song: Song):
    cmd = f'yt-dlp -o - "{get_song(song.id).url}" | ffplay -nodisp -autoexit -loglevel quiet -'
    subprocess.run(cmd, shell=True)