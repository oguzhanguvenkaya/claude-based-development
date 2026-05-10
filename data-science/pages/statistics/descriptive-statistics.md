---
title: "Descriptive Statistics"
domain: data-science
category: statistics
created: 2026-04-12
updated: 2026-04-12
sources:
  - "[[raw/course-notes/intro-to-descriptive-statistics]]"
tags:
  - statistics
  - central-tendency
  - spread
  - data-analysis
---

# Descriptive Statistics

> One-line summary: Methods for summarizing and describing the main features of a dataset using measures of central tendency, spread, and shape.

## Core Concept

Descriptive statistics reduce large datasets into interpretable summaries. They answer: "What does this data look like?" before you attempt inference or modeling. The three pillars are **central tendency** (where is the center?), **spread** (how dispersed?), and **shape** (what pattern?).

## How It Works

### Measures of Central Tendency
| Measure | Formula | Robust to Outliers? | Best For |
|---------|---------|---------------------|----------|
| **Mean** | sum(x_i) / n | No | Symmetric data |
| **Median** | Middle value (sorted) | Yes | Skewed data, outliers present |
| **Mode** | Most frequent value | N/A | Categorical data |

**Key insight:** When mean > median, data is right-skewed. When mean < median, left-skewed. When equal, roughly symmetric.

### Measures of Spread
| Measure | What It Tells You | Notes |
|---------|-------------------|-------|
| **Variance** | Average squared deviation from mean | Units are squared; sample uses n-1 (Bessel's correction) |
| **Std Dev** | Typical distance from mean | 68-95-99.7 rule for normal distributions |
| **Range** | Max - Min | Sensitive to outliers |
| **IQR** | Q3 - Q1 (middle 50%) | Robust; used for outlier detection (1.5 * IQR rule) |

### Measures of Shape
- **Skewness**: Positive = right tail, Negative = left tail, Zero = symmetric
- **Kurtosis**: Leptokurtic (>3) = heavy tails, Platykurtic (<3) = light tails

## Key Parameters

- **Bessel's correction** (n-1 vs N): Use n-1 for sample variance to get unbiased estimate
- **1.5 * IQR rule**: Values beyond Q1 - 1.5*IQR or Q3 + 1.5*IQR are potential outliers
- **68-95-99.7 rule**: For normal distributions, these percentages fall within 1, 2, 3 standard deviations

## When To Use

- **Always first**: Descriptive stats should be your first step in any data analysis (EDA)
- **Before modeling**: Understand distributions before choosing ML algorithms
- **Communication**: Summary statistics make datasets interpretable for stakeholders
- **Outlier detection**: IQR and std dev help identify anomalies before they corrupt models

## Connections

- Related: [[Data Visualization]], [[Probability Distributions]]
- Builds on: Basic arithmetic, sorting algorithms
- Compare with: [[Inferential Statistics]] (descriptive describes, inferential concludes)
- Used by: [[Exploratory Data Analysis]], [[Feature Engineering]]

## My Notes

- Mean vs Median is a classic interview question — always think about skewness
- Box plots are underrated — they show 5 statistics at once (min, Q1, median, Q3, max)
- Always check for outliers before computing mean — one extreme value can destroy your average
