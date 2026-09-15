# Prompt Log

Running record of AI sessions that mattered — what I asked, what the tool did, what I changed or kept.

<!-- Example entry format:

## YYYY-MM-DD — [engagement name]

**Tool:** Claude
**Prompt:** [what I asked]
**Outcome:** [what it produced, what I accepted/edited/rejected]

-->
## 2026-08-29 — Stage 0 repo setup
Tool: Claude
Prompt: Asked Claude to review my portfolio repo against Adam's Stage 0 onboarding checklist and tell me what was missing.
Outcome: Claude found the repo was missing a .gitignore, BIO.md, real content in README.md and AGENTS.md, and a prompt-log.md entry. It helped me learn how to add a .gitignore. It gave me examples of BIO.md and README.md bios — I rewrote the AGENTS.md sections and the README bio myself in my own words rather than using its draft, since those need to reflect my actual preferences and background.
## 2026-08-31 — Writing AGENTS.md
Tool: Claude
Prompt: Gave Claude my own draft answers for the four AGENTS.md sections (how I want explanations, what AI may/may not draft, what must never be pasted into a model) and asked if it was viable.
Outcome: Claude confirmed three of the four sections were solid and pointed out I hadn't written anything for "what must never be pasted into a model" — I added a line about never pasting patient information, since I work in healthcare (HIPAA). I committed the final version myself.
## 2026-09-01 — Prompt log entries
Tool: Claude
Prompt: Asked Claude to help me draft real entries for this prompt log, since I only had the empty template.
Outcome: Claude drafted the entries above summarizing our actual sessions so far. I'm reviewing them before committing.


## 2026-09-08 — Perfect Competition brief and hypothesis

**Tool:** Claude
**Prompt:** I asked Claude to check my hypothesis and brief and give me critiques and suggestions of what could be better. Claude checked the math values I calculated. I asked Claude to help me explain the steps and teach me how to create a file on GitHub.
**Outcome:** The hypothesis of the optimal mix of 30 mesclun beds, 20 carrot beds, and 12 tomato beds remained the same. I added an explanation for why I used 12 tomato beds instead of more, based on the labor equation given — I expected I did not have sufficient labor hours to support a 13th tomato bed. I stated the labor values I calculated in the hypothesis.

## September 15, 2026 — Perfect Competition: Spec, Model Build, and Audit

**Tool:** Claude
**Prompt:** I asked Claude to help me review my Perfect Competition specification, build an Excel model from my completed specification, and guide me through checking and auditing the model according to the assignment requirements.
**Outcome:** I wrote all five sections of my spec.md myself, including Inputs, Structure, Calculation Logic, Validation Rules, and Outputs. Claude reviewed my work and pointed out areas that were missing or unclear, such as missing check figures, vague constraints, and a formula that could cause a division error. I used that feedback to revise my specification and committed it before the Excel workbook was created.

Claude then used my committed specification to build model.xlsx. During verification, Claude identified that my standalone marginal-cost crossing points were off by one bed. I investigated the issue and found that my original definition identified the first unprofitable bed instead of the bed immediately before marginal cost reached or exceeded price. I corrected the definition, and the model was updated so the crossing points matched the expected results of 10 tomatoes, 10 carrots, and 6 mesclun.

I set up and ran Solver myself in Excel on my Mac. I also completed the model audit myself, including the q=1 hand calculation, two different Solver starting points, Farm Profit Lab marginal-cost cross-check, error-cell scan, and formula spot-check. During the audit, I documented five findings: both Solver runs produced the same solution, my tomato marginal cost closely matched the Farm Profit Lab, I identified and corrected the crossing-point issue, I found a small GRG Nonlinear precision residue in the tomato-bed result, and I documented the small profit difference associated with the labor-cost calculations and the provided CAR_HRS = 0.833 input.

Claude helped me review my audit findings for completeness, but I performed the checks and made the final decisions about my model. I also wrote the README.md description for the Marginal Analysis capability and connected it to my Perfect Competition engagement.
