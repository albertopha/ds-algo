/**
 * @param {string} digits
 * @return {string[]}
 */
const letterCombinations = (digits)  => {
    if (!digits || typeof digits !== 'string') return [];
    
    const letters = [
        [], ['a','b','c'],['d','e','f'],
        ['g','h','i'],['j','k','l'],['m','n','o'],
        ['p','q','r','s'],['t','u','v'],['w','x','y','z']
    ];
    
    return getLetterCombinations(digits, letters, 0);
};

const getLetterCombinations = (digits, letters, index) => {
    if (index >= digits.length) return [];
    const digit = digits[index];
    const letterCollections = letters[Number(digit)-1];
    const combinations = getLetterCombinations(digits, letters, index+1);
    const newCombinations = [];
    
    if (combinations.length === 0) return letterCollections;
    
    for (const combination of combinations) {
        for (const letter of letterCollections) {
            newCombinations.push(letter + combination);
        }
    }
    return newCombinations;
};
