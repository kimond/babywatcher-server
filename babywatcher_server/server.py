
# server constant
from flask import Flask, render_template, Response

from babywatcher_server.camera import OpenCvCamera

HOST = '0.0.0.0'
PORT = 5050


app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('template/index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(OpenCvCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host=HOST, threaded=True)
