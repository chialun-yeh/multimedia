import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import datetime

def force_aspectratio(ax, aspect=1):
  image = ax.get_images()
  extent =  image[0].get_extent()
  ax.set_aspect(abs((extent[1] - extent[0]) / (
      extent[3] - extent[2])) / aspect)


class VideoReader(object):

  def __init__(self):
    self._clear()

  def _clear(self):
    self.video_file_path = None
    self.capture = None
    self.width = 0
    self.height = 0
    self.number_of_frames = 0
    self.frame_rate = 0.0
    self.current_frame_index = 0

  def is_opened(self):
    return self.video_file_path is not None and (
        self.capture is not None and self.capture.isOpened())

  def get_width(self):
    return self.width

  def get_height(self):
    return self.height

  def get_number_of_frames(self):
    return self.number_of_frames

  def get_frame_rate(self):
    return self.frame_rate

  def get_current_frame_index(self):
    return self.current_frame_index

  def open(self, video_file_path):
    self.video_file_path = video_file_path
    if not os.path.isfile(self.video_file_path):
      self._clear()
      raise IOError('cannot open video: <%s> is not a valid file' % video_file_path)

    self.capture = cv2.VideoCapture(self.video_file_path)
    if not self.is_opened():
      self._clear()
      raise IOError('cannot open video: <%s> is not a valid video file' % video_file_path)

    # Read video properites.

    # Temporary fix
    # If running on Colab with a newer opencv version (3.x) - use names of the new version
    if cv2.__version__[0] == '3':
      self.width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
      self.height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
      self.number_of_frames = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
      self.frame_rate = np.float32(self.capture.get(cv2.CAP_PROP_FPS))

    # Otherwise default to nomenclature used by opencv 2.x
    else:
      self.width = int(self.capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
      self.height = int(self.capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
      self.number_of_frames = int(self.capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
      self.frame_rate = np.float32(self.capture.get(cv2.cv.CV_CAP_PROP_FPS))


  def get_frames(self):
    """
    Returns a video frame iterator.
    """
    while self.capture is not None:
      bln_frame_retrieved, frame = self.capture.read()
      if not bln_frame_retrieved:
        # Frame stream ended.
        raise StopIteration
      yield frame
      self.current_frame_index += 1

#cap = cv2.VideoCapture('data/ACCEDE00000.mp4')
video_reader = VideoReader()
video_reader.open('data/ACCEDE00000.mp4')
video_duration = float(video_reader.get_number_of_frames()) / float(video_reader.get_frame_rate())

print ('resolution: %d x %d' % (video_reader.get_width(), video_reader.get_height()))
print ('number of frames: %d' % video_reader.get_number_of_frames())
print ('duration: %s' % datetime.timedelta(seconds=video_duration))

# take first frame of the video
ret,frame = cap.read()
