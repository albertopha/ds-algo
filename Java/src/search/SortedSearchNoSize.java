package search;

public class SortedSearchNoSize {
	public static int sortedSearchNoSize(int[] list, int x) {
		int start = 0;
		int end = x;
		
		while (list[end] != -1 && list[end] <= x) {
			if (list[end] == x) {
				return end;
			}
			
			end *= 2;
		}
		
		while (start <= end) {
			int half = (int) Math.floor((start + end) / 2);
			
			if (list[half] == x) {
				return half;
			} else if(list[half] > x) {
				end = half-1;
			} else {
				start = half+1;
			}
		}
		
		return -1;
	}
	
	public static void main(String[] args) {
		int[] list1 = {1, 2, 3, 4, 5, 6, 7};
		int[] list2 = {1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25};
			
		int result1 = SortedSearchNoSize.sortedSearchNoSize(list1, 4);
		int result2 = SortedSearchNoSize.sortedSearchNoSize(list2, 11);
		int result3 = SortedSearchNoSize.sortedSearchNoSize(list2, 19);

		System.out.println(result1);
		System.out.println(result2);
		System.out.println(result3);
	}
}