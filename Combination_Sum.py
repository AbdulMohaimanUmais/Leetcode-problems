def combinationSum(candidates, target):
    result = []

    def backtrack(remain_target, combinations, start):

        if remain_target == 0:
            result.append(list(combinations))
            return

        elif remain_target < 0:
            return

        for i in range(start, len(candidates)):
            combinations.append(candidates[i])
            backtrack(remain_target - candidates[i], combinations, i )
            combinations.pop()

        backtrack(target, [], 0)
        return result