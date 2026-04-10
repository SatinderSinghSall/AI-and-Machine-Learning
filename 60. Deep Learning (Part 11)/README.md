# AI / ML: Deep Learning (Part 11)

# 🧠 Deep Learning – Generative Adversarial Networks (GANs)

### _Deep Learning Module | Prime AI/ML Batch (Part 11)_

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![PyTorch](https://img.shields.io/badge/Framework-PyTorch-red)
![GAN](https://img.shields.io/badge/Model-GAN-purple)
![DCGAN](https://img.shields.io/badge/Architecture-DCGAN-green)
![Dataset](https://img.shields.io/badge/Dataset-CelebA-orange)
![Status](https://img.shields.io/badge/Module-Completed-success)

---

## 📖 Overview

This module focuses on the **theory and implementation of Generative Adversarial Networks (GANs)**, one of the most powerful generative models in deep learning.

The project includes:

- Implementation of **Vanilla GAN**
- Advanced architecture using **Deep Convolutional GAN (DCGAN)**
- Training on **image datasets (CelebA)**
- Visualization of generated synthetic images

---

## 🎯 Objectives

- Understand **adversarial learning**
- Implement **Generator & Discriminator networks**
- Train GANs on real-world datasets
- Analyze **training stability and performance**
- Generate realistic synthetic images

---

## 🧠 Key Concepts Covered

### 1️⃣ Introduction to GANs

- Generative vs Discriminative models
- Adversarial training paradigm
- Minimax game concept

### 2️⃣ GAN Architecture

- Generator vs Discriminator roles
- Loss functions
- Training dynamics

### 3️⃣ Generator Network

- Latent vector (noise input)
- Upsampling layers
- Activation functions (ReLU, Tanh)

### 4️⃣ Discriminator Network

- Binary classification (Real vs Fake)
- CNN-based architecture
- Activation functions (LeakyReLU, Sigmoid)

### 5️⃣ Dataset Preparation

- CelebA dataset usage
- Image preprocessing & normalization
- Data loading pipelines

### 6️⃣ Vanilla GAN Implementation

- Fully connected architecture
- Basic adversarial training loop
- Loss tracking

### 7️⃣ DCGAN Architecture

- Convolutional layers
- Batch Normalization
- Improved training stability

### 8️⃣ Training the GAN

- Epoch-based training
- Balancing Generator & Discriminator
- Avoiding mode collapse

### 9️⃣ Results & Visualization

- Generated images over epochs
- Quality comparison (Vanilla vs DCGAN)

---

## 🧠 GAN Architecture Overview

---

## 📂 Project Structure

```bash
60. Deep Learning (Part 11)
│
├── vanilla_gan.ipynb        # Basic GAN implementation
├── dcgan.ipynb              # DCGAN implementation
│
├── data/
│   └── CelebA dataset       # Training dataset
│
├── outputs/
│   ├── epoch_1.png
│   ├── epoch_10.png
│   └── generated_images/
│
└── README.md
```

---

## ⚙️ Tech Stack

| Category      | Tools / Libraries |
| ------------- | ----------------- |
| Language      | Python            |
| Framework     | PyTorch           |
| Visualization | Matplotlib        |
| Dataset       | CelebA            |
| Environment   | Jupyter Notebook  |

---

## 🔄 Training Workflow

![Image](https://images.openai.com/static-rsc-4/aTL5Fz6DUyAadsEBYDt6Td8PqPiX-XB8tqof8Ea4pLhskuiBaHof9eLZELCiSe8KbRSt46D77yCZa6aZsgBRQ58AyWjkdjEYrwPg-e78UChVl0puAgamlcW0bCUIky2P8eG-oRfUYAO8OFqhTFaZrAe-HIARPrbHB5Lzx47_Nq85Q0MfZgsgaw79iyaaG_MT?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/xsG4ahjJqCSGibnxuNswto0PdB6YXEqJUel0KXiJpLIhbHXi8DMFQ_aN5KbyKxIWm6lQBHbvOcYGwgZdF1GYddMdMlridUZVvSMkV2sUXwmGAdUQ2dysi22A_H_bKd087HtG06Em1Dh0uIiBb9zmBj17bcrge8aJGcwQjD5FlGaqTT7-6oHJaDQJ_pTE2COC?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/gxsvQNACn91SE71qME-Ads4CiwypYgLccs2Mr-D1M9EOWLYii_xhMKhhio7E5BoJnDAHRrN8UBq0Fp1PUSqun_-CtVErpl2opL48ECXwmaqNu9f9RMsldJqTKd8xNIkFgcny_eAsYALvKhMiCkG6aALcBYU56kgf27PdiofWXTEREmBhmJBc3wRcX1R-8rCU?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/dt49KNMa6zXJ5cGVZkVfh7b6qLreHF3Lbv7cF6VEl4lLrqMZxkCk7T3iOVxcQz_u03qWKd2PP2dNfEh9H_rfBOXolJaLbPckmlcWRqAtZdSZmzUfnbBhxZseWEtte8j_rzMni987TCnSp8pRwHJau-nBFARMpp-BUgq-fgfDBF6KHEVFpdIB7zCruK7RowG3?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/OBwnpzfHKGmK_w7ulWZ6Ol0ZuFP9FZeNTOQx4z-naSdJ2oMMx3OEHx6p4SVl5j_2_HO_yYbWv7Au2rlftJuP-_b8WMoF08ZyPINGMOtIAM6KiITcUZk6rjHI4snU8F_pCYGusi1LmpgKDSKU3f_Uv4732TBVr0U_1cBWzNVzBdLkCKkvRDpTHrv14LevfxNt?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/TpsA1BCyeLULSvDy3HhrXaMJ8pHDlVILBaj_ir3INFzhM5HUgt3GgaQ4U5Y1_u2-dGukBerG2mmPDeeMuUrbSoIFlu4vgYIeOBbbge7cswyo6wcBbte8Q8ZF3EZWxhR_e0Dp73RLISCsCEMTwpvnrpW7S7EVyfpSxMVDB-iuPS4CKEEn6PSlONOC1FWU7ede?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/5o5vS6gCLHE0VQSQkOb25SGsUnjBq3w0FMyWxgZT3PI3n23OerZ6fjdr7O3gzTuP5GETLjiqXfN4W6Y4BxUqJnFxETCvfNk1QDAPZPY-3nQSD3QbhzuzfXeHC4R6aYl19Y4G-15eD3dMddgfsJqiJdV96q-DV0IvaK56xyNrJdd8JX1WBS4vHe-HFbJJ98n3?purpose=fullsize)

### Step-by-Step Process

1. **Generate Noise Vector (z)**
2. **Generator creates fake image**
3. **Discriminator evaluates real vs fake**
4. **Compute losses**
5. **Update Discriminator**
6. **Update Generator**
7. **Repeat for multiple epochs**

---

## 🧪 Implementation Details

### ✔️ Vanilla GAN

- Fully connected neural networks
- Basic adversarial setup
- Less stable training

### ✔️ DCGAN

- Convolutional layers
- Batch normalization
- Improved convergence and image quality

### ✔️ Training Strategy

- Alternating optimization
- Careful learning rate tuning
- Monitoring loss curves

---

## 📊 Results

- Generated realistic face images using **DCGAN**
- Observed:
  - Early epochs → noisy outputs
  - Later epochs → structured, human-like faces

### 🔍 Comparison

| Feature       | Vanilla GAN | DCGAN  |
| ------------- | ----------- | ------ |
| Stability     | Low         | High   |
| Image Quality | Moderate    | High   |
| Training Ease | Difficult   | Easier |

---

## 📈 Learning Outcomes

- ✅ Mastered **GAN fundamentals**
- ✅ Implemented **end-to-end generative models**
- ✅ Understood **training instability challenges**
- ✅ Learned **CNN-based generative architectures**
- ✅ Compared **basic vs advanced GANs**

---

## ⚠️ Challenges Faced

- Mode collapse
- Training instability
- Hyperparameter tuning
- Balancing Generator & Discriminator

---

## 🔮 Future Enhancements

- 🔹 Conditional GAN (cGAN)
- 🔹 StyleGAN implementation
- 🔹 High-resolution image generation
- 🔹 GAN evaluation metrics (FID Score)

---

## 📚 References

- Ian Goodfellow et al. – _Generative Adversarial Networks_
- PyTorch Documentation
- CelebA Dataset Documentation

---

## 👨‍💻 Author

**Satinder Singh Sall**
_AI/ML Engineer | Deep Learning Enthusiast_

**Course:** Prime AI/ML Batch – Deep Learning (Part 11)
**Date:** April 2026

---

## 🏁 Conclusion

This project demonstrates the power of **adversarial learning** in generating realistic data.

> 🎯 **GANs = Generator vs Discriminator → Learning through competition**

It forms a strong foundation for advanced generative models like:

- StyleGAN
- Diffusion Models
- Image-to-Image Translation

---

## ⭐ If you found this useful

Give it a ⭐ on GitHub and share it 🚀

---

# 📘 Deep Learning Module: Generative Adversarial Networks (GANs)

## 📌 Overview

This repository contains my coursework and assignments from the **Deep Learning (Part 11)** module, focused on **Generative Adversarial Networks (GANs)**. The work covers both theoretical understanding and practical implementation of GAN architectures, including Vanilla GAN and Deep Convolutional GAN (DCGAN).

The objective of this module is to understand how generative models learn data distributions and generate realistic synthetic data, particularly images.

---

## 🧠 Topics Covered

### 1. Introduction to GANs

- Concept of generative modeling
- Difference between discriminative vs generative models
- Basic GAN framework
- Adversarial training process

### 2. GAN Architecture

- Generator vs Discriminator roles
- Loss functions and optimization
- Minimax game formulation

### 3. Generator Network

- Input noise vector (latent space)
- Neural network design
- Activation functions (ReLU, Tanh)
- Upsampling techniques

### 4. Discriminator Network

- Binary classification (real vs fake)
- CNN-based architecture
- Activation functions (LeakyReLU, Sigmoid)

### 5. Dataset Preparation

- CelebA dataset setup
- Image preprocessing (normalization, resizing)
- Data loading pipelines

### 6. GAN Implementation

- Vanilla GAN from scratch
- Training loop design
- Loss tracking and visualization

### 7. DCGAN (Deep Convolutional GAN)

- Convolutional architecture improvements
- Batch Normalization
- Stable training practices

### 8. Training the GAN

- Epoch-wise training
- Generator vs Discriminator balance
- Avoiding mode collapse

### 9. Results & Visualization

- Generated fake images
- Output after multiple epochs
- Model performance analysis

---

## 📂 Repository Structure

```
├── vanilla_gan.ipynb      # Implementation of basic GAN
├── dcgan.ipynb            # Implementation of DCGAN
├── README.md              # Project documentation
```

---

## ⚙️ Technologies Used

- Python
- PyTorch / TensorFlow (based on your implementation)
- NumPy
- Matplotlib
- Jupyter Notebook

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/gan-project.git
cd gan-project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run notebooks:

```bash
jupyter notebook
```

---

## 📊 Results

- Successfully trained GAN models to generate synthetic images.
- Observed progressive improvement in image quality across epochs.
- Compared Vanilla GAN vs DCGAN performance:
  - DCGAN produced more stable and realistic outputs.
  - Vanilla GAN showed instability and noise in early training.

---

## 📈 Key Learnings

- Understanding adversarial training dynamics is crucial.
- Proper balance between generator and discriminator is necessary.
- Architectural improvements (DCGAN) significantly enhance performance.
- Training GANs is sensitive and requires tuning.

---

## ⚠️ Challenges Faced

- Mode collapse during training
- Instability in loss convergence
- Hyperparameter tuning complexity
- Dataset preprocessing issues

---

## 🔮 Future Work

- Implement Conditional GANs (cGAN)
- Explore StyleGAN architectures
- Improve training stability techniques
- Apply GANs to real-world datasets

---

## 📚 References

- Goodfellow et al., "Generative Adversarial Networks"
- PyTorch / TensorFlow official documentation
- Course materials from AI/ML Batch

---

## 👨‍💻 Author

**Satinder Singh Sall**
AI/ML Student

---
