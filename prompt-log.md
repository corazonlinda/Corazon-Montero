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

## 2026-09-21 — Perfect Competition: Stage 3 analysis, figures, and memo

Claude checked the numbers in all four sections of my Stage 3 analysis against my model and found that the shadow prices I originally used for carrots and mesclun came from the standalone crop schedules instead of re-optimizing the entire farm. Claude recreated the optimization in Python and confirmed the same solution as my workbook of about 10 tomato beds, 20 carrot beds, and 30 mesclun beds, with a profit of $42,775.17. The model was then re-run with each crop limit increased by one bed, which gave corrected values of about $353 for carrots and $247 for mesclun. I used those corrected numbers to rewrite Section 2 in my own words. Claude also found that the marginal costs for carrots and mesclun briefly rise above their prices before dropping again, and I revised Section 4 to explain that pattern. Claude generated three MC-vs-price figures using data from my workbook, which I reviewed for my analysis. For the memo, Claude helped guide me through each of the three required parts by asking questions, and I used my answers to develop the final recommendation.

**Reflection:**

While working through Stage 3 I learned that it is important to understand where the numbers in a model are actually coming from rather than assuming that a number is correct just because the calculation looks correct. The biggest issue I ran into was with the shadow prices for carrots and mesclun. At first, I was using $405.63 and $280, but with Claude's help, I realized those numbers came from the standalone crop schedules and did not represent what would happen if the entire farm was re-optimized. Claude recreated the model in Python and found values of about $353 for carrots and $247 for mesclun. I compared those results with my workbook and reviewed the calculations before using them to revise my analysis. Claude also helped me notice patterns in the marginal-cost curves that I had missed and generated the figures from my workbook data. What I learned most from this process is that using AI still requires me to question the results and understand what they mean. A calculation can be mathematically correct but still answer the wrong question. This stage helped me be more cautious about checking the numbers and the interpretation of them.

## 2026-10-09 — Individual Research Paper: Dakota Access Pipeline

**Tool:** Claude

**Prompt:** I asked Claude to help me research the Dakota Access Pipeline and the potential financial consequences of an oil spill near the Standing Rock Sioux Tribe. I needed help finding reliable sources, understanding the Environmental Impact Statement (EIS), checking my calculations, and organizing my research into a brief that answered Adam's five questions.

**Outcome:**

Claude helped me work through the EIS by finding information about the probability of an oil spill, possible environmental damages, and who would be financially responsible if a spill occurred. It also helped me locate the pages where the information came from so I could check the original sources myself.

Claude suggested using the costs of previous oil spills to estimate how much a major spill at Lake Oahe could potentially cost. It converted the Kalamazoo spill's reported volume of nearly 3 million liters into barrels and estimated a cost of approximately $55,000 per barrel. I used this estimate, along with the Yellowstone spill comparison, to calculate a possible range of damages. I also worked through the expected loss calculations and compared the estimated damages with the previously identified $725.7 million federal liability limit.

While reviewing my research, I found that some of the information needed to be corrected. Claude initially provided a link to an Army Corps webpage that did not work. It also pointed out that the 37,207-year return period included releases of all sizes and directed me to Table 3.1.4-2 in the EIS. I checked the table in the original PDF and confirmed that 5,774,148 years was the design-adjusted return period for a release exceeding 10,000 barrels. I added this information as Row 23 in my research notes and revised my expected loss calculations.

Another important correction involved the Standing Rock Sioux Tribe's water supply. Claude initially described the tribe's drinking water as being exposed to a potential spill. After reviewing the EIS, we found that the modeling did not predict an impact on the tribe's drinking-water intake within the 10-day period. However, the EIS did identify possible impacts on the tribe's agricultural water intakes. I changed my brief to make sure it accurately reflected these findings.

Claude also reviewed my drafts and helped me identify areas that needed improvement. It pointed out that Question 3 was one of my weakest sections because I had not calculated the spill size at which the estimated damages would exceed the liability figure. It also suggested that I include a specific minimum amount of financial assurance in Question 5 instead of making a general recommendation. I used this feedback to rewrite both sections in my own words.

I reviewed all 26 research findings against the original documents and websites and checked the calculations used in my brief. I wrote my responses to Adam's five questions and decided on my recommendation that the Army Corps should require independently verified financial assurance from DAPL. I also included an opposing argument and decided that I would revisit my recommendation by October 2027 if new evidence became available.

After completing my research brief, I asked Claude to commit it to my GitHub repository under docs/briefs/2026-10-09-research-brief.md.

**What I accepted, changed, or rejected:**

**Accepted:** Claude's suggestion to use previous oil spills to estimate potential damages per barrel, including its conversion of the Kalamazoo spill volume from liters to barrels. I also used its help locating information in the EIS, reviewing my drafts, and identifying areas that needed more evidence or calculations.

**Changed:** I corrected the spill probability used in my expected loss calculations after confirming the information in the EIS. I also revised the discussion about Standing Rock's water supply, added a break-even calculation to Question 3, and included a specific financial assurance recommendation in Question 5.

**Rejected:** I did not use the incorrect Army Corps link or keep the original wording suggesting that the tribe's drinking-water intake was expected to be affected.

**Reflection:**

One thing I learned from this assignment is that I cannot automatically assume the information AI gives me is correct, even when it sounds convincing. There were several times when Claude provided information that seemed accurate, but when I checked the original documents, I found mistakes or details that needed to be further explained. The biggest example was the difference between the probability of any oil spill and the probability of a spill exceeding 10,000 barrels. Using the wrong number would have changed my calculations and the argument I was making.

I also learned how important it is to read the original source instead of relying only on an AI summary. The information about Standing Rock's drinking-water intake and agricultural intakes made me realize that small differences in wording can completely change how an issue is presented. I found Claude helpful for finding information and explaining calculations, but I still needed to check the evidence and make my own decisions about what to include. Next time, I want to check the original sources earlier in the research process instead of building my argument around information that I have not confirmed. Moving forward, I want to continue using AI as a research tool while making sure I understand and verify the information before using it in my assignments.
