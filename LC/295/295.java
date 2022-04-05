class MedianFinder {
    PriorityQueue<Double> maxHeap;
    PriorityQueue<Double> minHeap;

    public MedianFinder() {
        this.maxHeap = new PriorityQueue<>((x, y) -> Double.compare(y, x));
        this.minHeap = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        if (this.maxHeap.isEmpty()) this.maxHeap.offer((double) num);
        else if (num > this.maxHeap.peek()) this.minHeap.offer((double) num);
        else this.maxHeap.offer((double) num);
        balanceHeaps(this.maxHeap, this.minHeap);
    }
    
    public double findMedian() {
        if ((this.maxHeap.size() + this.minHeap.size()) % 2 == 0) {
            return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
        }
        return (this.maxHeap.size() > this.minHeap.size())
            ? this.maxHeap.peek()
            : this.minHeap.peek();
    }
    
    private void balanceHeaps(PriorityQueue<Double> larger, PriorityQueue<Double> smaller) {
        if (smaller.size() > larger.size()) {
            balanceHeaps(smaller, larger);
            return;
        }
        
        while (larger.size() - smaller.size() > 1) {
            smaller.offer(larger.poll());
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
