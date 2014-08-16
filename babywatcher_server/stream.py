import subprocess
import time
import config

class Stream(object):

    stream_process = None

    @staticmethod
    def startStream():
        # Stream with vlc
        Stream.stream_process = subprocess.Popen(['cvlc','v4l2:///dev/video0',
                                                ':sout=#transcode{vcodec=h264,vb=56,fps=5,scale=Auto,width=176,height=144,acodec=none}:rtp{sdp=rtsp://:8554/}',
                                                ':sout-keep'])

    @staticmethod
    def stopStream():
        Stream.stream_process.kill()
        Stream.stream_process = None

    @staticmethod
    def getStream():
        if not Stream.stream_process:
            Stream.startStream()
            time.sleep(3)
        stream_url = "rtsp://{0}:8554/".format(config.get_ip_address('wlan0'))
        return stream_url

