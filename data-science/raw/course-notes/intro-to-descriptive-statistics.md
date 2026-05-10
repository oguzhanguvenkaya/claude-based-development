---
title: "Course Notes: Introduction to Descriptive Statistics"
source_type: course-notes
source_url: ""
author: "Data Science Course"
domain: data-science
date_added: 2026-04-12
ingested: true
tags:
  - raw
  - data-science
  - statistics
---

# Introduction to Descriptive Statistics

## Measures of Central Tendency

### Mean (Arithmetic Average)
The sum of all values divided by the number of values. Sensitive to outliers.
- Formula: x_bar = (1/n) * sum(x_i)
- Use when: data is roughly symmetric, no extreme outliers
- Example: Average salary in a company — but can be misleading if CEO salary is included

### Median
The middle value when data is sorted. Robust to outliers.
- For odd n: middle value
- For even n: average of two middle values
- Use when: data is skewed or has outliers
- Example: Median house price is more representative than mean in most markets

### Mode
The most frequently occurring value. Can be used with categorical data.
- Unimodal: one peak
- Bimodal: two peaks (may indicate mixed populations)
- Use when: categorical data or finding most common value

## Measures of Spread

### Variance
Average of squared differences from the mean.
- Population variance: sigma^2 = (1/N) * sum((x_i - mu)^2)
- Sample variance: s^2 = (1/(n-1)) * sum((x_i - x_bar)^2)
- Bessel's correction (n-1) gives unbiased estimate for samples
- Units are squared — not directly interpretable

### Standard Deviation
Square root of variance. Same units as original data.
- sigma = sqrt(variance)
- 68-95-99.7 rule for normal distributions
- Use for: understanding typical deviation from mean

### Range
Maximum minus minimum. Simple but sensitive to outliers.

### Interquartile Range (IQR)
Q3 - Q1. Middle 50% of data. Robust to outliers.
- Q1 = 25th percentile
- Q3 = 75th percentile
- Used in: box plots, outlier detection (1.5 * IQR rule)

## Measures of Shape

### Skewness
Measures asymmetry of distribution.
- Positive skew: tail to the right, mean > median
- Negative skew: tail to the left, mean < median
- Zero skew: symmetric (like normal distribution)

### Kurtosis
Measures tail heaviness.
- Leptokurtic (k > 3): heavy tails, more outliers
- Mesokurtic (k = 3): normal distribution
- Platykurtic (k < 3): light tails, fewer outliers

## Data Visualization for Descriptive Stats
- Histogram: frequency distribution, spot shape
- Box plot: median, quartiles, outliers
- Scatter plot: relationship between two variables
- Bar chart: categorical comparisons
