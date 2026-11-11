class Solution:
  def minimumCost(
      self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
  ) -> int:
    dual_cost = min(costBoth, cost1 + cost2)
    shared_need = min(need1, need2)
    total_cost = shared_need * dual_cost
    # costs min(costBoth, cost1).
    rem1 = need1 - shared_need
    if rem1 > 0:
      total_cost += rem1 * min(costBoth, cost1)

    # For any leftover requirement of type 2, buying a type 3 item or a type 2 item
    # costs min(costBoth, cost2).
    rem2 = need2 - shared_need
    if rem2 > 0:
      total_cost += rem2 * min(costBoth, cost2)

    return total_cost
