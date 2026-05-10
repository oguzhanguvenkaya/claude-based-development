---
title: "Measures of Spread"
domain: data-science
category: statistics
created: 2026-04-12
updated: 2026-04-12
sources:
  - "[[raw/course-notes/intro-to-descriptive-statistics]]"
tags:
  - statistics
  - variance
  - standard-deviation
  - iqr
  - spread
---

# Measures of Spread

> One-line summary: Variance, standard deviation, range, and IQR — quantify how dispersed data points are around the center.

## Core Concept

Spread (or dispersion) answers: "How much do values vary from the typical value?" Two datasets can have the same mean but wildly different spreads. Understanding spread is essential for assessing data quality, detecting outliers, and choosing appropriate models.

## How It Works

### Variance
- **Population:** sigma^2 = (1/N) * sum((x_i - mu)^2)
- **Sample:** s^2 = (1/(n-1)) * sum((x_i - x_bar)^2)
- **Bessel's correction:** Using n-1 instead of n gives an unbiased estimate of population variance from a sample
- **Problem:** Units are squared (e.g., dollars^2) — not directly interpretable

### Standard Deviation
- **Formula:** sigma = sqrt(variance)
- **Key property:** Same units as the original data
- **68-95-99.7 rule** (for normal distributions): 68% within 1 SD, 95% within 2 SD, 99.7% within 3 SD
- **Interpretation:** "The typical distance of a data point from the mean"

### Range
- **Formula:** max - min
- **Pro:** Simplest possible measure of spread
- **Con:** Uses only 2 data points, extremely sensitive to outliers

### Interquartile Range (IQR)
- **Formula:** Q3 - Q1 (75th percentile - 25th percentile)
- **Represents:** The middle 50% of data
- **Outlier detection:** Values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR are potential outliers
- **Visualized in:** Box plots

## Key Parameters

- **Coefficient of Variation (CV):** (std_dev / mean) * 100% — compare spread across different scales
- **MAD (Median Absolute Deviation):** Robust alternative to standard deviation

## When To Use

| Measure | Best For | Limitation |
|---------|----------|------------|
| Std Dev | General purpose, normal-ish data | Sensitive to outliers |
| IQR | Skewed data, outlier detection | Ignores tail behavior |
| Range | Quick sense of data extent | Only 2 data points |
| CV | Comparing spread across scales | Meaningless if mean near zero |

## Connections

- Complementary to: [[Measures of Central Tendency]] — center without spread is incomplete
- Part of: [[Descriptive Statistics]]
- Used by: [[Hypothesis Testing]] (standard error = SD / sqrt(n))
- Related: [[Box Plots]], [[Normal Distribution]]
- Applied in: [[Feature Scaling]] (standardization uses mean and std dev)

## My Notes

- Always report both central tendency AND spread — "average salary is $80K" means nothing without knowing the spread
- IQR is my go-to for initial outlier screening — the 1.5*IQR rule is simple and effective
- Variance is the foundation of so much in statistics (ANOVA, regression) — understand it deeply
