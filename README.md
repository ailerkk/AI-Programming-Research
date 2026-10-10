# The Impact of Generative AI Assistance on Programming Learning Effectiveness Among Undergraduate Students

## Authors
- Yerkindik Ailen
- Aitkali Dariga

## 1. Project Overview

This research examines how generative AI assistance affects programming learning among undergraduate students.

The study focuses on programming task performance, completion time, understanding of programming concepts, and independent problem-solving skills.

Three learning conditions are considered:

- Group A: Programming without AI assistance.
- Group B: Programming with AI-generated hints and explanations.
- Group C: Programming with direct AI-generated solutions.

The main goal is to understand which type of AI assistance supports effective programming learning.

## 2. Research Questions

**RQ1:** How does access to generative AI during programming exercises affect students' task performance and completion time compared with learning without AI?

**RQ2:** How does the use of generative AI during programming practice affect students' understanding and retention when AI assistance is later removed?

**RQ3:** Which type of AI support, explanations and hints or direct solution generation, leads to better independent programming performance?

## 3. Research Methodology

**Research Type:** Quantitative Research

The study uses a quantitative approach to compare programming performance under different AI assistance conditions.

The independent variables are AI access and type of AI assistance.

The dependent variables include programming task scores, completion time, programming errors, and independent task performance.

Controlled variables include programming language, task difficulty, time limits, learning materials, and evaluation criteria. Prior programming experience will be measured and considered during analysis.

## 4. Hypotheses

**H0:** There is no statistically significant difference in independent programming performance between the compared AI assistance conditions.

**H1:** Students receiving AI-generated hints and explanations achieve higher independent programming performance than students receiving direct AI-generated solutions.

## 5. Evaluation Metrics

| Metric | Description | Unit |
|---|---|---|
| Independent Task Score | Percentage of passed test cases without AI | % |
| Completion Time | Time required to complete a programming task | Minutes |
| Concept Test Score | Percentage of correct answers | % |
| Programming Errors | Number of recorded programming errors | Count |
| Valid Results Rate | Percentage of correctly processed records | % |

**Primary Metric:** Independent Programming Task Score (%).

**Baseline:** Students completing programming exercises without AI assistance.

## 6. Repository Structure

```text
AI-Programming-Research/
├── README.md
├── LICENSE
├── .gitignore
├── Dockerfile
├── requirements.txt
├── src/
│   └── benchmark.py
├── data/
│   └── sample/
│       └── sample_results.csv
├── configs/
│   └── config.yaml
└── docs/
    └── Methodology_Passport_Card.pdf
```

## 7. System Requirements

- Python 3.11
- Docker (recommended)
- Git
- Windows, Linux, or macOS
- Internet connection for the initial setup

## 8. Quickstart Guide

After all project files are added, the benchmark can be executed using Docker:

```bash
docker build -t ai-programming-research .
docker run --rm ai-programming-research
```

The benchmark will read the sample dataset, calculate performance metrics, and print the results.

## 9. Planned Benchmark Results

| Group | Independent Task Score (%) | Completion Time (min) |
|---|---|---|
| No AI | To be measured | To be measured |
| AI Hints | To be measured | To be measured |
| AI Solutions | To be measured | To be measured |

These are planned measurements, not actual experimental results.

## 10. Citation and License

This project is developed for the Research Methods course.

Authors: Yerkindik Ailen and Aitkali Dariga.

License: MIT License.

## 11. Project Status

Task 2 — Methodology and benchmark pipeline preparation.

The initial benchmark will be tested using a small sample dataset before collecting research data.
