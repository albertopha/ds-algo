function solution(A) {
  A.sort((a, b) => a - b);
  let first = 0, last = A.length - 1;
  // console.log(A)
  while (first < last) {
    if (A[first] == -A[last]) {
      return A[last];
    }

    // Applying absolute to ensure both sides have positive integers
    if (Math.abs(A[first]) < Math.abs(A[last])) {// By applying abs on both sides, it is more readable and comprehensible
      last -= 1;
    }
    else {
      first += 1;
    }
  }

  return 0;
}


console.log(solution([1,0,0,0,0,0,0,-2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,2,1]));
console.log(solution([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2]));