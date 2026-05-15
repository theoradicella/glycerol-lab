import cv2
import matplotlib.pyplot as plt
from IPython import display
import time
import numpy as np
import scipy.ndimage as ndi
from pathlib import Path

def get_fall_time(trial, ball_size):
    '''
    INPUT: size of the ball in mm
    OUTPUT: no. frames for the fall between markers
    '''
    script_dir = Path(__file__).parent
    relative_path =  fr"..\videos\100ml\trial{trial}\{ball_size}mm.mp4v"
    path = str((script_dir / relative_path).resolve())
    cap = cv2.VideoCapture(path)

    # extract frames from video
    frames = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video reached
        frames.append(frame)
        frame_count += 1

    # transform to grayscale and filter for low intensity
    new_frames = [np.dot(frame[..., :3], [0.114, 0.587, 0.299]) for frame in frames]
    new_frames = [frame < 30 for frame in new_frames] # 30 chosen by looking 

    # find marker locations and crop the frames
    clusters, num_features = ndi.label(new_frames[-1])
    counts = np.bincount(clusters.ravel())
    counts[0] = 0 # disregard the background
    label1, label2 = np.argsort(counts)[-2:][::-1]

    marker1 = clusters==label1
    marker2 = clusters==label2

    y_coords1 = np.unique(np.argwhere(marker1)[:, 0]) # col0 ycoord; col1 x coord
    y_coords2 = np.unique(np.argwhere(marker2)[:, 0])

    new_range = sorted([min(y_coords1), min(y_coords2), max(y_coords1), max(y_coords2)])[1:3]

    cropped_frames = [frame[new_range[0]+1:new_range[1]-1, 160:300] for frame in new_frames] # x axis range chosen by looking 

    # find the times the ball enters and exits the frame
    pixels = []
    for frame in cropped_frames:
        pixels.append(int(frame.sum() > 0))

    pixels = np.pad(pixels, (1, 1), mode='constant') # in case the array starts or ends with a one
    diffs = np.diff(pixels)
    starts = np.where(diffs == 1)[0]
    ends = np.where(diffs == -1)[0]
    lens = ends-starts
    max_idx = np.argmax(lens)
    start = starts[max_idx]
    end = ends[max_idx] # - 1 we add 1 to finish on an empty frame

    return end - start
