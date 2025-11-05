<h1 align="center">Development of a Two-Step Artificial Intelligence System
for the Detection and Classification of Recreational Fishing</h1>

<p align="center"> 
  <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Python"> 
  <img src="https://img.shields.io/badge/Framework-Ultralytics%20YOLO-red.svg" alt="YOLO"> 
  <img src="https://img.shields.io/badge/Deep%20Learning-PyTorch-orange.svg" alt="PyTorch"> 
  <img src="https://img.shields.io/badge/Platform-Google%20Colab-yellow.svg" alt="Colab"> 
  <img src="https://img.shields.io/badge/Architecture-Two--Step%20AI-green.svg" alt="2-Step AI"> 
</p>

<p>
A two-step computer vision system designed to automatically detect and classify recreational fishing activities on beaches and coastal areas.
The system improves monitoring accuracy by separating person detection and fisher classification into two dedicated deep learning models.
</p>

<hr>

<p align="center">
<img src="docs/2step_diagram.png" width="850">
</p>

<h2>Development</h2>

<h3>1. Person Detection Model (YOLOv11-L) - Detection</h3>

<h4><i>Manual hyperparameter search</i></h4>

<p>A total of <strong>7 custom configurations</strong> were manually designed and tested, varying:</p>
<ul>
  <li>Learning rate</li>
  <li>Optimizer (AUTO vs SGD)</li>
  <li>Momentum</li>
  <li>Distribution Focal Loss (DFL)</li>
  <li>Image size and batch size</li>
</ul>
<p>Each configuration was trained for 50 epochs on Google Colab, using early stopping to compare performance.</p>

<h4><i>Training with best configuration</i></h4>
<p>The configuration <code>config3_lr_basso</code> showed the best detection metrics (<strong>mAP50, Recall, Precision</strong>) and was selected for full training.</p>

<h4><i>Testing</i></h4>
<p>The model was evaluated on the Mix Detection test set, achieving the following results:

<ul>
  <li><strong>mAP50:</strong> 0.561</li>
  <li><strong>mAP50-95:</strong> 0.301</li>
  <li><strong>Precision:</strong> 0.701</li>
  <li><strong>Recall:</strong> 0.498</li>
</ul></p>

<p align="center">
<img src="runs/detect/val/val_batch1_pred.jpg" width="850">
</p>


<hr>

<h3>2. Person–Fisher Classification Model (YOLOv11-Classify) - Classification</h3>

<h4><i>Automated hyperparameter tuning</i></h4>
<p>The <strong>YOLO tune</strong> method was used for automatic hyperparameter optimization.</p>

<h4><i>Training with optimal parameters</i></h4>
<p>The classification model was trained using the best configuration identified by the automated tuning.</p>

<h4><i>Testing</i></h4>
<p>The model was evaluated on the Mix Classification test set, achieving the following results:

<ul>
  <li><strong>Top-1 accuracy:</strong> 99.16%</li>
  <li><strong>Inference Time:</strong> 412 ms</li>
</ul></p>

<p align="center">
<img src="runs/classify/val/val_batch0_pred.jpg" width="850">
</p>



<h2>Tech Stack</h2>
<ul>
  <li>Python 3.12</li>
  <li>Ultralytics YOLOv11</li>
  <li>PyTorch</li>
  <li>Google Colab (A100/T4 GPUs)</li>
</ul>

<h2>Documentation</h2>
<p>
Full technical documentation available here: 
<a href="/docs/Tesi_Michele_Vigliotta.pdf"><code>Tesi_Michele_Vigliotta.pdf</code></a>
</p>

<h2>Authors</h2>

* Michele Vigliotta

<hr>

<p align="center"><i>University project developed as part of the thesis work.</i></p>




