/**
 * @param {number} num
 * @return {string}
 */

/*
    ones = {
        1: "One",
        2: "Two",
        3: "Three"
    }
    |123|
    
    |12|345|
    
    |1|234|567|
    
    |1|234|567|891|
    
    ["","","Hundred","Thousand","Million","Billion"]
*/
const ones = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
};

const tens = {
    0: "",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eihty",
    90: "Ninety"
};

var numberToWords = function(num) {
    if (!Number.isInteger(num) || num < 1) {
        return (num === 0) ? "Zero" : "";
    }
    
    const prefixes = ["", "Thousand", "Million", "Billion"];
    const groups = [];
    
    let tmpNum = num;
    while (tmpNum > 0) {
        groups.push(tmpNum % 1000);
        tmpNum = Math.floor(tmpNum / 1000);
    }
    
    const result = groups.reduce((acc, group, i) => {
        if (group === 0) {
            return acc;
        }
        const converted = convertToStr(group).trim();
        const prefix = prefixes[i];
        return `${convertToStr(group)} ${prefixes[i]} ${acc}`.trim();
    }, "");
    
    return result.trim();
};

var convertToStr = function(num) {
    if (num < 10) {
        return ones[num];
    }
    
    if (num < 20) {
        return tens[num];
    }
    
    if (num < 100) {
        let str = "";
        
        // first digit
        let digit = num % 10;
        num = Math.floor(num / 10);
        str = ones[digit];
        
        // second digit
        digit = num % 10;
        str = `${tens[digit * 10]} ${str}`;
        return str.trim();
    }
    
    let str = ones[Math.floor(num / 100)];
    str = `${str} Hundred ${convertToStr(num % 100)}`;
    return str.trim();
};
