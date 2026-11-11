class Solution:
  def minimumCost(
      self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
  ) -> int:
    dual_cost = min(costBoth, cost1 + cost2)
    shared_need = min(need1, need2)
    total_cost = shared_need * dual_cost
    rem1 = need1 - shared_need
    if rem1 > 0:
      total_cost += rem1 * min(costBoth, cost1)
    rem2 = need2 - shared_need
    if rem2 > 0:
      total_cost += rem2 * min(costBoth, cost2)
    return total_cost
