/*
[3,2,4,1]
arr.length -> 4

*/
class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return Arrays.stream(arr).boxed().collect(Collectors.toList());
        }
        
        List<Integer> list = new ArrayList<>();
        for (int i = arr.length; i > 1; i--) {
            for (int j = 0; j <= i; j++) {
                if (i == arr[j]) {
                    if (j == i-1) break;
                    if (j > 0) {
                        list.add(j+1);
                        flip(arr, 0, j);
                    }
                    list.add(i);
                    flip(arr, 0, i-1);
                }
            }
        }
        return list;
    }
    
    private void flip(int] arr, int start, int end) {
        int left = start;
        int right = end;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
}

