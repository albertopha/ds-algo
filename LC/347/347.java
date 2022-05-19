class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if (nums.length == 0) return nums;
        return useQuickSelect(nums, k);
        // return usePriorityQueue(nums, k);
    }
    
    private int[] useQuickSelect(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if  (!counter.containsKey(nums[i])) counter.put(nums[i], 0);
            counter.put(nums[i], counter.get(nums[i])+1);
        }
        
        int[][] counts = new int[counter.size()][2];
        int i = 0;
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            Integer num = entry.getKey();
            Integer count = entry.getValue();
            counts[i++] = new int[]{count, num};
        }
        
        int[] result = new int[k];
        quickSelect(counts, 0, counts.length-1, k);
        i = 0;
        int j = counts.length-1;
        while (k-- > 0) {
            result[i++] = counts[j--][1];
        }
        return result;
    }
    
    private void quickSelect(int[][] counts, int start, int end, int k) {
        if (start >= end) return;
        int pivot = partition(counts, start, end);
        int diff = counts.length - pivot;
        if (diff == k) return;
        if (diff < k) quickSelect(counts, start, pivot - 1, k);
        else quickSelect(counts, pivot + 1, end, k);
    }
    
    private int partition(int[][] counts, int start, int end) {
        int pivot = end;
        int left = start,
            right = pivot-1;
        int pivotCount = counts[pivot][0];
        while (left <= right) {
            int leftCount = counts[left][0];
            if (leftCount <= pivotCount) left++;
            else {
                swap(counts, left, right);
                right--;
            }
        }
        swap(counts, left, pivot);
        return left;
    }
    
    private void swap(int[][] counts, int a, int b) {
        int[] temp = counts[a];
        counts[a] = counts[b];
        counts[b] = temp;
    }
    
    private int[] usePriorityQueue(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if  (!counter.containsKey(nums[i])) counter.put(nums[i], 0);
            counter.put(nums[i], counter.get(nums[i])+1);
        }
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            Integer num = entry.getKey();
            Integer count = entry.getValue();
            pq.offer(new int[]{count, num});
        }
        
        int[] result = new int[k];
        int i = 0;
        while (!pq.isEmpty() && i < k) {            
            result[i++] = pq.poll()[1];
        }
        return result;
    }
}
