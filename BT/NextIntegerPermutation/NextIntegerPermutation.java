import java.util.*;

/*
123
=> 132

321
=> 123

527
=> 572

572
 ^
=> 725

63875

65873
*/
class Solution {
    public int solve(int n) {
        int[] arr = intToArr(n);
        if (arr.length <= 1) return n;

        int dropPoint = findDropPoint(arr);
        if (dropPoint >= 0) {
            int swapPoint = findSwapPoint(arr, dropPoint);
            swap(arr, dropPoint, swapPoint);
        }
        reverse(arr, dropPoint+1);
        return arrToInt(arr);
    }

    private int[] intToArr(int n) {
        String str = Integer.toString(n);
        int[] arr = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            arr[i] = Integer.parseInt(String.valueOf(str.charAt(i)));
        }
        return arr;
    }

    private int arrToInt(int[] arr) {
        int result = 0;
        int increment = 1;
        for (int i = arr.length-1; i >= 0; i--) {
            result += (arr[i] * increment);
            increment *= 10;
        }
        return result;
    }

    private void reverse(int[] arr, int startIdx) {
        if (startIdx >= arr.length-1) return;
        int lastIdx = arr.length-1;
        while (startIdx < lastIdx) {
            swap(arr, startIdx, lastIdx);
            startIdx++;
            lastIdx--;
        }
    }

    private int findDropPoint(int[] arr) {
        int idx = arr.length - 2;
        while (idx >= 0 && arr[idx] >= arr[idx+1]) idx--;
        return idx;
    }

    private int findSwapPoint(int[] arr, int dropPoint) {
        int swapPoint = dropPoint;
        for (int i = dropPoint + 1; i < arr.length; i++) {
            if (arr[i] <= arr[dropPoint]) break;
            swapPoint = i;
        }
        return swapPoint;
    }

    private void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
}
