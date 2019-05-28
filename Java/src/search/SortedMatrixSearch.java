package search;

public class SortedMatrixSearch {
	public static int[] searchMatrixSearch(int[][] matrix, int N, int M, int target) {
		int[] result = new int[] {-1, -1};
		SortedMatrixSearch.binarySearch(matrix, 0, 0, N-1, M-1, target, result);
		return result;
	}
	
	private static void binarySearch(int[][] matrix, int startN, int startM, int endN, int endM, int target, int[] result) {
		int midN = (int) Math.floor((startN + endN) /2);
		int midM = (int) Math.floor((startM + endM) /2);
		
		if (startN > endN || startM > endM) {
			return;
		}


		if (matrix[midN][midM] == target) {
			result[0] = midN;
			result[1] = midM;
		} else if (matrix[midN][midM] < target) {
			binarySearch(matrix, midN+1, startM, endN, endM, target, result);
			binarySearch(matrix, startN, midM+1, endN, endM, target, result);
		} else {
			binarySearch(matrix, startN, startM, midN-1, endM, target, result);
			binarySearch(matrix, startN, startM, endN, midM-1, target, result);
		}
	}
	
	public static void main(String[] args) {
		int[][] matrix = {
				{1, 2, 3, 4},
				{2, 3, 4, 5},
				{3, 7, 9, 9},
				{4, 8, 9, 10},
				{5, 9, 10, 12}
			};
		
		int[] result = SortedMatrixSearch.searchMatrixSearch(matrix, 5, 4, 8);
		System.out.println("row = " + result[0] + " col = " + result[1]);
		
		int[] noResult = SortedMatrixSearch.searchMatrixSearch(matrix, 5, 4, 6);
		System.out.println("row = " + noResult[0] + " col = " + noResult[1]);
		
		int[] result2 = SortedMatrixSearch.searchMatrixSearch(matrix, 5, 4, 5);
		System.out.println("row = " + result2[0] + " col = " + result2[1]);
		
		int[] result3 = SortedMatrixSearch.searchMatrixSearch(matrix, 5, 4, 9);
		System.out.println("row = " + result3[0] + " col = " + result3[1]);

	}
}
