---
type: spec
engagement: perfect-competition
capability: marginal-analysis
date: 2026-09-15
status: draft
---

# Marginal Analysis — Perfect Competition
## Model Specification

## Inputs

| Name | Value | Unit | Source |
|---|---|---|---|
| `TOM_PRICE` | 8800 | USD per bed | Case scenario, crop table |
| `TOM_CAP` | 20 | beds | Case scenario, crop table |
| `TOM_HRS` | 2.5 | hours per week per bed | Case scenario, crop table |
| `TOM_FERT` | 880 | USD per bed | Case scenario, crop table |
| `TOM_DIM` | 0.10 | decimal | Case scenario, crop table |
| `CAR_PRICE` | 2094 | USD per bed | Case scenario, crop table |
| `CAR_CAP` | 20 | beds | Case scenario, crop table |
| `CAR_HRS` | 0.833 | hours per week per bed | Case scenario, crop table |
| `CAR_FERT` | 440 | USD per bed | Case scenario, crop table |
| `CAR_DIM` | 0.025 | decimal | Case scenario, crop table |
| `MES_PRICE` | 2700 | USD per bed | Case scenario, crop table |
| `MES_CAP` | 30 | beds | Case scenario, crop table |
| `MES_HRS` | 1.25 | hours per week per bed | Case scenario, crop table |
| `MES_FERT` | 880 | USD per bed | Case scenario, crop table |
| `MES_DIM` | 0.0125 | decimal | Case scenario, crop table |
| `WEEKS` | 36 | weeks | Case scenario, farm table |
| `FIXED_COST` | 20000 | USD per season | Case scenario, farm table |
| `TOTAL_BEDS` | 64 | beds | Case scenario, farm table |
| `OWN_HRS` | 720 | hours | Case scenario, farm table |
| `OWN_RATE` | 34.72 | USD per hour | Case scenario, farm table |
| `MAX_WORKERS` | 4 | workers | Case scenario, farm table |
| `WORKER_HRS` | 1440 | hours per worker | Case scenario, farm table |
| `WORKER_RATE` | 17.36 | USD per hour | Case scenario, farm table |

## Structure

* **Tab 1: Inputs**
  * Purpose: Holds all 23 inputs used in the model.
  * What lives here: The inputs will be organized by tomatoes, carrots, mesclun, and overall farm information. This includes crop prices, bed caps, labor hours, fertilizer costs, diminishing-return rates, season length, fixed costs, available beds, and labor information.

* **Tab 2: Cost Structure**
  * Purpose: Calculates the labor hours and costs associated with planting each crop.
  * What lives here: Labor hours for each crop using the labor equation, fertilizer costs, the farmer's own labor hours and cost, temporary-worker hours and cost, and total labor cost. This tab will also calculate the blended labor rate (`BLENDED_RATE`) by dividing total labor dollars by total labor hours. The same blended labor rate will be applied to the labor hours for all three crops when calculating their labor costs.

* **Tab 3: Marginal Cost Schedules**
  * Purpose: Shows how the marginal cost changes as additional beds of each crop are planted.
  * What lives here: A bed-by-bed marginal-cost schedule for tomatoes, carrots, and mesclun from the first bed through each crop's bed cap. Each crop's marginal cost will be compared with its revenue per bed to identify where marginal cost approaches or reaches the crop's revenue.

* **Tab 4: Optimization**
  * Purpose: Uses Solver to find the combination of crops that produces the highest total profit while staying within the farm's limits.
  * What lives here: The number of tomato, carrot, and mesclun beds as the three changing cells, total profit as the objective cell, and the constraints for the 64 available beds, individual crop bed caps, available labor, and temporary workers. Total revenue, total costs, and profit will also be calculated here.

* **Tab 5: Checks**
  * Purpose: Makes sure the model and Solver results are working correctly before the results are used.
  * What lives here: The q=1 hand check, required check figures, checks for the bed and labor constraints, and an error-cell scan. At least one intermediate marginal-cost value will also be compared with the Farm Profit Lab as a cross-check. Solver will be run from two different starting points, 0/0/0 and 20/0/0, to verify that both starting points produce the same final solution.

