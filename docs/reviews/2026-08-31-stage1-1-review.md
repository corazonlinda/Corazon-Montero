<!-- PR TARGET: https://github.com/corazonlinda/Corazon-Montero | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief

**Not yet submitted. Held; the deadline has not passed.**

> Checked 2026-08-31. There is no Stage 1.1 brief in your repository — docs/briefs/ exists and holds only its README — and no submission in Lamaku. Nothing is recorded. You appeared on my roster for the first time in the 31 August export, so this is your first feedback from me on this stage; read it as an orientation rather than a scolding.

### Read the stage 0 feedback alongside this one

Your repository is in reasonable shape — the skeleton is mostly there and your .gitignore is correct — so this brief has somewhere to land. The one thing worth doing first is replacing the placeholder bio in README.md, because that is a thirty-minute job that is currently costing more than anything else in your portfolio. Details in the Stage 0 comment.

### What this stage asks for

About a page at docs/briefs/perfect-competition-brief.md, in your own words, committed before you build anything.

The reason it comes before the model, and the reason it is graded on its own: a prediction written before the model runs can be proven wrong. The same sentence written afterwards is a summary of the output, and it teaches you nothing, because you can no longer tell "I understood the economics" from "I read the answer cell." Stage 3 asks you to compare what you predicted against what the model found, and that comparison cannot be reconstructed later. A wrong hypothesis, precisely reasoned, is worth as much as a correct one and considerably more than a lucky one.

- State the problem in your own words. What the farm is deciding, what is fixed, what you choose, what limits the choice, and what it costs to decide badly. Restating is not copying — if you cannot say it differently from the case page, you do not have it yet.

- Name a specific mix. Three real bed counts: I expect X tomato beds, Y carrot beds, Z mesclun beds. Not a range, not percentages, not "a balanced mix."

- Say why, using the numbers the case gives you.

- Say how you would know you were wrong. Two or three named outcomes. This is where most of this cohort loses points, so write it carefully: "if the model shows a different mix" is true of every hypothesis ever written and tests nothing.

### The case, in short

A market garden has 64 beds — four plots of 16 — and a 36-week season. Fixed costs are $20,000. The farmer earns $50,000 and spends half her time in the field, which works out to 720 field hours at an implied $34.72 an hour. She can hire up to four temporary workers at $25,000 each for up to 1,440 hours, an implied $17.36 an hour.

- Tomatoes — max 20 beds, $8,800 per bed, 2.50 labor hours per bed per week, $880 fertilizer per bed, 10.00% diminishing returns per bed

- Carrots — max 20 beds, $2,094 per bed, 0.833 labor hours per bed per week, $440 fertilizer per bed, 2.50% per bed

- Mesclun — max 30 beds, $2,700 per bed, 1.25 labor hours per bed per week, $880 fertilizer per bed, 1.25% per bed

The farm cannot influence prices — it takes what the market gives, which is what makes this perfect competition. The caps sum to 70 against 64 beds, so all three cannot be maxed and something has to give.

The mechanism that decides it is that labor compounds: the hours for q beds of a crop are q x hours-per-bed-per-week x 36 x (1 + rate) to the power of q. So each additional bed raises the labor requirement for every bed of that crop, not just the new one. That is why the crop earning the most per bed also gets expensive fastest, and the question is where those two things cross.

### Where you stand, and what i would do about it

Most of this cohort has finished this stage and several are into Stage 1.2, the specification and the Excel model, which is due 6 September. That is a real gap and it is worth knowing about now rather than discovering later.

It is also a gap people in this cohort have closed in two or three days. The order that works: fix the README bio tonight, write this brief tomorrow, then start the specification. The brief is an hour of honest thinking, not a research project, and it has to come before the model.

If anything is blocking you — access, tooling, or the assignment itself — say so now rather than after the deadline. I would rather answer a question this week than grade a gap next week.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
