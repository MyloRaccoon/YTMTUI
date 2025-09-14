import subprocess
import mpv
import threading, queue

from back.song import Song, get_song

class Player:
    def __init__(self):
        self.player = mpv.MPV(ytdl=True, vid=False)
        self.queue = queue.Queue()
        self.next_song = None

        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def loop(self):
        while True:
            try:
                cmd, arg = self.queue.get(timeout=0.1)
                if cmd == "play":
                    self.player.play(arg)
                elif cmd == "stop":
                    self.player.stop()
                elif cmd == "pause":
                    self.player.pause = not self.player.pause
                elif cmd == "seek":
                    self.player.seek(arg, reference="absolute")
                elif cmd == "+10":
                    if self.get_position() < self.get_duration() - 11:
                        self.player.seek(self.get_position() + 10, reference="absolute")
                    else:
                        self.player.seek(self.get_duration(), reference="absolute")
                elif cmd == "-10":
                    if self.get_position() > 10:
                        self.player.seek(self.get_position() - 10, reference="absolute")
                    else:
                        self.player.seek(0, reference="absolute")

            except queue.Empty:
                continue

    def get_duration(self) -> int:
        return int(self.player.duration or 0)

    def get_position(self) -> int:
        return int(self.player.time_pos or 0)

    def send(self, cmd, arg=None):
        self.queue.put((cmd, arg))

    def is_finished(self) -> bool:
        return self.player.eof_reached is not False

