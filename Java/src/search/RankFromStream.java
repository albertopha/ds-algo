// ! BST
package search;

import java.util.ArrayList;
import java.util.List;

public class RankFromStream {
	private List<Rank> sorted = new ArrayList<Rank>();
	
	public List<Rank> getSorted() {
		return sorted;
	}

	public void track(int x) {
		int newRank = 0;

		if (sorted.size() == 0) {
			sorted.add(new Rank(x, newRank));
			return;
		}

		for (int i = 0; i < sorted.size(); i++) {
			int currRank = sorted.get(i).getValue();
			if (currRank < x && i == sorted.size()-1) {
				sorted.add(new Rank(x, newRank));
			}
			else if (currRank < x) {
				newRank = sorted.get(i).getRank() + 1;
			} else if (currRank > x) {
				sorted.add(i, new Rank(x, newRank));

				// adjust rest of the list:
				adjustList(i+1);
				break;
			} else {
				sorted.get(i).setRank(sorted.get(i).getRank() + 1);
				adjustList(i+1);
				break;
			}
		}
	}
	
	private void adjustList(int start) {
		for (int j = start; j < sorted.size(); j++) {
			sorted.get(j).setRank(sorted.get(j).getRank() + 1);
		}
	}
	
	public int getRankOfNumber(int x) {
		int start = 0;
		int end = sorted.size();
		
		while (start <= end) {
			int mid = (int) Math.floor((start+end)/2);
			
			if (sorted.get(mid).getValue() == x) {
				return sorted.get(mid).getRank();
			} else if (sorted.get(mid).getValue() < x) {
				start = mid+1;
			} else {
				end = mid-1;
			}
		}
		
		return -1;
	}
	
	public static void main(String[] args) {
		RankFromStream rfs = new RankFromStream();
		int[] stream = {5, 1, 4, 4, 5, 9, 7, 13, 3};
		
		for (int i = 0; i < stream.length; i++) {
			rfs.track(stream[i]);
		}
		
		System.out.println(rfs.getSorted());
		System.out.println(rfs.getRankOfNumber(1));
		System.out.println(rfs.getRankOfNumber(3));
		System.out.println(rfs.getRankOfNumber(4));
		System.out.println(rfs.getRankOfNumber(9));
		System.out.println(rfs.getRankOfNumber(13));
	}
}
