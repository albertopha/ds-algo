//!
package search;

public class SparseSearch {
	public static int sparseSearch(String[] sortedList, String target) {
		int start = 0;
		int end = sortedList.length;
		
		while(start <= end) {
			int half = (int) Math.floor((start + end) / 2);
			
			if(sortedList[half].equals("")) {
				int searchLow = half;
				int searchTop = half;
				
				while(searchLow >= start || searchTop <= end) {
					if(!sortedList[searchLow].equals("")) {
						half = searchLow;
						break;
					}
					
					if(!sortedList[searchTop].equals("")) {
						half = searchTop;
						break;
					}
					
					searchLow -= 1;
					searchTop += 1;
				}
				
				if(searchLow < start && searchTop > end) {
					return -1;
				}
			}
			
			int compared = compareStrings(sortedList[half], target);
			
			if (compared == 0) {
				return half;
			} else if(compared == -1) {
				start = half+1;
			} else {
				end = half-1;
			}
		}

		return -1;
	}
	
	private static int compareStrings(String a, String b) {
		int lenA = a.length();
		int lenB = b.length();
		int minLen = Math.min(lenA, lenB);
		
		if(a.equals(b)) {
			return 0;
		}
		
		for (int i = 0; i < minLen; i++) {
			if((int) a.charAt(i) == (int) b.charAt(i)) {
				continue;
			} else if((int) a.charAt(i) < (int) b.charAt(i)) {
				return -1;
			} else {
				return 1;
			}
		}
		
		return 0;
	}
	
	public static void main(String[] args) {
		String[] list = {"at", "", "", "ball", "", "car", "", "", "data", "", ""};
		int result1 = SparseSearch.sparseSearch(list, "data");
		int result2 = SparseSearch.sparseSearch(list, "car");
		int result3 = SparseSearch.sparseSearch(list, "ball");
		int result4 = SparseSearch.sparseSearch(list, "at");
		int result5 = SparseSearch.sparseSearch(list, "albert");
		
		System.out.println(result1);
		System.out.println(result2);
		System.out.println(result3);
		System.out.println(result4);
		System.out.println(result5);
	}
}