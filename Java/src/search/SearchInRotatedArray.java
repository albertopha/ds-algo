package search;

class SearchInRotatedArray {		
	public static int searchInRotatedArray(int[] sortedArr, int target) {
		int start = 0;
		int end = 0;
		int len = sortedArr.length;
		int[] indexedArr = sortedArr.clone();
		
		for(int i = 0; i < len-1; i++) {
			if(sortedArr[i] > sortedArr[i+1]) {
				end = i;
				start = i+1;
			}
		}
		
		if(start > end) {
			int countFromEnd = 0;
			for(int count = 0; count < len; count++) {
				if(start < len) {
					indexedArr[count] = start;
					start++;
				} else {
					indexedArr[count] = countFromEnd;
					countFromEnd++;
				}
			}
		}
		
		start = 0;
		end = len-1;
		
		while(start <= end) {
			int half = (int) Math.floor((start + end) / 2);
			int curr = sortedArr[indexedArr[half]];
			
			if(curr == target) {
				return indexedArr[half];
			} else if(curr < target) {
				start = half+1;
			} else {
				end = half-1;
			}
		}
		
		return -1;
	}
	
	public static void main(String[] args) {
		int[] arr = {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14};
		int ind1 = SearchInRotatedArray.searchInRotatedArray(arr, 5);
		int ind2 = SearchInRotatedArray.searchInRotatedArray(arr, 14);
		System.out.print(ind1);
		System.out.print(ind2);
	}
}