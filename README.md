<!--A curated list of resources for Image and Video Deblurring-->
<!-- PROJECT LOGO -->

<p align="center">
  <h2 align="center">Awesome-Deep-Learning-Technologies-in-Events</h2>
  <p align="center">A curated list of resources for deep learning with events camera.
    <br />
    <br />
    <br />
    <a href="https://github.com/yunfanLu/Awesome-Event-Guided-Enhancement/pulls/new">Suggest new item</a>
    <br />
    <a href="https://github.com/yunfanLu/Awesome-Event-Guided-Enhancement/issues/new">Report Bug</a>
  </p>
</p>

## DDL Time:

2023-01-15

<h2>Table of contents</h2>

- [1  Event Representation](#1--event-representation)
  - [1.0 Event Streaming](#10-event-streaming)
  - [1.1 Event Count Image](#11-event-count-image)
  - [1.2 Event Voxel Grids](#12-event-voxel-grids)
  - [1.3 Surface of Active Event (SAE)](#13-surface-of-active-event-sae)
  - [1.4 Histograms of Averaged Time Surfaces (HATS)](#14-histograms-of-averaged-time-surfaces-hats)
- [2 Event Only](#2-event-only)
  - [2.1 Image / Video Reconstruction](#21-image--video-reconstruction)
    - [(1) Reconstruction and SR](#1-reconstruction-and-sr)
  - [2.2 Optical Flow Estimation](#22-optical-flow-estimation)
  - [2.3 Classifications](#23-classifications)
  - [2.4 Detection](#24-detection)
  - [2.5 Segmentation](#25-segmentation)
- [3 Event + RGB](#3-event--rgb)
  - [3.1 Event Guided Image / Video SR](#31-event-guided-image--video-sr)
  - [3.2 Event Guided Image / Video Deblurring](#32-event-guided-image--video-deblurring)
  - [3.3 Event Guided Image / Video HDR](#33-event-guided-image--video-hdr)
    - [(1) Low Light](#1-low-light)
  - [3.4 Event Guided Image / Video Denoising](#34-event-guided-image--video-denoising)
  - [3.5 Event Guided Video Interpolation](#35-event-guided-video-interpolation)
  - [3.6 Depth estimation](#36-depth-estimation)
- [4 Domain Specific](#4-domain-specific)
  - [4.1 NeRF](#41-nerf)
  - [4.2 Human Pose and Shape](#42-human-pose-and-shape)
  - [4.3 Body and Eye Tracking](#43-body-and-eye-tracking)
  - [4.4 Face](#44-face)
  - [4.5 Compression](#45-compression)
  - [4.4 SAI](#44-sai)
- [5 Robotic Vision](#5-robotic-vision)
  - [5.1 Corner Tracking](#51-corner-tracking)
  - [5.2 Camera Pose Estimation](#52-camera-pose-estimation)
  - [5.3 Calibrate](#53-calibrate)
  - [5.4 Motion Estimation](#54-motion-estimation)
  - [5.5 Visual-Inertial Odometry](#55-visual-inertial-odometry)
  - [5.6 Light Estimation](#56-light-estimation)
- [6 New Direction](#6-new-direction)
- [7 Discussion](#7-discussion)
- [8 Conclusion](#8-conclusion)
- [Supplementary Material](#supplementary-material)
  - [Event Dataset](#event-dataset)
  - [Simulation](#simulation)


# 1  Event Representation
## 1.0 Event Streaming

## 1.1 Event Count Image

## 1.2 Event Voxel Grids


| Publication | Title                                                                                                  | Highlight |
| ----------- | ------------------------------------------------------------------------------------------------------ | --------- |
| T-PAMA 2020 | Time-Ordered Recent Event (TORE) Volumes for Event Cameras                                             |           |
| NC 2019     | Asynchronous Event-Based Motion Processing: From Visual Events to Probabilistic Sensory Representation |           |


## 1.3 Surface of Active Event (SAE)


| Publication | Title                                                                          | Highlight  |
| ----------- | ------------------------------------------------------------------------------ | ---------- |
| T-RAL 2020  | Efﬁcient Spatial-Temporal Normalization of SAE Representation for Event Camera |            |
| T-NLL 2014  | The event-based visual ﬂow                                                     | First work |

## 1.4 Histograms of Averaged Time Surfaces (HATS)
| Publication | Title                                                                                  | Highlight  |
| ----------- | -------------------------------------------------------------------------------------- | ---------- |
| CVPR 2018   | Hats: Histograms of averaged time surfaces for robust event-based object classiﬁcation | First Work |

# 2 Event Only

## 2.1 Image / Video Reconstruction
| Publication | Title                                                                                                                                              | Highlight |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| CVPR 2021   | mage Reconstruction From Neuromorphic Event Cameras Using Laplacian-Prediction and Poisson Integration With Spiking and Artificial Neural Networks |           |
| CVPR 2021   | Event-Based Synthetic Aperture Imaging With a Hybrid Network                                                                                       |           |
| CVPR 2021   | Learning To Reconstruct High Speed and High Dynamic Range Videos From Events                                                                       |           |
| CVPR 2021   | Back to Event Basics: Self-Supervised Learning of Image Reconstruction for Event Cameras via Photometric Constancy                                 |           |
| IJCV 2021   | Learning to Reconstruct HDR Images from Events, with Applications to Depth and Flow Prediction                                                     |           |
| ICCP 2021   | EventGAN: Leveraging Large Scale Image Datasets for Event Cameras                                                                                  |           |
| ECCV 2020   | Reducing the Sim-to-Real Gap for Event Cameras                                                                                                     |           |
| ECCV 2020   | Event Enhanced High-Quality Image Recovery                                                                                                         |           |
| WACV 2020   | Fast Image Reconstruction with an Event Camera                                                                                                     |           |
| T-PAMI 2020 | High Frame Rate Video Reconstruction Based on an Event Camera                                                                                      |           |
| T-PAMI 2019 | High Speed and High Dynamic Range Video with an Event Camera                                                                                       |           |
| CVPR 2019   | Events-to-Video: Bringing Modern Computer Vision to Event Cameras                                                                                  |           |
| IJCV 2018   | Real-Time Intensity-Image Reconstruction for Event Cameras Using Manifold Regularisation                                                           |           |

### (1) Reconstruction and SR
| Publication         | Title                                                                                                                            | Highlight                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| ICCV 2021           | EvIntSR-Net: Event Guided Multiple Latent Frames Reconstruction and Super-resolution                                             | Latent frame reconstruction; MISR            |
| ECCV 2020           | Event Enhanced High-Quality Image Recovery                                                                                       | eSL-Net; Sparse learning                     |
| CVPR 2020           | Joint Filtering of Intensity Images and Neuromorphic Events for High-Resolution Noise-Robust Imaging                             | GEF; Joint filtering                         |
| CVPR 2021           | Turning Frequency to Resolution: Video Super-resolution via Event Cameras                                                        | E-VSR; frequency                             |
| ICCV 2021           | EvIntSR-Net: Event Guided Multiple Latent Frames Reconstruction and Super-resolution                                             |                                              |
| CVPR 2021           | EventZoom: Learning To Denoise and Super Resolve Neuromorphic Events                                                             | Denoise                                      |
| CVPR 2021           | Turning Frequency to Resolution: Video Super-Resolution via Event Camera                                                         | Video SR + RGB                               |
| CVPR 2020           | Learning to Super Resolve Intensity Images from Events                                                                           |                                              |
| CVPR 2020           | EventSR: From Asynchronous Events to Image Reconstruction, Restoration, and Super-Resolution via End-to-End Adversarial Learning | EventSR; End2end; Adversarial learning + RGB |
| TAPMI 2020          | E2SRI: Learning to Super-Resolve Intensity Images from Events                                                                    | SR-Net; RCNN + RGB                           |
| Neurocomputing 2019 | Super-resolution of spatiotemporal event-stream image                                                                            |                                              |


## 2.2 Optical Flow Estimation


| Publication | Title                                                                                                                               | Highlight |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 3DV  2021   | E-RAFT: Dense Optical Flow from Event Cameras                                                                                       |           |
| CVPR 2020   | Single Image Optical Flow Estimation With an Event Camera                                                                           |           |
| CVPR 2019   | Unsupervised Event-Based Learning of Optical Flow, Depth, and Egomotion                                                             |           |
| ICCV 2019   | End-to-End Learning of Representations for Asynchronous Event-Based Data                                                            |           |
| IEEE 2017   | Event-based real-time optical flow estimation                                                                                       |           |
| CVPR 2016   | Simultaneous Optical Flow and Intensity Estimation From an Event Camera                                                             |           |
| CVPR 2021   | Spike Timing-Based Unsupervised Learning of Orientation, Disparity, and Motion Representations in a Spiking Neural Network          |           |
| Arxiv 2021  | Formulating Event-based Image Reconstruction as a Linear Inverse Problem using Optical Flow                                         |           |
| ECCV 2020   | Jointly learning visual motion and confidence from local patches in event cameras                                                   |           |
| T-PAMI 2020 | Real-time high speed motion prediction using fast aperture-robust event-driven visual flow                                          |           |
| CVPR 2020   | SOFEA: A Non-Iterative and Robust Optical Flow Estimation Algorithm for Dynamic Vision Sensors                                      |           |
| CVPR 2020   | Single Image Optical Flow Estimation with an Event Camera                                                                           |           |
| ECCV 2020   | Spike-FlowNet: Event-based Optical Flow Estimation with Energy-Efficient Hybrid Neural Networks                                     |           |
| 3DV 2021    | E-RAFT: Dense Optical Flow from Event Cameras                                                                                       |           |
| T-PAMI 2020 | Distance Surface for Event-Based Optical Flow                                                                                       |           |
| IROS 2020   | Unsupervised Learning of Dense Optical Flow, Depth and Egomotion with Event-Based Sensors                                           |           |
| CVPR 2020   | Single Image Optical Flow Estimation With an Event Camera                                                                           |           |
| T-PAMI 2019 | Unsupervised Learning of a Hierarchical Spiking Neural Network for Optical Flow Estimation: From Events to Global Motion Perception |           |
| ICCV 2019   | End-to-End Learning of Representations for Asynchronous Event-Based Data                                                            |           |
| CVPR 2019   | Unsupervised Event-Based Learning of Optical Flow, Depth, and Egomotion                                                             |           |
| CVPR 2019   | Secrets of Event-based Optical Flow                                                                                                 |           |
| CVPR 2019   | Event-Based Motion Segmentation by Motion Compensation                                                                              |           |
| CVPR 2019   | Event Cameras, Contrast Maximization and Reward Functions: An Analysis                                                              |           |
| ICCV 2019   | End-to-End Learning of Representations for Asynchronous Event-Based Data                                                            |           |
| BMVC 2018   | Adaptive Time-Slice Block-Matching Optical Flow Algorithm for Dynamic Vision Sensors                                                |           |
| RSS 2018    | EV-FlowNet: Self-Supervised Optical Flow Estimation for Event-based Cameras                                                         |           |
| CVPR 2018   | A Unifying Contrast Maximization Framework for Event Cameras, with Applications to Motion, Depth and Optical Flow Estimation        |           |
| T-BCS 2018  | Spiking Optical Flow for Event-based Sensors Using IBM's TrueNorth Neurosynaptic System                                             |           |
| IEEE 2017   | Event-based real-time optical flow estimation                                                                                       |           |
| CVPR 2016   | Simultaneous Optical Flow and Intensity Estimation From an Event Camera                                                             |           |




## 2.3 Classifications

## 2.4 Detection
| Publication | Title                                                                                                             | Highlight |
| ----------- | ----------------------------------------------------------------------------------------------------------------- | --------- |
| NIPS 2020   | Learning to Detect Objects with a 1 Megapixel Event Camera                                                        |           |
| ICRA 2022   | Fusing Event-based and RGB camera for Robust Object Detection in Adverse Conditio                                 |           |
| ICIP 2021   | An Attention Fusion Network For Event-Based Vehicle Object Detection                                              |           |
| TIP  2021   | Asynchronous Spatio-Temporal Memory Network for Continuous Event-Based Object Detection                           |           |
| WACV 2022   | Learned Event-based Visual Perception for Improved Space Object Detection                                         |           |
| IROA 2018   | Event-Based Moving Object Detection and Tracking                                                                  |           |
| ICCVW 2021  | Moving Object Detection for Event-Based Vision Using Graph Spectral Clustering                                    |           |
| ICME 2019   | Event-Based Vision Enhanced: A Joint Detection Framework in Autonomous Driving                                    |           |
| ECCV 2020   | Event-Based Asynchronous Sparse Convolutional Networks                                                            |           |
| MFI 2022    | Global-local Feature Aggregation for Event-based Object Detection on EventKITTI                                   |           |
| TPAMI 2019  | DART: Distribution Aware Retinal Transform for Event-Based Cameras                                                |           |
| CVPR 2018   | Pseudo-Labels for Supervised Learning on Dynamic Vision Sensor Data, Applied to Object Detection Under Ego-Motion |           |
| AAAI 2020   | End-to-End Learning of Object Motion Estimation from Retinal Events for Event-Based Object Tracking               |           |
| TCSVT 2020  | e-TLD: Event-Based Framework for Dynamic Object Tracking                                                          |           |
| IROS 2018   | Towards Event-Driven Object Detection with Off-the-Shelf Deep Learning                                            |           |
| ACCVW 2018  | PCA-RECT: An Energy-Efficient Object Detection Approach for Event Cameras                                         |           |
| CVPRW 2019  | Asynchronous Convolutional Networks for Object Detection in Neuromorphic Cameras                                  |           |
| CVPR  2021  | N-ImageNet: Towards Robust, Fine-Grained Object Recognition with Event Cameras                                    |           |
|             | Detection of Binary Square Fiducial Markers Using an Event Camera                                                 |           |

## 2.5 Segmentation
| Publication | Title                                                                                                                          | Highlight |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------ | --------- |
| CVPRW 2019  | EV-SegNet: Semantic Segmentation for Event-Based Cameras                                                                       |           |
| ECCV 2022   | ESS: Learning Event-Based Semantic Segmentation from Still Images                                                              |           |
| IROS 2021   | ISSAFE: Improving Semantic Segmentation in Accidents by Fusing Event-based Data                                                |           |
| CVPR 2021   | Dual Transfer Learning for Event-Based End-Task Prediction via Pluggable Event to Image Translation                            |           |
| CVPRW 2021  | SoccerNet-v2: A Dataset and Benchmarks for Holistic Understanding of Broadcast Soccer Videos                                   |           |
| CVPR 2020   | Video to Events:Recycling Video Datasets for Event Cameras                                                                     |           |
| CVPR 2020   | Learning Visual Motion Segmentation using Event Surfaces                                                                       |           |
| CVPR 2021   | EvDistill: Asynchronous Events to End-task Learning via Bidirectional Reconstruction-guided Cross-modal Knowledge Distillation |           |
| ICCV 2019   | Event-Based Motion Segmentation by Motion Compensation                                                                         |           |
| TPAMI 2022  | Globally-Optimal Contrast Maximisation for Event Cameras                                                                       |           |
|             | Event-Based Motion Segmentation With Spatio-Temporal Graph Cuts                                                                |           |
|             | Event Camera Survey and Extension Application to Semantic Segmentation                                                         |           |


# 3 Event + RGB 

## 3.1 Event Guided Image / Video SR


| Publication | Title                                                                                                                            | Highlight                              |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| CVPR 2020   | EventSR: From Asynchronous Events to Image Reconstruction, Restoration, and Super-Resolution via End-to-End Adversarial Learning | EventSR; End2end; Adversarial learning |
| TAPMI 2020  | E2SRI: Learning to Super-Resolve Intensity Images from Events                                                                    | SR-Net; RCNN                           |


## 3.2 Event Guided Image / Video Deblurring
| Publication | Title                                                               | Highlight                |
| ----------- | ------------------------------------------------------------------- | ------------------------ |
| ECCV 2020   | Event Enhanced High-Quality Image Recovery                          | eSL-Net; Sparse learning |
| ECCV 2022   | Event-guided Deblurring of Unknown Exposure Time Videos             | ETES; Cross-modal        |
| T-CAI       | Robust motion compensation for event cameras with smooth constraint |                          |
| MMM 2021    | Fine-Grained Video Deblurring with Event Camera                     |                          |
| Access 2020 | Hybrid Deblur Net: Deep Non-Uniform Deblurring With Event Camera    |                          |
| ECCV 2020   | Learning Event-Driven Video Deblurring and Interpolation            |                          |
| ECCV 2020   | Event Enhanced High-Quality Image Recovery                          |                          |
| CVPR 2020   | Learning Event-Based Motion Deblurring                              |                          |
| T-CAI       | Robust motion compensation for event cameras with smooth constraint |                          |



## 3.3 Event Guided Image / Video HDR
| Publication | Title                                                                                                                            | Highlight                  |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| CVPR 2022   | Multi-Bracket High Dynamic Range Imaging With Event Cameras                                                                      |                            |
| CVPR 2021   | Learning To Reconstruct High Speed and High Dynamic Range Videos From Events                                                     |                            |
| IJCV 2021   | Learning to Reconstruct HDR Images from Events, with Applications to Depth and Flow Prediction                                   |                            |
| ICCV 2021   | An Asynchronous Kalman Filter for Hybrid Event Cameras                                                                           |                            |
| CVPR 2019   | Event-based High Dynamic Range Image and Very High Frame Rate Video Generation using Conditional Generative Adversarial Networks | Conditional GAN            |
| TAPMI 2019  | High Speed and High Dynamic Range Video with an Event Camera                                                                     | Recurrent network          |
| CVPR 2021   | Learning to Reconstruct High Speed and High Dynamic Range Videos from Events                                                     | RCNN; Temporal consistency |
| CVPR 2020   | Neuromorphic Camera Guided High Dynamic Range Imaging                                                                            |                            |

### (1) Low Light
| Publication | Title                                   | Highlight |
| ----------- | --------------------------------------- | --------- |
| ECCV 2020   | Learning to See in the Dark with Events |           |

## 3.4 Event Guided Image / Video Denoising

| Publication | Title                                                                                                | Highlight |
| ----------- | ---------------------------------------------------------------------------------------------------- | --------- |
| CVPR 2021   | EventZoom: Learning To Denoise and Super Resolve Neuromorphic Events                                 | Denoise   |
| CVPR 2020   | Joint Filtering of Intensity Images and Neuromorphic Events for High-Resolution Noise-Robust Imaging |           |


## 3.5 Event Guided Video Interpolation

| Publication | Title                                                                                               | Highlight                 |
| ----------- | --------------------------------------------------------------------------------------------------- | ------------------------- |
| CVPR 2022   | TimeReplayer: Unlocking the Potential of Event Cameras for Video Interpolation                      |                           |
| CVPR 2022   | E-CIR: Event-Enhanced Continuous Intensity Recovery                                                 |                           |
| CVPR 2022   | Time Lens++: Event-based Frame Interpolation with Parametric Non-linear Flow and Multi-scale Fusion | Dataset                   |
| CVPR 2022   | Unifying Motion Deblurring and Frame Interpolation with Events                                      |                           |
| ECCV 2022   | Video Interpolation by Event-driven Anisotropic Adjustment of Optical Flow                          |                           |
| ICCV 2021   | Training Weakly Supervised Video Frame Interpolation with Events                                    | Weakly Supervised         |
| CVPR 2021   | Time Lens: Event-based Video Frame Interpolation                                                    | First Work; Dataset       |
| CVPR 2021   | EFI-Net: Video Frame Interpolation from Fusion of Events and Frames                                 | Dataset; Open Dataset     |
| ECCV 2020   | Learning Event-Driven Video Deblurring and Interpolation                                            | Deblurring; Interpolation |
| ICCV-W 2019 | Event-driven Video Frame Synthesis                                                                  |                           |

## 3.6 Depth estimation
| Publication | Title                                                               | Highlight |
| ----------- | ------------------------------------------------------------------- | --------- |
| ICCV 2021   | Event-Intensity Stereo: Estimating Depth by the Best of Both Worlds |           |

# 4 Domain Specific


## 4.1 NeRF
| Publication | Title                                                               | Highlight |
| ----------- | ------------------------------------------------------------------- | --------- |
| Arxiv 2022  | EventNeRF: Neural Radiance Fields from a Single Colour Event Camera |           |

## 4.2 Human Pose and Shape


| Publication | Title                                                                                | Highlight  |
| ----------- | ------------------------------------------------------------------------------------ | ---------- |
| Arxiv 2022  | Efficient Human Pose Estimation via 3D Event Point Cloud                             |            |
| Arxiv 2022  | A Temporal Densely Connected Recurrent Network for Event-based Human Pose Estimation |            |
| ICCV 2021   | EventHands: real-time neural 3D hand pose estimation from an event stream            | Hand Pose  |
| CVPR 2021   | Lifting Monocular Events to 3D Human Poses                                           |            |
| ICCV 2021   | EventHPE: Event-based 3D Human Pose and Shape Estimation                             | Human Pose |
| CVPR 2020   | EventCap: Monocular 3D Capture of High-Speed Human Motions Using an Event Camera     | Human Pose |
| Arxiv 2020  | EventHands: Real-Time Neural 3D Hand Reconstruction from an Event Stream             | Hand Pose  |
| WACV 2019   | Space-Time Event Clouds for Gesture Recognition: From RGB Cameras to Event Cameras   | Hand Pose  |
| CVPR 2019   | DHP19: Dynamic Vision Sensor 3D Human Pose Dataset                                   |            |
| Arxiv 2019  | EventGAN: Leveraging Large Scale Image Datasets for Event Cameras                    |            |



## 4.3 Body and Eye Tracking

| Publication | Title                                                                             | Highlight |
| ----------- | --------------------------------------------------------------------------------- | --------- |
|             | Object tracking on event cameras with offline–online learning                     |           |
|             | Real-Time Face & Eye Tracking and Blink Detection using Event Cameras             |           |
| ECCV 2020   | Stereo Event-based Particle Tracking Velocimetry for 3D Fluid Flow Reconstruction |           |
| ISFV 2014   | Large-scale Particle Tracking with Dynamic Vision Sensors                         |           |
| T-CG 2021   | Event Based, Near-Eye Gaze Tracking Beyond 10,000Hz                               | Dataset   |

## 4.4 Face
| Publication | Title                                  | Highlight |
| ----------- | -------------------------------------- | --------- |
| Sensor 2020 | Face pose alignment with event cameras |           |



## 4.5 Compression
| Publication | Title                                       | Highlight |
| ----------- | ------------------------------------------- | --------- |
| T-SPL 2020  | Lossless Compression of Event Camera Frames |           |

## 4.4 SAI

| Publication | Title                                                        | Highlight |
| ----------- | ------------------------------------------------------------ | --------- |
| CVPR 2021   | Event-Based Synthetic Aperture Imaging With a Hybrid Network |           |


# 5 Robotic Vision

## 5.1 Corner Tracking

| Publication | Title                                                                                      | Highlight |
| ----------- | ------------------------------------------------------------------------------------------ | --------- |
| CVPR-W 2019 | Fast Event-based Corner Detection                                                          |           |
| CVPR-W 2019 | Speed Invariant Time Surface for Learning to Detect Corner Points with Event-Based Cameras |           |
|             | Object tracking on event cameras with offline–online learning                              |           |
|             | Real-Time Face & Eye Tracking and Blink Detection using Event Cameras                      |           |
| ECCV 2020   | Stereo Event-based Particle Tracking Velocimetry for 3D Fluid Flow Reconstruction          |           |
| ISFV 2014   | Large-scale Particle Tracking with Dynamic Vision Sensors                                  |           |


## 5.2 Camera Pose Estimation


## 5.3 Calibrate

| Publication | Title                              | Highlight |
| ----------- | ---------------------------------- | --------- |
| CVPR-W 2021 | How To Calibrate Your Event Camera |           |

## 5.4 Motion Estimation
| Publication | Title                                                        | Highlight           |
| ----------- | ------------------------------------------------------------ | ------------------- |
| T-IRAL 2016 | Accurate Angular Velocity Estimation With an Event Camera    | velocity estimation |
| ICRA 2020   | EVDodgeNet: Deep Dynamic Obstacle Dodging with Event Cameras |                     |

## 5.5 Visual-Inertial Odometry

| sensors     | Visual Odometry with an Event Camera Using Continuous Ray Warping and Volumetric Contrast Maximization |           |

## 5.6 Light Estimation
| Publication | Title                                            | Highlight |
| ----------- | ------------------------------------------------ | --------- |
| CVPR 2021   | Indoor Lighting Estimation Using an Event Camera |           |

# 6 New Direction


# 7 Discussion


# 8 Conclusion




# Supplementary Material

## Event Dataset

| Publication | Title                                                                                   | Highlight    |
| ----------- | --------------------------------------------------------------------------------------- | ------------ |
| CVPR 2022   | Video to -Events: Recycling Video Datasets for Event Cameras                            |              |
|             | DSEC: A Stereo Event Camera Dataset for Driving Scenarios                               |              |
| T-CG 2021   | Event Based, Near-Eye Gaze Tracking Beyond 10,000Hz                                     | Eye Tracking |
| IEEE 2021   | DSEC: A Stereo Event Camera Dataset for Driving Scenarios                               |              |
| CVPR 2019   | CED: Color Event Camera Dataset                                                         | First Color  |
| CVPR 2019   | DHP19: Dynamic Vision Sensor 3D Human Pose Dataset                                      |              |
| IEEE 2018   | The Multivehicle Stereo Event Camera Dataset: An Event Camera Dataset for 3D Perception |              |

## Simulation
| Publication | Title                                                       | Highlight |
| ----------- | ----------------------------------------------------------- | --------- |
| ECCV 2020   | Reducing the Sim-to-Real Gap for Event Cameras              |           |
| CVPR 20202  | Video to Events: Recycling Video Datasets for Event Cameras |           |