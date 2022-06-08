from typing import Tuple, List
import torch
from numpy import asanyarray
import cv2
import numpy as np


def crop_resize(img, x1, x2, y1, y2, oh, ow):
    img = img[x1:x2, y1:y2]
    return cv2.resize(img, (ow, oh))


def flip_event(eventdata):
    m = asanyarray(eventdata)
    eventdata = m[:, ::-1, ...].copy()
    return eventdata


def crop_resize_event(event_data, x1, x2, y1, y2, oh, ow):
    # Only preserve the selected x-y region
    delete_index = np.where(event_data[:, 1] > x2)
    event_data = np.delete(event_data, delete_index, axis=0)
    delete_index = np.where(event_data[:, 1] < x1)
    event_data = np.delete(event_data, delete_index, axis=0)
    delete_index = np.where(event_data[:, 2] > x2)
    event_data = np.delete(event_data, delete_index, axis=0)
    delete_index = np.where(event_data[:, 2] < y1)
    event_data = np.delete(event_data, delete_index, axis=0)

    # resize
    h_rate = oh/(y2-y1)
    w_rate = ow/(x2-x1)
    event_data[:, 1] = event_data[:, 1] * w_rate
    event_data[:, 2] = event_data[:, 2] * h_rate

    return event_data


def sample(ih, iw, oh, ow, lr=0.5, ur=1.5):
    """
    :param ih: input high
    :param iw: input width
    :param oh: output high
    :param ow: output width
    :param lr: low rate
    :param ur: up rate
    :return:
    """
    tr = min(ih / oh, iw / ow)
    lr = min(tr, lr)
    ur = min(tr, ur)
    r = np.random.uniform(lr, ur)
    nh = int(oh * r)
    nw = int(ow * r)
    top = np.random.randint(0, ih - nh)
    left = np.random.randint(0, iw - nw)
    return top, top + nh, left, left + nw


class FrameEventTransform:
    def __init__(self,
                 output_dim: Tuple = None,
                 lr=0.5,
                 ur=1.5,
                 mean=0,
                 sigma=1):

        self.output_dim = output_dim
        self.mean = mean
        self.sigma = sigma
        self.lr = lr
        self.ur = ur

    def __call__(self, aps_frame: List[np.ndarray], eventdata: List[np.ndarray]):

        # crop & resize
        h, w, c = aps_frame[0].shape
        aps_frame = [af.astype(np.float32) for af in aps_frame]
        aps_frame = [cv2.cvtColor(af, cv2.COLOR_BGR2GRAY) for af in aps_frame]
        oh, ow = self.output_dim
        x1, x2, y1, y2 = sample(ih=h, iw=w, oh=oh, ow=ow, lr=self.lr, ur=self.ur)
        aps_frame = [crop_resize(af, x1, x2, y1, y2, oh, ow) for af in aps_frame]
        eventdata = [crop_resize_event(ed, x1, x2, y1, y2, oh, ow) for ed in eventdata]

        # flip, horizontal
        aps_frame = [cv2.flip(af, 1) for af in aps_frame]
        eventdata = [flip_event(ed) for ed in eventdata]

        # normalize to 0-1
        aps_frame = np.array(aps_frame) / 255.0

        # gaussian noise
        noise = np.random.normal(self.mean, self.sigma, aps_frame.shape)
        aps_frame = aps_frame + noise

        # to tensor
        aps_frame = torch.from_numpy(aps_frame).float()
        eventdata = [torch.from_numpy(ed).float() for ed in eventdata]

        return aps_frame, eventdata
