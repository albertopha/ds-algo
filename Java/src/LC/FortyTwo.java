// Re - stack, two pointers
public class FortyTwo {
	public int trap(int[] height) {
        return bruteForce(height);
    }
	
	public int bruteForce(int[] height) {
		int lmax = 0;
		int rmax = 0;
		int totalWater = 0;
		
		for(int i = 1; i < height.length-1; i++) {
			int curr = height[i];
			
			for (int l = 0; l < i; l++) {
				if (lmax < height[l]) {
					lmax = height[l];
				}
			}
			
			for (int r = height.length-1; r >= i; r--) {
				if (rmax < height[r]) {
					rmax = height[r];
				}
			}
			
			int minHeight = Math.min(lmax, rmax);
			totalWater += minHeight - curr;
		}
		
		return totalWater;
	}
	
	public int dp(int[] height) {
		return -1;
	}
	
	public int stack(int[] height) {
		return -1;
	}
	
	
	public static void main(String[] args) {
		FortyTwo ft = new FortyTwo();
		int[] heights = {0,1,0,2,1,0,1,3,2,1,2,1};
		int total = ft.trap(heights);
		System.out.println(total);
	}
}