## Calculation Logic

**1. Labor hours per crop**
The labor required for each crop increases as more beds are planted because of diminishing returns.
```
LABOR_HRS_TOM(q) = q × TOM_HRS × WEEKS × (1 + TOM_DIM)^q
LABOR_HRS_CAR(q) = q × CAR_HRS × WEEKS × (1 + CAR_DIM)^q
LABOR_HRS_MES(q) = q × MES_HRS × WEEKS × (1 + MES_DIM)^q
```
The three Solver changing cells are:
```
TOM_BEDS = number of tomato beds
CAR_BEDS = number of carrot beds
MES_BEDS = number of mesclun beds
```

**2. Total labor hours for the chosen farm mix**
```
TOTAL_HRS = LABOR_HRS_TOM(TOM_BEDS) + LABOR_HRS_CAR(CAR_BEDS) + LABOR_HRS_MES(MES_BEDS)
```

**3. Farmer hours used first**
The farmer's own labor will be used before temporary-worker labor.
```
FARMER_HRS_USED = MIN(TOTAL_HRS, OWN_HRS)
TEMP_HRS_USED = MAX(TOTAL_HRS - OWN_HRS, 0)
TEMP_HRS_USED ≤ MAX_WORKERS × WORKER_HRS
```

**4. Total labor dollars**
```
TOTAL_LABOR_DOLLARS = (FARMER_HRS_USED × OWN_RATE) + (TEMP_HRS_USED × WORKER_RATE)
```

**5. Blended labor rate for the farm**
One blended labor rate will be calculated for the chosen farm mix.
```
BLENDED_RATE = TOTAL_LABOR_DOLLARS ÷ TOTAL_HRS
If TOTAL_HRS = 0: BLENDED_RATE = 0
```
The same blended labor rate is applied to the labor hours for all three crops in the chosen farm mix.

**6. Labor cost per crop in the chosen farm mix**
```
LABOR_COST_TOM = LABOR_HRS_TOM(TOM_BEDS) × BLENDED_RATE
LABOR_COST_CAR = LABOR_HRS_CAR(CAR_BEDS) × BLENDED_RATE
LABOR_COST_MES = LABOR_HRS_MES(MES_BEDS) × BLENDED_RATE
```

**7. Fertilizer cost per crop**
```
FERT_COST_TOM(q) = q × TOM_FERT
FERT_COST_CAR(q) = q × CAR_FERT
FERT_COST_MES(q) = q × MES_FERT
```
At the final Solver bed counts:
```
FERT_COST_TOM = TOM_BEDS × TOM_FERT
FERT_COST_CAR = CAR_BEDS × CAR_FERT
FERT_COST_MES = MES_BEDS × MES_FERT
```

**8. Revenue per crop**
```
REVENUE_TOM(q) = q × TOM_PRICE
REVENUE_CAR(q) = q × CAR_PRICE
REVENUE_MES(q) = q × MES_PRICE
```
At the final Solver bed counts:
```
REVENUE_TOM = TOM_BEDS × TOM_PRICE
REVENUE_CAR = CAR_BEDS × CAR_PRICE
REVENUE_MES = MES_BEDS × MES_PRICE
```

**9. Standalone marginal-cost schedules**
Calculated independently of the final Solver solution. For each crop, q runs from 0 through that crop's bed cap while the other two crops are treated as having zero beds. The q = 0 row is only the zero-cost starting point needed to calculate marginal cost at q = 1. Marginal cost is only calculated from q = 1 through the crop's bed cap — no marginal-cost value at q = 0. For every value of q, the farmer's own hours are used first; temporary-worker hours are used only when the labor requirement exceeds `OWN_HRS`.

