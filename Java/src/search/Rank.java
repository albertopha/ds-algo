package search;

import java.util.Comparator;

public class Rank implements Comparator<Rank> {
	private int value;
	private int rank;
	
	public Rank(int value) {
		this.value = value;
		this.rank = 0;
	}

	public Rank(int value, int rank) {
		this.value = value;
		this.rank = rank;
	}
	
	public int getRank() {
		return rank;
	}
	
	public void setRank(int rank) {
		this.rank = rank;
	}
	
	public int getValue() {
		return value;
	}
	
	public boolean isValue(int value) {
		return this.value == value;
	}

	@Override
	public int compare(Rank o1, Rank o2) {
		if (o1.value < o2.value) {
			return -1;
		}
		
		if (o1.value > o2.value) {
			return 1;
		}

		return 0;
	}
}