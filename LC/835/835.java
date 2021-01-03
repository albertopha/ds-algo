public int largestOverlap(int[][] A, int[][] B) {
	int N = A.length;
	int maxSum = 0;
	for (int rowA = N - 1; rowA >= 0; rowA--) {
		for (int colA = N - 1; colA >= 0; colA--) {
			int startRow = rowA, startCol = colA, sum1 = 0, sum2 = 0, sum3 = 0, sum4 = 0;
			for (int rowB = 0; startRow + rowB < N; rowB++) {
				for (int colB = 0; startCol + colB < N; colB++) {
					sum1 += A[startRow + rowB][startCol + colB] & B[rowB][colB];
					sum2 += B[startRow + rowB][startCol + colB] & A[rowB][colB];
					sum3 += A[N - startRow - rowB - 1][startCol + colB] & B[N - rowB -1][colB];
					sum4 += B[N - startRow - rowB - 1][startCol + colB] & A[N - rowB -1][colB];
				}
			}
			maxSum = Math.max(maxSum, Math.max(sum1, Math.max(sum2, Math.max(sum3, sum4))));
		}
	}
return maxSum;
}
	