*Tomatoes*
```
STANDALONE_FARMER_HRS_TOM(q) = MIN(LABOR_HRS_TOM(q), OWN_HRS)
STANDALONE_TEMP_HRS_TOM(q) = MAX(LABOR_HRS_TOM(q) - OWN_HRS, 0)
STANDALONE_LABOR_DOLLARS_TOM(q) = (STANDALONE_FARMER_HRS_TOM(q) × OWN_RATE) + (STANDALONE_TEMP_HRS_TOM(q) × WORKER_RATE)

If LABOR_HRS_TOM(q) = 0: STANDALONE_BLENDED_RATE_TOM(q) = 0
Otherwise: STANDALONE_BLENDED_RATE_TOM(q) = STANDALONE_LABOR_DOLLARS_TOM(q) ÷ LABOR_HRS_TOM(q)

TOTAL_COST_TOM(q) = STANDALONE_LABOR_DOLLARS_TOM(q) + FERT_COST_TOM(q)

For q = 1 through TOM_CAP:
MC_TOM(q) = TOTAL_COST_TOM(q) - TOTAL_COST_TOM(q - 1)
```

*Carrots*
```
STANDALONE_FARMER_HRS_CAR(q) = MIN(LABOR_HRS_CAR(q), OWN_HRS)
STANDALONE_TEMP_HRS_CAR(q) = MAX(LABOR_HRS_CAR(q) - OWN_HRS, 0)
STANDALONE_LABOR_DOLLARS_CAR(q) = (STANDALONE_FARMER_HRS_CAR(q) × OWN_RATE) + (STANDALONE_TEMP_HRS_CAR(q) × WORKER_RATE)

If LABOR_HRS_CAR(q) = 0: STANDALONE_BLENDED_RATE_CAR(q) = 0
Otherwise: STANDALONE_BLENDED_RATE_CAR(q) = STANDALONE_LABOR_DOLLARS_CAR(q) ÷ LABOR_HRS_CAR(q)

TOTAL_COST_CAR(q) = STANDALONE_LABOR_DOLLARS_CAR(q) + FERT_COST_CAR(q)

For q = 1 through CAR_CAP:
MC_CAR(q) = TOTAL_COST_CAR(q) - TOTAL_COST_CAR(q - 1)
```

*Mesclun*
```
STANDALONE_FARMER_HRS_MES(q) = MIN(LABOR_HRS_MES(q), OWN_HRS)
STANDALONE_TEMP_HRS_MES(q) = MAX(LABOR_HRS_MES(q) - OWN_HRS, 0)
STANDALONE_LABOR_DOLLARS_MES(q) = (STANDALONE_FARMER_HRS_MES(q) × OWN_RATE) + (STANDALONE_TEMP_HRS_MES(q) × WORKER_RATE)

If LABOR_HRS_MES(q) = 0: STANDALONE_BLENDED_RATE_MES(q) = 0
Otherwise: STANDALONE_BLENDED_RATE_MES(q) = STANDALONE_LABOR_DOLLARS_MES(q) ÷ LABOR_HRS_MES(q)

TOTAL_COST_MES(q) = STANDALONE_LABOR_DOLLARS_MES(q) + FERT_COST_MES(q)

For q = 1 through MES_CAP:
MC_MES(q) = TOTAL_COST_MES(q) - TOTAL_COST_MES(q - 1)
```

At q = 0, standalone labor cost and fertilizer cost equal zero, and the marginal-cost cell is left blank because q = 0 is only a reference point.

The standalone blended rates are informational values showing the effective labor rate at each value of q — not used directly in the marginal-cost formula. Marginal cost is calculated from the change in total standalone cost between q − 1 and q.

Each crop's marginal cost is compared with its revenue per bed:
```
MC_TOM(q) compared with TOM_PRICE
MC_CAR(q) compared with CAR_PRICE
MC_MES(q) compared with MES_PRICE
```
This allows each crop's standalone P ≈ MC crossing point to be checked independently of Solver.

**Marginal-Cost Schedule Rule**
The standalone marginal-cost schedules use Option B: for each value of q, the crop's labor requirements, farmer hours, temporary-worker hours, labor dollars, and blended labor rate are recalculated independently, assuming the other two crops have zero beds. This lets the marginal-cost schedule show whether the cost of adding another bed reaches the crop's revenue per bed before or after the farm reaches its labor limit, without relying on the blended labor rate from the final Solver solution.

