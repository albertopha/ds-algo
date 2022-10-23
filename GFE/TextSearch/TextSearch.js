/**
 * @param {string} string
 * @param {string} query
 * @return {string}
 */
export default function textSearch(string, query) {
  if (!string || !query) return (!string) ? '' : string;

  const searchStr = string.toLowerCase();
  const queryStr = query.toLowerCase();
  const boldedIndices = [];

  let index = 0;
  while (index < searchStr.length) {
    index = searchStr.indexOf(queryStr, index);
    if (index === -1) break;
    adjustBoldedIndices(boldedIndices, index, index+queryStr.length);
    index += queryStr.length;
  }

  let resultStr = '';
  let boldedIndex = 0;
  while (boldedIndices.length) {
    const [startIndex, endIndex] = boldedIndices.shift();
    resultStr += string.substring(boldedIndex, startIndex);
    resultStr += `<b>${string.substring(startIndex, endIndex)}</b>`;
    boldedIndex = endIndex;
  }

  if (boldedIndex < string.length) resultStr += string.substring(boldedIndex, string.length);
  return resultStr;
}

function adjustBoldedIndices(boldedIndices, startIndex, endIndex) {
  // Checks if startIndex overlaps with the last boldedIndices
  // If not, append the new start and end indices
  const length = boldedIndices.length;
  if (length === 0 || startIndex > boldedIndices[length-1][1]) {
    boldedIndices.push([startIndex, endIndex]);
    return;
  }

  // If so, merge with the latest index pairs
  boldedIndices[length-1][1] = endIndex;
}

// console.log('test 1: ', textSearch('The Quick Brown Fox Jumps Over The Lazy Dog', 'fox'));
// console.log('test 2: ', textSearch('The Quick Brown Fox Jumps Over The Lazy Dog', 'dog'));
// console.log('test 3: ', textSearch('aaa', 'aa'));
// console.log('test 4: ', textSearch('aaaa', 'aa'));
// console.log('test 5: ', textSearch('aaaa', 'a'));
// console.log('test 6: ', textSearch('The Quick Brown Fox Jumps Over The Lazy Dog', 'fox '));
