# /challenge — Belief Pressure Testing

## Usage
```
/challenge [domain] [topic-or-page]
```
Example: `/challenge data-science "Random Forest is always better than logistic regression"`

## Purpose
Pressure-test a wiki page's claims or a stated belief. Find counter-evidence, edge cases, and alternative perspectives using the wiki's own content and general knowledge.

## Steps

### 1. Identify the Claim
- If a wiki page is referenced, read it and extract the main claims
- If a belief is stated, clarify it precisely

### 2. Search for Counter-Evidence
- Search the wiki for contradicting information
- Check if other pages present alternative approaches
- Apply general domain knowledge for edge cases

### 3. Present the Challenge
```
## Challenge: [Claim]

### The Claim
[What the wiki/user states]

### Counter-Evidence
- [Point 1]: [source or reasoning]
- [Point 2]: [source or reasoning]

### Edge Cases Where This Breaks
- [Scenario]: [Why the claim doesn't hold]

### Nuanced View
[A more balanced perspective that accounts for both sides]

### Verdict
[Is the claim solid, partially true, or needs revision?]
```

### 4. Offer to Update
- If the wiki page needs revision: "Want me to update [[Page]] with this nuanced view?"
- If a new page is warranted: "This analysis could become its own page. Save it?"