**Standalone Marginal-Cost Crossing Points**
```
TOM_CROSSING = first q where MC_TOM(q) ≥ TOM_PRICE
CAR_CROSSING = first q where MC_CAR(q) ≥ CAR_PRICE
MES_CROSSING = first q where MC_MES(q) ≥ MES_PRICE
```
Must use an exact first-match search, not an approximate or sorted lookup, since marginal cost is not guaranteed to increase at every bed. The calculation searches each marginal-cost schedule for the first TRUE result from `MC_X(q) ≥ X_PRICE`, and returns the corresponding q. If no crossing point is found within a crop's bed cap, the formula returns that crop's bed cap instead of an error, to prevent an expected no-crossing result from creating an `#N/A` error.

**10. Total revenue**
```
TOTAL_REVENUE = REVENUE_TOM + REVENUE_CAR + REVENUE_MES
```

**11. Total fertilizer cost**
```
TOTAL_FERT_COST = FERT_COST_TOM + FERT_COST_CAR + FERT_COST_MES
```

**12. Total variable cost**
```
TOTAL_VARIABLE_COST = TOTAL_LABOR_DOLLARS + TOTAL_FERT_COST
```

**13. Total cost**
```
TOTAL_COST = TOTAL_VARIABLE_COST + FIXED_COST
```

**14. Season profit**
```
PROFIT = TOTAL_REVENUE - TOTAL_LABOR_DOLLARS - TOTAL_FERT_COST - FIXED_COST
Equivalent form: PROFIT = TOTAL_REVENUE - TOTAL_COST
```
Solver will maximize `PROFIT` by changing `TOM_BEDS`, `CAR_BEDS`, and `MES_BEDS`.

**15. Solver constraints**
```
Individual crop bed caps:
TOM_BEDS ≤ TOM_CAP
CAR_BEDS ≤ CAR_CAP
MES_BEDS ≤ MES_CAP

Total available beds:
TOM_BEDS + CAR_BEDS + MES_BEDS ≤ TOTAL_BEDS
(total may be less than TOTAL_BEDS — Solver is not required to use all 64 beds)

Available temporary labor:
TEMP_HRS_USED ≤ MAX_WORKERS × WORKER_HRS

Nonnegative bed counts:
TOM_BEDS ≥ 0
CAR_BEDS ≥ 0
MES_BEDS ≥ 0

Integer decisions:
TOM_BEDS = integer
CAR_BEDS = integer
MES_BEDS = integer
```
Solver may choose zero beds of a crop, but cannot choose a negative or fractional number of beds.

## Validation Rules

I will use the following checks to make sure my workbook is calculating correctly before I accept the final results.

**1. Hand check at q = 1**
```
LABOR_HRS_TOM(1) = 1 × TOM_HRS × WEEKS × (1 + TOM_DIM)^1
             = 1 × 2.5 × 36 × 1.10 = 99 hours
```
The workbook passes this check if `LABOR_HRS_TOM(1)` also equals 99 hours.

**2. Farm Profit Lab cross-check**
I will use `MC_TOM(10)` as my intermediate check. The workbook passes this check if my calculated `MC_TOM(10)` is within $1.00 of the corresponding value in the Farm Profit Lab. If the difference is greater than $1.00, I will check my formulas before accepting the results.

**3. Two Solver starting points**
Run 1: `TOM_BEDS = 0, CAR_BEDS = 0, MES_BEDS = 0`
Run 2: `TOM_BEDS = 20, CAR_BEDS = 0, MES_BEDS = 0`
Both runs should end with the same values for `TOM_BEDS`, `CAR_BEDS`, and `MES_BEDS`. The final `PROFIT` from both runs should also match within $0.01. If the two runs give different crop mixes or different profit results, I will check the model before accepting the Solver solution.

