<!-- PR TARGET: https://github.com/corazonlinda/Corazon-Montero | Stage 1.1 -->
# Stage 1.1 review — engagement brief

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/corazonlinda/Corazon-Montero/blob/main/docs/briefs/perfect-competition-brief.md)

> Graded 2026-09-07 against the brief you committed on 6 September. At every earlier pass this file did not exist, so this stage had been standing as not submitted. It arrived, and it arrived with arithmetic in it that almost nobody else attempted.

| Criterion | Where it stands |
|---|---|
| Problem restated in your own voice | This is the strongest part of the brief and it is written the way the criterion asks for. You separate three things that most briefs run together: what is outside the farmer's control, what limits her, and what she actually gets to choose. You catch the tension the whole case turns on — the crop caps total 70 against 64 beds, so not all three can be planted to their maximum — and you say why labor is not a fixed pool but something that grows as beds are added. What is still open is that nothing on the page says what it costs to decide this badly: the plan is committed once, before the season, with no chance to correct it in week eight. |
| Hypothesis names a specific mix | 30 mesclun, 20 carrot, 12 tomato. Three whole numbers, every one inside its own cap, 62 of the 64 beds used, and the two beds you leave fallow are deliberate rather than left over. The frontmatter carries the same numbers as the body. Nothing to add. |
| Economic mechanism | You did the arithmetic, and I checked it against my own model: 30 mesclun, 20 carrot and 12 tomato beds require 6,332 hours against the 6,480 available, and a thirteenth tomato bed takes the requirement to 6,982. Both figures are right to the hour. Very few briefs in this cohort computed anything at all, and yours computes the exact quantity your prediction rests on. What holds the criterion short of everything this criterion asks for is that the hour ceiling is the only mechanism on the page. Your argument is that the farmer stops at 12 tomato beds because a thirteenth will not fit. The question the case is really built around is the other one: does a tomato bed stop being worth planting before the hours run out? |
| Falsifiability and process | Three conditions, and the middle one is exactly the right test — if Solver finds a thirteenth tomato bed feasible, the arithmetic that produced your number is wrong, and you would know it in one glance. The third is good too: a mix that uses the same labor or less and earns more is a clean refutation. What is still open is the first one. "Any other mix than 30, 20 and 12" makes 29 mesclun beds and 4 tomato beds the same verdict, and they are not the same verdict at all. Sequence and path are clean — the brief is at the canonical path and was committed before any model existed in the repository. |

### I checked your arithmetic, and it holds

Both numbers in your hypothesis reproduce exactly against my own model of this case.

30 mesclun beds require 30 x 1.25 x 36 x 1.0125^30, which is 1,959.7 hours. 20 carrot beds require 20 x 0.8333 x 36 x 1.025^20, or 983.2. 12 tomato beds require 12 x 2.50 x 36 x 1.10^12, or 3,389.5. That totals 6,332 against a pool of 6,480 — your figure, to the hour.

The thirteenth tomato bed takes tomato hours from 3,389.5 to 4,039.2, and the farm total to 6,982. Also your figure. That is a real derivation, not a guess dressed up as one, and it is the thing that separates a brief with a mechanism from a brief with an opinion.

### The one question your mechanism does not ask

Your whole argument is a capacity argument: 12 tomato beds because 13 will not fit inside 6,480 hours. That is a legitimate reading and you have supported it properly. But it assumes the twelfth bed is worth planting, and nothing on the page tests that.

The other reading is a marginal one. A bed stops being worth planting when the extra cost of that one bed exceeds the $8,800 it brings in — and because tomato labor compounds at 10% per bed, that cost climbs fast. If the marginal cost of the eleventh or twelfth tomato bed has already passed $8,800, the farmer stops there whether or not there are hours left over, and your model will come back with unused labor.

That is not a correction and you should not touch the brief. It is the question to carry into the model: build the marginal-cost schedule for tomatoes bed by bed, find where it crosses $8,800, and then see whether the answer is set by the ceiling or by the crossing. Whichever it turns out to be, you will have a real finding to write up, and your third falsification condition already anticipates it.

### Do not edit this brief from here on

The brief is committed and dated, and from now on it is evidence rather than a draft. If your model returns something other than 30, 20 and 12, that gap is the most valuable thing you will have to write about — it is exactly what the analysis stage asks you to explain. A brief quietly revised afterwards to agree with the model has nothing left to explain.

### Where your repository stands for the next stage

Stage 1.2 is the specification and the Excel model, and there is nothing in your repository for it yet — you have capabilities/README.md but no capabilities/marginal-analysis/ folder underneath it.

The three files it wants are capabilities/marginal-analysis/spec.md, capabilities/marginal-analysis/model.xlsx, and a short README.md in the same folder. The order matters and is graded from your commit history: the specification is written and committed first, then the workbook is built from it. Two other canonical files are also still missing — analysis/README.md and docs/README.md — and each of those is one sentence saying what the folder holds.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
