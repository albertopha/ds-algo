/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */

/*
                    horse, ros
                    (4)         (2)
                 /                   |              \
            hors, ro              hors, ros      horse, ro
          /    |     \            /    |   \     /    |   \
     hor, r  hor, ro  hors, r hor, ro
        
Four options:
1. If two strings match:
    decrement both indices
2. Replace -> decrement both indices
3. Insert -> decrement word1 index
4. Delete -> decrement word2 index

            
*/
var minDistance = function(word1, word2) {
    if (typeof word1 !== "string" || typeof word2 !== "string") {
        return 0;
    }
    
    if (!word1 || !word2) {
        return (!word1) ? word2.lengh : word1.length;
    }
    
    if (word1.length > word2.length) {
        return minDistance(word2, word1);
    }
    
    const memo = new Array(word1.length).fill(-1).map((row) => new Array(word2.length).fill(-1));
    return minDistanceHelper(word1, word2, word1.length-1, word2.length-1, memo);
};

var minDistanceHelper = function(word1, word2, w1i, w2i, memo) {
    if (w1i < 0 || w2i < 0) {
        return (w1i < 0)
            ? w2i + 1
            : w1i + 1;
    }
    
    if (memo[w1i][w2i] !== -1) {
        return memo[w1i][w2i];
    }
    
    if (word1[w1i] === word2[w2i]) {
        memo[w1i][w2i] = minDistanceHelper(word1, word2, w1i-1, w2i-1, memo);
        return memo[w1i][w2i];
    }
    
    const replaced = 1 + minDistanceHelper(word1, word2, w1i-1, w2i-1, memo);
    const deleted = 1 + minDistanceHelper(word1, word2, w1i, w2i-1, memo);
    const added = 1 + minDistanceHelper(word1, word2, w1i-1, w2i, memo);
    memo[w1i][w2i] = Math.min(replaced, Math.min(deleted, added));
    return memo[w1i][w2i];
};
