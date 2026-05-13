---
title: "Vanity Metrics Anti Patterns"
domain: data-science
category: data-analysis
created: 2026-05-12
updated: 2026-05-12
sources:
  - "[[raw/course-notes/sprint 1/03-ileri-seviye-kpi/transcripts/05-kpi-seciminde-kacinilmasi-gerekenler]]"
tags:
  - data-analysis
  - kpi
  - anti-patterns
  - vanity-metrics
  - goodharts-law
---

# Vanity Metrics Anti Patterns

> One-line summary: Vanity metrics look impressive but do not drive action — they flatter the team without revealing whether the business is winning; replace them with metrics that map directly to outcomes (revenue, retention, conversion) so dashboard movement triggers decisions, not just applause.

## Core Concept

A 42% email open rate sounds great. But if click-through is 1% and revenue from the campaign is zero, the open rate is meaningless. **Vanity metrics** are numbers that:

- Go up over time (or look big in absolute terms)
- Make the team feel good
- Do not correlate with business outcomes
- Lead to no decision when they move

They are the most common KPI failure mode. Replacing them with **actionable metrics** — those that map directly to revenue, retention, or growth — is the single highest-ROI KPI improvement most teams can make.

## How It Works

### Common vanity metrics and their actionable replacements

| Vanity metric | What it ignores | Actionable replacement |
|---------------|-----------------|------------------------|
| Total signups | Whether they activate | Activation rate (% who reach value) |
| Total page views | Engagement quality | Pages per session, time on page |
| Total followers | Whether they engage | Engagement rate, click-through |
| Email open rate | Whether they buy | Click-through rate, revenue per email |
| Total app downloads | Whether they use the app | DAU/MAU, day-7 retention |
| Total demos booked | Whether they convert | Demo-to-paid conversion rate |
| Likes / impressions | Business outcomes | Revenue attribution per channel |
| Cumulative customers | Whether they stay | Net retention, MRR growth |
| Number of features shipped | Whether they're used | Feature adoption rate |

Notice the pattern: vanity metrics are **absolute counts** or **shallow engagement signals**. Actionable metrics are **ratios** or **outcome-linked** numbers.

### The transcript's example — email campaign

> "Our last email campaign hit a 42% open rate. The team celebrated. I looked at clicks and revenue — clicks were low, revenue was lower. The 42% was vanity."

The fix: pair every "engagement" metric with a downstream **outcome** metric. Open rate alone is vanity; open rate + click-through + conversion + revenue tells the real story.

### Why vanity metrics persist

Despite known weaknesses, vanity metrics survive in dashboards because:

- **They flatter stakeholders**: "Our app has 1M downloads!" sounds better than "Our app has 8% day-7 retention"
- **They're easy to measure**: counting signups is trivial; measuring activation requires defining "activated"
- **They go up reliably**: cumulative metrics only grow, providing always-positive narratives
- **They predate honest reporting**: legacy dashboards never get pruned

### Goodhart's Law

> "When a measure becomes a target, it ceases to be a good measure." — Charles Goodhart

If you set a vanity metric as a team's KPI, people optimize *the metric* instead of *the outcome it was supposed to indicate*. Examples:

- Reward for "lines of code written" → bloated codebases
- Reward for "tickets closed" → tickets closed without solving the actual issue
- Reward for "new signups" → spammy lead generation that adds no real users

Senior analysts protect their team from Goodhart's Law by choosing KPIs that **cannot easily be gamed** without also moving the underlying outcome.

### The "wow, that number is big" trap

Big absolute numbers feel meaningful. They are usually not. A few transformations to detect:

- **Cumulative → per-period**: "1 million signups in 5 years" is "200K per year on average" — much less impressive if the trend is declining
- **Absolute → ratio**: "50K conversions" is meaningless without conversion rate
- **Count → cohort**: "100K active users" can hide that 90% churned in their first month if newer cohorts are smaller

When a number feels impressive but does not drive a clear decision, reframe it as a rate or cohort metric before celebrating.

### The five-question audit

For any candidate KPI, ask:

1. **What decision does this trigger when it moves?** (no answer → vanity)
2. **What's the target?** (no target → vanity)
3. **Can it go down as well as up?** (cumulative metrics rarely → vanity)
4. **Does it correlate with a business outcome we care about?** (if no historical data → suspect vanity)
5. **Can a team improve this without affecting the outcome?** (yes → Goodhart risk)

Two or more "no" answers → strong vanity candidate. Drop or replace.

### Replacing vanity metrics — the migration

The political problem: telling a stakeholder their favorite number is vanity is unpopular. The diplomatic move:

1. **Keep showing the vanity metric** alongside the actionable replacement for 1–2 quarters
2. **Show the divergence**: vanity going up while outcome stagnates is the killer chart
3. **Gradually reduce vanity metric prominence** in dashboards
4. **Eventually retire** once stakeholders accept the actionable replacement

Forcing immediate replacement causes resistance. Showing the contradiction in data forces honest re-evaluation.

### The opposite trap — over-correction

Some teams over-correct by tracking only revenue. This loses diagnostic signal: when revenue drops, you cannot tell *why* without the supporting metrics. The right architecture:

- 1 headline outcome KPI per team
- 5–10 supporting metrics that diagnose movement
- 0 pure vanity metrics

The supporting metrics are not vanity *if* they are causally upstream of the KPI. CAC is not vanity even though it does not directly equal revenue, because lower CAC drives higher LTV/CAC ratio (an outcome).

## Key Parameters

- **Outcome linkage required**: every metric on a dashboard should plausibly cause or predict an outcome
- **Pair engagement with conversion**: every "they did X" metric paired with "and then converted to Y"
- **Cohort analysis**: time-segmented views reveal patterns that absolute numbers hide ([[Cohort Analysis]])
- **Annual dashboard audit**: prune vanity metrics every year minimum
- **Goodhart's Law defenses**: choose metrics that can't be easily decoupled from the outcome

## When To Use

- **New KPI design**: filter every candidate through the five-question audit
- **Dashboard audit**: review existing dashboards quarterly; retire vanity metrics
- **Cross-team disputes**: when teams cite contradictory numbers, vanity vs actionable is often the gap
- **Pre-investor presentations**: founders pitching "huge user base" without retention numbers is a classic vanity tell
- Anti-pattern: presenting only cumulative absolute numbers in stakeholder meetings
- Anti-pattern: KPI lists that have no recently-modified entries — they have not been audited

## Connections

- Related: [[KPI Fundamentals]] (the basic concept), [[KPI by Team and Function]] (team-specific KPI design), [[KPI by Business Model]] (context-aware selection), [[Cohort Analysis]] (the antidote to many vanity patterns)
- Builds on: critical thinking about causation vs correlation
- Compare with: "actionable metrics" framework (Lean Startup methodology), HEART (Google's Happiness/Engagement/Adoption/Retention/Task-success framework)
- Used by: every dashboard owner; every senior analytics leader

## My Notes

- The most painful conversation in analytics is telling a founder their favorite number is vanity. Do it anyway. The data team's credibility depends on it.
- Practice: [Amazon Books CRM Raporu](https://nextgen.workintech.com.tr/project/201/4?pid=7283) — audit a real dashboard, label each metric as vanity or actionable, propose replacements.
- A useful tool: the "vanity tag" — every metric in your dashboard catalog labeled green (actionable), yellow (suspect), red (vanity). Forces explicit categorization.
- Interview tip: when asked about KPI design, naming Goodhart's Law explicitly signals senior thinking. Many candidates know "vanity metrics"; fewer know the formal principle behind why metrics-as-targets break.
