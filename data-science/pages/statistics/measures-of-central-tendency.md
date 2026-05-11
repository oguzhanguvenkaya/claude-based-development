---
title: "Measures of Central Tendency"
domain: data-science
category: statistics
created: 2026-04-12
updated: 2026-05-11
sources:
  - "[[raw/course-notes/intro-to-descriptive-statistics]]"
tags:
  - statistics
  - mean
  - median
  - mode
  - central-tendency
---

# Measures of Central Tendency

> One-line summary: Mean, median, and mode — three ways to describe the "center" of a dataset, each with different sensitivity to outliers and data types.

## Core Concept

Central tendency answers: "What is a typical value in this dataset?" The choice between mean, median, and mode depends on data distribution, presence of outliers, and data type.

## How It Works

### Mean (Arithmetic Average)
- **Formula:** x_bar = (1/n) * sum(x_i)
- **Strength:** Uses all data points, mathematically tractable
- **Weakness:** Pulled toward outliers
- **Example:** Average salary at a company with a CEO earning 10x everyone else — mean is misleading

### Median
- **Formula:** Middle value of sorted data (average of two middle values if n is even)
- **Strength:** Robust to outliers and skewed distributions
- **Weakness:** Ignores the magnitude of extreme values
- **Example:** Median house price — much more representative in markets with luxury outliers

### Mode
- **Formula:** Most frequent value
- **Strength:** Works with categorical data, identifies peaks
- **Weakness:** May not exist (all values unique) or be ambiguous (multimodal)
- **Use cases:** Most popular product, most common category, bimodal distribution detection

## Key Parameters

- **Weighted mean:** sum(w_i * x_i) / sum(w_i) — when observations have different importance
- **Trimmed mean:** Remove top/bottom k% before computing mean — compromise between mean and median
- **Geometric mean:** (product(x_i))^(1/n) — for growth rates and ratios

## When To Use

| Situation | Best Measure | Why |
|-----------|-------------|-----|
| Symmetric data, no outliers | Mean | Uses all information |
| Skewed data or outliers | Median | Not affected by extremes |
| Categorical data | Mode | Only option for non-numeric |
| Growth rates / ratios | Geometric mean | Handles multiplicative relationships |
| Mean with outlier protection | Trimmed mean | Compromise approach |

## Connections

- Part of: [[Descriptive Statistics]]
- Related: [[Measures of Spread]] — central tendency without spread is incomplete
- Used by: [[Hypothesis Testing]] (comparing means), [[Linear Regression]] (minimizes mean squared error)
- Compare with: [[Robust Statistics]] — methods designed for outlier resistance
- Computed via: [[Sum Avg Min Max]] (AVG = mean), [[Count and Countif]] (n for the denominator), [[Group By]] + ORDER BY for mode; median uses `APPROX_QUANTILES(col, 100)[OFFSET(50)]` in BigQuery. See [[SQL Computed Data Overview]] for the broader aggregation toolkit.

## My Notes

- Quick skewness test: if mean > median → right-skewed, if mean < median → left-skewed
- In real-world data, always check both mean AND median — the gap tells you about skewness
- In SQL the trio is rarely all available natively — `AVG` is built-in, median needs an approx function, mode needs a separate GROUP BY query. See [[Select Statement]] and aggregation lessons.
