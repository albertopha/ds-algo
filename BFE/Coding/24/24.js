// complete the implementation
class PriorityQueue {
  /**
   * @param {(a: any, b: any) => -1 | 0 | 1} compare - 
   * compare function, similar to parameter of Array.prototype.sort
   */
  constructor(compare) {
    this.compare = compare;
    this.heap = [];
  }

  /**
   * return {number} amount of items
   */
  size() {
    return this.heap.length;
  }

  /**
   * returns the head element
   */
  peek() {
    return (this.heap.length) ? this.heap[0] : null;
  }

  /**
   * @param {any} element - new element to add
   */
  add(element) {
    this.heap.push(element);
    this.bubbleUp(this.heap.length-1);
    console.log(this.heap);  
  }

  /**
   * remove the head element
   * @return {any} the head element
   */
  poll() {
    if (this.heap.length === 0) return;
    this.swap(0, this.heap.length-1);
    const output = this.heap.pop();
    this.bubbleDown(0);
    return output;
  }

  /**
   * bubbles up towards the root of the heap
   * @param {number} starting index
   */
  bubbleUp(index) {
    while (
      Math.floor(index / 2) >= 0 &&
      this.compare(
        this.heap[index],
        this.heap[Math.floor(index / 2)]
      ) < 0
    ) {
      const parentIdx = Math.floor(index / 2);
      this.swap(parentIdx, index);
      index = Math.floor(index / 2);
    }
  }

  /**
   * bubbles down from the root
   * @param {number} starting index
   */
  bubbleDown(index) {
    let left = index * 2 + 1;
    let right = index * 2 + 2;

    while (
      (left < this.heap.length && this.compare(this.heap[index], this.heap[left]) > 0) ||
      (right < this.heap.length && this.compare(this.heap[index], this.heap[right]) > 0)
    ) {
      if (left < this.heap.length && this.compare(this.heap[index], this.heap[left]) > 0) {
        this.swap(index, left);
        index = index * 2 + 1;
      } else {
        this.swap(index, right);
        index = index * 2 + 2;
      }
    }
  }

  swap(idx1, idx2) {
    const tmp = this.heap[idx1];
    this.heap[idx1] = this.heap[idx2];
    this.heap[idx2] = tmp;
  }
}
