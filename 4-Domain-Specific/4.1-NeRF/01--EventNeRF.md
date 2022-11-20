# EventNeRF: Neural Radiance Fields from a Single Colour Event Camera

Arxiv 2022

## Research Question:
	We demonstrate that it is possible to learn NeRF suitable for novel-view synthesis in the RGB space from asynchronous event streams. 


## Motivation:
(1)	Event camera instead of an RGB camera have several merits, including its ability to handle strong motion blur that exist in RGB images and could cause several RGB-based computer vision methods to fail. 
(2)	Event cameras do not suffer from motion blur and have already brought valuable contributions in the important and long-standing problems of hand and body tracking in this regard.

## Contributions:
(1) EventNeRF: The first approach for inferring NeRF from a monocular colour event stream that enable novel view synthesis in the RGB space at a test time.
(2) A ray smpling strategy that allows for data-efficient training and that is tailored to events.
