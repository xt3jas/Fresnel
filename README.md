# Fresnel

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Beta-orange?style=for-the-badge)

**Deep Text Analysis. 100% Deterministic.**

[Features](#-key-features) • [Installation](#-installation--usage) • [Roadmap](#-future-implementation-plan)

</div>

---

## What is Fresnel?

**Fresnel** is a lightweight forensic text analysis engine designed to reveal the hidden mathematical structure of written language.
Unlike modern LLMs (ChatGPT, Claude) that "read" text by predicting the next token, Fresnel analyzes the **physical and statistical properties** of the text itself: entropy, vector similarity,  burstiness, etc.
**It contains absolutely no ML or Neural Networks.** Every metric it outputs is mathematically explainable, reproducible, and verifiable. It runs locally on your CPU, ensuring total privacy for all sensitive documents. 

---
## Why Fresnel?

For Novelists & Screenwriters: Eliminate sections of the text that don't feel as lively. Don't just guess that Chapter 10 feels slow but see the mathematical proof that your sentence variance dropped by 40% and your pacing stalled. Fix structural issues before an agent rejects you.

For Editors & Publishers: Objectivity is your best defense. Instead of telling a client their writing feels "repetitive," show them the Entropy Score proving their vocabulary has degraded over the last 50 pages. Turn subjective feedback into actionable data.

For Legal & Academic Privacy: You cannot upload sensitive IP, NDAs, or unreleased manuscripts to ChatGPT. Fresnel runs 100% offline on your machine. You get deep insights such as authorship verification, ghostwriter detection, and consistency checks.
## Key Features

Fresnel decomposes text into a few main layers:

### I. The Stylometric Fingerprint
* **Shannon Entropy Score:** Measures the complexity and randomness of word choice. High entropy indicates complex, unpredictable thought patterns.
* **Lexical Diversity (TTR):** Visualizes "cognitive fatigue" by tracking vocabulary degradation over time.
* **Burstiness Index:** Calculates the standard deviation of sentence lengths to score narrative pacing and flow (monotone vs. dynamic).

### II. Psycholinguistic Profiling
* **Sensory Immersion:** Quantifies the density of Visual, Auditory, and Tactile language to measure writing.
* **Ego Graphing:** Tracks the ratio of *I/Me* vs. *We/Us* pronouns to detect narcissism or collective focus.
  
### III. Structural Network 
* **Ghostwriter Detection:** Uses Cosine Similarity on function word vectors to detect if, for example, Chapter 5 was written by the same person as Chapter 1.

---

## Tech Stack

* **Language:** Python 3.8+
* **Core Libraries:**
    * `math` (Statistical formulas & Entropy)
    * `re` (Regex)
    * `collections` (Frequency mapping & Probability distributions)
    * `statistics` (Variance & Standard Deviation)

---

## Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone 
    cd fresnel
    ```

2.  **Run the analyzer**
    No complex environment setup required. It runs out of the box with standard libraries.
    ```bash
    python main.py
    ```

3.  **Input your text**
    Enter the path to your file OR drag and drop your file. 

---

## The Roadmap ahead

I intend to keep adding new features to Fresnel. The goal is to enable it to unlock deep insights into texts. Everything's going to be implemented incrementally but there's no fixed
timeline since I'll be working on Fresnel while juggling uni. On that note, the features I aim to implement next are:
1. Implement a few more evaluation insights such as features that assess too much use of adverbs as 'crutches' and points out where they should be replaced with better sounding words, etc.
2. A proper GUI or TUI at the very least.
3. Interactive graphs or aligned features to visualise the characteristics (using d3.js perhaps)
