class Solution:
  def minimumCost(
      self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
  ) -> int:
    
    # costs `costBoth`. Alternatively, we could buy one type 1 item and one type 2 item,
    # which costs `cost1 + cost2`. We should always take the cheaper option for dual contributions.
    dual_cost = min(costBoth, cost1 + cost2)

    # 2. To fulfill the shared requirement (the minimum of need1 and need2),
    # we can use the optimal dual items.
    shared_need = min(need1, need2)
    total_cost = shared_need * dual_cost

    # 3. Handle remaining requirements for type 1 or type 2 independently.
    # For any leftover requirement of type 1, buying a type 3 item or a type 1 item
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
