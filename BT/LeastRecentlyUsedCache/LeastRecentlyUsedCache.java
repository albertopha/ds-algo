import java.util.*;

/*
HashMap -> key: value
Recently used -> deque

*/

class Node {
    public int key;
    public int value;
    public Node prev;
    public Node next;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    private int capacity;
    private Map<Integer, Node> cache;
    private Node head;
    private Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    public int get(int key) {
        if (!this.cache.containsKey(key)) return -1;
        Node node = this.cache.get(key);
        addToTail(node);
        return node.value;
    }

    public void set(int key, int val) {
        // Remove the existing node
        if (this.cache.containsKey(key)) removeNode(this.cache.get(key));

        Node node = new Node(key, val);
        this.cache.put(key, node);
        addToTail(node);

        if (this.cache.size() > this.capacity) removeNode(this.head.next);
    }

    private void removeNode(Node node) {
        Node prevNode = node.prev;
        Node nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        this.cache.remove(node.key);
    }

    private void addToTail(Node node) {
        Node prevNode = this.tail.prev;
        prevNode.next = node;
        node.prev = prevNode;
        node.next = this.tail;
        this.tail.prev = node;
    }
}
