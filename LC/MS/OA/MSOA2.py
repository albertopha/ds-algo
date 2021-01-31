function solution(A) {
  A.sort((a, b) => a - b);
  let first = 0, last = A.length - 1;

  while (first < last) {
    if (A[first] = -A[last])
      return A[last];

    if (A[first] > -A[last])
      last -= 1;
    else
      first += 1;
  }

  return 0;
}


if __name__ == "__main__":
    print('hello')