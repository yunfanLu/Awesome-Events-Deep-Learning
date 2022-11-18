<!--A curated list of resources for Image and Video Deblurring-->
<!-- PROJECT LOGO -->

<p align="center">
  <h2 align="center">Awesome-Deep-Learning-Technologies-in-Events</h2>
  <p align="center">A curated list of resources for de#ep learning with events camera.
    <br />
    <br />
    <br />
    <a href="https://github.com/yunfanLu/Awesome-Event-Guided-Enhancement/pulls/new">Suggest new item</a>
    <br />
    <a href="https://github.com/yunfanLu/Awesome-Event-Guided-Enhancement/issues/new">Report Bug</a>
  </p>
</p>

## Conference Time:

| conference | Submission deadline |
| ---------- | ------------------- |
| AAAI2023   | 2022/08/08          |
| CVPR2023   | 2022/11(TBD)        |

<h2>Table of contents</h2>

- [0. Event Imaging, Simulation, Representation and Dataset](#0-event-imaging-simulation-representation-and-dataset)
  - [0.1 Imaging](#01-imaging)
  - [0.1 Simulation](#01-simulation)
  - [0.2 Representation](#02-representation)
  - [0.3 Dataset](#03-dataset)
- [1. Low-Level Vision](#1-low-level-vision)
  - [1.0 Image / Video Reconstruction](#10-image--video-reconstruction)
  - [1.1 Super Resolution with Event](#11-super-resolution-with-event)
  - [1.2 Deblurring with Event](#12-deblurring-with-event)
  - [1.3 Video Interpolation with Event](#13-video-interpolation-with-event)
  - [1.4 Low-light Image Enhancement with Event](#14-low-light-image-enhancement-with-event)
  - [1.5 HDR Imaging with Event](#15-hdr-imaging-with-event)
  - [1.6 Denoising](#16-denoising)
  - [1.7 Super Resolution](#17-super-resolution)
  - [1.8 Deblur](#18-deblur)
  - [1.9 Calibrate](#19-calibrate)
  - [1.10 Optical Flow Estimation](#110-optical-flow-estimation)
  - [1.11 Motion Estimation](#111-motion-estimation)
  - [1.12 SAI](#112-sai)
- [2 High-Level](#2-high-level)
  - [2.1 Detection](#21-detection)
  - [2.2 Segmentation](#22-segmentation)
  - [2.3 Pose Estimation](#23-pose-estimation)
  - [2.4 Video Understanding](#24-video-understanding)
  - [2.5 Tracking](#25-tracking)
  - [2.6 Visual-Inertial Odometry](#26-visual-inertial-odometry)
- [3 Three-D Vision with Event](#3-three-d-vision-with-event)
  - [3.1 NeRF with Events](#31-nerf-with-events)
  - [3.2 3D Reconstruction with Events](#32-3d-reconstruction-with-events)
  - [3.3 Depth estimation](#33-depth-estimation)
- [4. Compression](#4-compression)
- [4.1 Lossless](#41-lossless)

# 0. Event Imaging, Simulation, Representation and Dataset

## 0.1 Imaging

## 0.1 Simulation

| Publication | Title                                                       | Highlight |
| ----------- | ----------------------------------------------------------- | --------- |
| ECCV 2020   | Reducing the Sim-to-Real Gap for Event Cameras              |           |
| CVPR 20202  | Video to Events: Recycling Video Datasets for Event Cameras |           |

## 0.2 Representation

| Publication | Title                                                                                                  | Highlight |
| ----------- | ------------------------------------------------------------------------------------------------------ | --------- |
| T-PAMA 2020 | Time-Ordered Recent Event (TORE) Volumes for Event Cameras                                             |           |
| NC 2019     | Asynchronous Event-Based Motion Processing: From Visual Events to Probabilistic Sensory Representation |           |

## 0.3 Dataset

| Publication | Title                                                                                   | Highlight    |
| ----------- | --------------------------------------------------------------------------------------- | ------------ |
| CVPR 2022   | Video to -Events: Recycling Video Datasets for Event Cameras                            |              |
|             | DSEC: A Stereo Event Camera Dataset for Driving Scenarios                               |              |
| T-CG 2021   | Event Based, Near-Eye Gaze Tracking Beyond 10,000Hz                                     | Eye Tracking |
| IEEE 2021   | DSEC: A Stereo Event Camera Dataset for Driving Scenarios                               |              |
| CVPR 2019   | CED: Color Event Camera Dataset                                                         | First Color  |
| CVPR 2019   | DHP19: Dynamic Vision Sensor 3D Human Pose Dataset                                      |              |
| IEEE 2018   | The Multivehicle Stereo Event Camera Dataset: An Event Camera Dataset for 3D Perception |              |

# 1. Low-Level Vision

## 1.0 Image / Video Reconstruction

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

## 1.1 Super Resolution with Event

| Publication | Title                                                                                                | Highlight                         |
| ----------- | ---------------------------------------------------------------------------------------------------- | --------------------------------- |
| ICCV 2021   | EvIntSR-Net: Event Guided Multiple Latent Frames Reconstruction and Super-resolution                 | Latent frame reconstruction; MISR |
| ECCV 2020   | Event Enhanced High-Quality Image Recovery                                                           | eSL-Net; Sparse learning          |
| CVPR 2020   | Joint Filtering of Intensity Images and Neuromorphic Events for High-Resolution Noise-Robust Imaging | GEF; Joint filtering              |
| CVPR 2021   | Turning Frequency to Resolution: Video Super-resolution via Event Cameras                            | E-VSR; frequency                  |

## 1.2 Deblurring with Event

| Publication | Title                                                   | Highlight                |
| ----------- | ------------------------------------------------------- | ------------------------ |
| ECCV 2020   | Event Enhanced High-Quality Image Recovery              | eSL-Net; Sparse learning |
| ECCV 2022   | Event-guided Deblurring of Unknown Exposure Time Videos | ETES; Cross-modal        |

## 1.3 Video Interpolation with Event

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

## 1.4 Low-light Image Enhancement with Event

| Publication | Title                                   | Highlight |
| ----------- | --------------------------------------- | --------- |
| ECCV 2020   | Learning to See in the Dark with Events |           |

## 1.5 HDR Imaging with Event

| Publication | Title                                                                                                                            | Highlight                  |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| CVPR 2022   | Multi-Bracket High Dynamic Range Imaging With Event Cameras                                                                      |                            |
| CVPR 2021   | Learning To Reconstruct High Speed and High Dynamic Range Videos From Events                                                     |                            |
| IJCV 2021   | Learning to Reconstruct HDR Images from Events, with Applications to Depth and Flow Prediction                                   |                            |
| ICCV 2021   | An Asynchronous Kalman Filter for Hybrid Event Cameras                                                                           |                            |
| CVPR 2019   | Event-based High Dynamic Range Image and Very High Frame Rate Video Generation using Conditional Generative Adversarial Networks | Conditional GAN            |
| TAPMI 2019  | High Speed and High Dynamic Range Video with an Event Camera                                                                     | Recurrent network          |
| CVPR 2021   | Learning to Reconstruct High Speed and High Dynamic Range Videos from Events                                                     | RCNN; Temporal consistency |

## 1.6 Denoising

| Publication | Title                                                                                                | Highlight |
| ----------- | ---------------------------------------------------------------------------------------------------- | --------- |
| CVPR 2021   | EventZoom: Learning To Denoise and Super Resolve Neuromorphic Events                                 | Denoise   |
| CVPR 2020   | Joint Filtering of Intensity Images and Neuromorphic Events for High-Resolution Noise-Robust Imaging |           |

## 1.7 Super Resolution

| Publication         | Title                                                                                                                            | Highlight                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| ICCV 2021           | EvIntSR-Net: Event Guided Multiple Latent Frames Reconstruction and Super-resolution                                             |                                              |
| CVPR 2021           | EventZoom: Learning To Denoise and Super Resolve Neuromorphic Events                                                             | Denoise                                      |
| CVPR 2021           | Turning Frequency to Resolution: Video Super-Resolution via Event Camera                                                         | Video SR + RGB                               |
| CVPR 2020           | Learning to Super Resolve Intensity Images from Events                                                                           |                                              |
| CVPR 2020           | EventSR: From Asynchronous Events to Image Reconstruction, Restoration, and Super-Resolution via End-to-End Adversarial Learning | EventSR; End2end; Adversarial learning + RGB |
| TAPMI 2020          | E2SRI: Learning to Super-Resolve Intensity Images from Events                                                                    | SR-Net; RCNN + RGB                           |
| Neurocomputing 2019 | Super-resolution of spatiotemporal event-stream image                                                                            |                                              |

## 1.8 Deblur

| Publication | Title                                                               | Highlight |
| ----------- | ------------------------------------------------------------------- | --------- |
| MMM 2021    | Fine-Grained Video Deblurring with Event Camera                     |           |
| Access 2020 | Hybrid Deblur Net: Deep Non-Uniform Deblurring With Event Camera    |           |
| ECCV 2020   | Learning Event-Driven Video Deblurring and Interpolation            |           |
| ECCV 2020   | Event Enhanced High-Quality Image Recovery                          |           |
| CVPR 2020   | Learning Event-Based Motion Deblurring                              |           |
| T-CAI       | Robust motion compensation for event cameras with smooth constraint |           |

## 1.9 Calibrate

| Publication | Title                              | Highlight |
| ----------- | ---------------------------------- | --------- |
| CVPR-W 2021 | How To Calibrate Your Event Camera |           |

## 1.10 Motion Estimation

| Publication | Title                                                        | Highlight           |
| ----------- | ------------------------------------------------------------ | ------------------- |
| T-IRAL 2016 | Accurate Angular Velocity Estimation With an Event Camera    | velocity estimation |
| ICRA 2020   | EVDodgeNet: Deep Dynamic Obstacle Dodging with Event Cameras |                     |

## 1.11 SAI

| Publication | Title                                                        | Highlight |
| ----------- | ------------------------------------------------------------ | --------- |
| CVPR 2021   | Event-Based Synthetic Aperture Imaging With a Hybrid Network |           |

## 1.12 Camera Pose Estimation

| Publication | Title                                                                              | Highlight                |
| ----------- | ---------------------------------------------------------------------------------- | ------------------------ |
| CVPR 2019   | Space-Time Event Clouds for Gesture Recognition: From RGB Cameras to Event Cameras | 6DOF Pose Relocalization |

## 1.13 Optical Flow Estimation

| Publication | Title                                                                                                                               | Highlight |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------- |
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
| ICCV 2020   | Single Image Optical Flow Estimation With an Event Camera                                                                           |           |
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

## 1.14 Corner Detection and Tracking

| Publication | Title                                                                                      | Highlight |
| ----------- | ------------------------------------------------------------------------------------------ | --------- |
| CVPR-W 2019 | Fast Event-based Corner Detection                                                          |           |
| CVPR-W 2019 | Speed Invariant Time Surface for Learning to Detect Corner Points with Event-Based Cameras |           |

## 1.15 Tone Mapping

| Publication | Title                                                 | Highlight |
| ----------- | ----------------------------------------------------- | --------- |
| CVPR 2020   | Neuromorphic Camera Guided High Dynamic Range Imaging |           |

## 1.17 Indoor Lighting Estimation

| Publication | Title                                            | Highlight |
| ----------- | ------------------------------------------------ | --------- |
| CVPR 2021   | Indoor Lighting Estimation Using an Event Camera |           |

# 2 High-Level

## 2.1 Detection

| Publication | Title                                                                                                             | Highlight |
| ----------- | ----------------------------------------------------------------------------------------------------------------- | --------- |
| NIPS 2020   | Learning to Detect Objects with a 1 Megapixel Event Camera                                                        |           |
| ICRA 2022   | Fusing Event-based and RGB camera for Robust Object Detection in Adverse Conditio                                 |           |
| ICIP 2021   | An Attention Fusion Network For Event-Based Vehicle Object Detection                                              |           |
| TIP 2021    | Asynchronous Spatio-Temporal Memory Network for Continuous Event-Based Object Detection                           |           |
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
| CVPR 2021   | N-ImageNet: Towards Robust, Fine-Grained Object Recognition with Event Cameras                                    |           |
|             | Detection of Binary Square Fiducial Markers Using an Event Camera                                                 |           |

## 2.2 Segmentation

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

## 2.3 Pose Estimation

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

## 2.6 Face

| Publication | Title                                  | Highlight |
| ----------- | -------------------------------------- | --------- |
| Sensor 2020 | Face pose alignment with event cameras |           |

## 2.5 Video Understanding

| Publication | Title                                                                | Highlight |
| ----------- | -------------------------------------------------------------------- | --------- |
|             | Dynamic Graph CNN for Event-Camera Based Gesture Recognition         |           |
|             | Human identification by gait from event-based camera                 |           |
|             | Multipath Event-Based Network for Low-Power Human Action Recognition |           |

## 2.6 Tracking

| Publication | Title                                                                             | Highlight |
| ----------- | --------------------------------------------------------------------------------- | --------- |
|             | Object tracking on event cameras with offline–online learning                     |           |
|             | Real-Time Face & Eye Tracking and Blink Detection using Event Cameras             |           |
| ECCV 2020   | Stereo Event-based Particle Tracking Velocimetry for 3D Fluid Flow Reconstruction |           |
| ISFV 2014   | Large-scale Particle Tracking with Dynamic Vision Sensors                         |           |

## 2.7 Eye Tracking

| Publication | Title                                                                 | Highlight |
| ----------- | --------------------------------------------------------------------- | --------- |
| T-CG 2021   | Event Based, Near-Eye Gaze Tracking Beyond 10,000Hz                   | Dataset   |
| Arxiv 2020  | Real-Time Face & Eye Tracking and Blink Detection using Event Cameras |           |

## 2.8 Visual-Inertial Odometry

| Publication | Title                                                                                                  | Highlight |
| ----------- | ------------------------------------------------------------------------------------------------------ | --------- |
| sensors     | Visual Odometry with an Event Camera Using Continuous Ray Warping and Volumetric Contrast Maximization |           |

# 3 Three-D Vision with Event

## 3.1 NeRF with Events

| Publication | Title                                                               | Highlight |
| ----------- | ------------------------------------------------------------------- | --------- |
| Arxiv 2022  | EventNeRF: Neural Radiance Fields from a Single Colour Event Camera |           |

## 3.2 3D Reconstruction with Events

## 3.3 Depth estimation

| Publication | Title                                                               | Highlight |
| ----------- | ------------------------------------------------------------------- | --------- |
| ICCV 2021   | Event-Intensity Stereo: Estimating Depth by the Best of Both Worlds |           |

# 4. Compression

## 4.1 Lossless

| Publication | Title                                       | Highlight |
| ----------- | ------------------------------------------- | --------- |
| T-SPL 2020  | Lossless Compression of Event Camera Frames |           |

# 5 Application

## 5.1 Human-Object Interactions

| Publication | Title | Highlight |
| ----------- | ----- | --------- |
| CVPR 2021   |       |           |