**4. Published check figures**
The final crop mix should be `TOM_BEDS = 10`, `CAR_BEDS = 20`, `MES_BEDS = 30` — the workbook passes this check only on an exact match.
The published profit check figure is `PROFIT = $42,762`. My calculated `PROFIT` should match this within $0.01.
The standalone marginal-cost schedules should show crossing points near:
- Tomatoes: `MC_TOM(q) ≈ TOM_PRICE` near q = 10
- Carrots: `MC_CAR(q) ≈ CAR_PRICE` near q = 10
- Mesclun: `MC_MES(q) ≈ MES_PRICE` near q = 6

If my results are not close to these values, I will go back and check the marginal-cost formulas before accepting the results.

**5. No error cells**
No cell should show `#REF!`, `#DIV/0!`, or `#NAME?`. If any of these errors appear, I will correct them before accepting the workbook results.

**6. Formulas instead of typed-in answers**
All calculated values in my workbook (`LABOR_HRS_*`, `MC_*`, `PROFIT`, labor costs, fertilizer costs, revenue, total costs) will come from formulas that use the appropriate named ranges or calculated cells, not pasted or typed-in numbers.

**7. Constraint checks**
I will include TRUE/FALSE cells on the Checks tab confirming:
```
TOM_BEDS ≤ TOM_CAP
CAR_BEDS ≤ CAR_CAP
MES_BEDS ≤ MES_CAP
TOM_BEDS + CAR_BEDS + MES_BEDS ≤ TOTAL_BEDS
TEMP_HRS_USED ≤ MAX_WORKERS × WORKER_HRS
TOM_BEDS ≥ 0
CAR_BEDS ≥ 0
MES_BEDS ≥ 0
```
I will also check that `TOM_BEDS`, `CAR_BEDS`, and `MES_BEDS` are whole numbers. A constraint that is satisfied will show TRUE and can be formatted green; a constraint that is not satisfied will show FALSE and can be formatted red. The workbook passes this check only when all constraint-check cells show TRUE.

## Outputs

The workbook will clearly show the main results so I can see what Solver chose, how the final profit was calculated, how much labor was used, and what the marginal-cost schedules show.

**1. Decision results**
```
TOM_BEDS = final number of tomato beds
CAR_BEDS = final number of carrot beds
MES_BEDS = final number of mesclun beds
```

**2. Financial results**
```
PROFIT = final season profit
TOTAL_REVENUE = total revenue from all three crops
TOTAL_COST = total cost for the season
TOTAL_LABOR_DOLLARS = total cost of the farmer's labor and temporary-worker labor
TOTAL_FERT_COST = total fertilizer cost for all three crops
```
Labor and fertilizer costs are shown separately instead of only being folded into `TOTAL_COST`, to make it easier to see where the farm's costs are coming from and how the final profit was calculated.

**3. Labor results**
```
TOTAL_HRS = total labor hours required by the final crop mix
FARMER_HRS_USED = number of the farmer's own labor hours used
TEMP_HRS_USED = number of temporary-worker hours used
BLENDED_RATE = blended hourly labor rate for the final crop mix
```
The farmer's hours and temporary-worker hours are shown separately so it is clear that the farmer's own labor is used first and temporary labor is only used after the farmer's available hours are used.

**4. Marginal-cost schedules**
The Marginal Cost Schedules tab will show the full bed-by-bed marginal-cost schedule for each crop.
```
MC_TOM(q) for q = 1 through TOM_CAP
MC_CAR(q) for q = 1 through CAR_CAP
MC_MES(q) for q = 1 through MES_CAP
```
Each schedule will also show the crop's revenue per bed so I can compare what an additional bed earns with what that additional bed costs.

**5. Standalone crossing points**
```
TOM_CROSSING
CAR_CROSSING
MES_CROSSING
```
These labeled results (formulas defined in Calculation Logic) make it easy to see the crossing point for each crop without searching through the full marginal-cost schedules.

**6. Check results**
The Checks tab will clearly show whether the workbook passed the validation rules: the TRUE/FALSE results for each Solver constraint, the result of the q = 1 tomato labor hand check, the result of the Farm Profit Lab cross-check, the result of comparing the two Solver runs from different starting points, and the comparison between the final model results and the published check figures.
