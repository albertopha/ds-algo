function combinationSum(candidates: number[], target: number): number[][] {
    if (!candidates.length) return [];
    
    const cands = candidates.sort((a,b) => a - b);
    const combinations = [];
    getCombination(cands, 0, target, 0, [], combinations); 
    return combinations;
};

function getCombination(candidates: number[], start: number, target: number, sum: number, combination: number[], combinations: number[][]): void {
    if (start >= candidates.length || sum > target) return;
    if (sum === target) {
        combinations.push([...combination]);
        return;
    }

    for (let i = start; i < candidates.length; i++) {
        const currSum = sum + candidates[i];
        if (currSum > target) return;
        combination.push(candidates[i]);
        getCombination(candidates, i, target, currSum, combination, combinations);
        combination.pop();
    }
};
