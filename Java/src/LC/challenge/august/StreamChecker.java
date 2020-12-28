package challenge.august;

import java.util.*;

class Node {
    Character value;
    Boolean isWord;
    HashMap<Character, Node> next;

    public Node(Character value) {
        this.value = value;
        this.isWord = false;
        this.next = new HashMap<Character, Node>();
    }
}

class StreamChecker {
    final Node root = new Node(null);

    public StreamChecker(String[] words) {
        for (int i = 0; i < words.length; i++) {
            Node curr = this.root;
            String word = words[i];
            for (int j = 0; j < word.length(); i++) {
                char chr = word.charAt(j);
                Map<Character, Node> map = curr.next;
                if (!map.containsKey(chr)) {
                    map.put(chr,  new Node(chr));
                }
                curr = map.get(chr);
            }
            curr.isWord = true;
        }
    }

    public boolean query(char letter) {
        return false;
    }

    public void printTrie() {
        Queue<Node> queue = new LinkedList<>();
        queue.offer(this.root);

        while (queue.size() > 0) {
            System.out.println(queue.size());
            Node curr = queue.poll();
            System.out.println(curr.value);
            Set<Character> nextNodes = curr.next.keySet();

            for (Character next: nextNodes) {
                queue.offer(curr.next.get(next));
            }
        }
    }

    public static void main(String[] args) {
        StreamChecker streamChecker = new StreamChecker(new String[]{"cd", "f", "kl"});
        streamChecker.printTrie();
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker obj = new StreamChecker(words);
 * boolean param_1 = obj.query(letter);
 */
