# 📄 **Conda Definitions & Commands (Basic → Advanced)**

## 🔰 1. Basic Definitions

| Term                 | Meaning                                                       |
| -------------------- | ------------------------------------------------------------- |
| **Conda**            | Package + Environment manager for Python/R and other tools.   |
| **Environment**      | A separate workspace with its own Python version & libraries. |
| **Base Environment** | Default environment created during Anaconda installation.     |
| **Channel**          | Source/Repository from where packages are downloaded.         |
| **Package**          | Library or software installed via conda.                      |
| **YAML File**        | File format to store environment configuration.               |

---

## 🟢 2. Basic Conda Commands

### Check Version & Help

```
conda --version
conda --help
conda <command> --help
```

### Create & Manage Environments

```
conda create --name myenv python=3.11
conda activate myenv
conda deactivate
```

### View Details

```
conda env list
conda list
```

### Install / Remove Packages

```
conda install numpy pandas
conda remove numpy
```

---

## 🔵 3. Intermediate Commands

### Update Conda & Packages

```
conda update conda
conda update --all
```

### Clone / Rename / Delete Environment

```
conda create --name clone_env --clone myenv
conda remove --name myenv --all
```

### Export & Import Environment (Reproducibility)

```
conda env export > env.yml
conda env create -f env.yml
```

### Create Environment from YAML

```
conda env create -f environment.yml
```

---

## 🔥 4. Advanced Commands

### Managing Channels

```
conda config --show channels
conda config --add channels conda-forge
conda config --set channel_priority strict
```

### Install Non-Python Tools (Conda Advantage)

```
conda install r-base
conda install ffmpeg
conda install cuda-toolkit
```

### Create Environment With Multiple Languages

```
conda create -n hybrid python=3.11 r-base
```

### Run Applications (Jupyter, Spyder, etc.)

```
conda activate myenv
jupyter lab
spyder
```

### Clean Cache & Unused Packages

```
conda clean --all
```

---

## 🚀 Bonus — Using Mamba (Faster Conda)

### Install Mamba

```
conda install -n base -c conda-forge mamba
```

### Speed Up Installations

```
mamba install numpy
mamba create -n fastenv python=3.11
```

---

# Summary

| Level        | What You Should Know                              |
| ------------ | ------------------------------------------------- |
| Beginner     | Create env, install packages, activate/deactivate |
| Intermediate | Export/import, clone env, updates & backups       |
| Advanced     | Channels, hybrid env, Jupyter, system-level tools |
| Pro          | Mamba, performance optimization, automation       |

---

# 🔥 Extra Advanced Topics (Optional, but very useful)

### ➤ Managing Python versions inside environments

```
conda create -n py38 python=3.8
conda create -n py312 python=3.12
```

---

### ➤ Installing specific package versions

```
conda install numpy=1.26 pandas=2.1.1
```

---

### ➤ Removing channels or resetting config

```
conda config --remove channels conda-forge
conda config --remove-key channels
```

---

### ➤ Search for available packages

```
conda search scikit-learn
```

---

### ➤ List & view configuration settings

```
conda config --show
conda info
```

---

### ➤ Lock environment for production-level consistency

```
conda list --explicit > locked.txt
conda create --name newenv --file locked.txt
```

---

### ➤ Running Python directly inside conda env

```
python
python --version
```

---

# When is your file **complete enough?**

| User Level   | Your File                               | Need More?      |
| ------------ | --------------------------------------- | --------------- |
| Beginner     | ✔ Perfect                               | No              |
| Intermediate | ✔ Enough                                | Optional extras |
| Advanced Pro | 🔶 Expand with locking, version pinning | Yes recommended |

---
