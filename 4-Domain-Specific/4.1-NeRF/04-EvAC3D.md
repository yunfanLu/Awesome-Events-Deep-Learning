# EvAC3D: From Event-based Apparent Contours to 3D Models via Continuous Visual Hulls

ECCV 2022

## Research Question:
    3D reconstruction is feasible using events lies in the information contained in the occluding contours and in the continuous scene acquisition with events.
    
## Highlights:
(1) Instead of posed images of the original NeRF, the input to Ev-NeRF is the event measurements accompanied by the movements of the sensors.

(2) Ev-NeRF properly handles the complex noise in event cameras withhout ground truth supervision, and at the same time, enjoys the technical advantages of the sensor over conventional cameras.

(3) The generated neural volume can also produce intensity images from novel views with reasonable depth estimates.
	
## Contributions:
(1) Ev-NeRF: Combination of the popular NeRF formulation with the raw event output of a neuromorphic camera for the first time (claimed)

(2) Ev-NeRF is higly robust to event noise and provide high-quality obervations.

(3) Intensity image reconstruction: novel-view image synthesis, 3D reconstruction and HDR imaging

(4) Performance comparable to many existing event-vision algorithms 

## Experiemnts:
Noise Reduction / HDR Image Reconstruction / Intensity Image Reconstruction / Novel View Synthesis / 3D Sturcture Estimation

