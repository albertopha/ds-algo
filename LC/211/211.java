class Node {
    public Character chr;
    public boolean isWord;
    public Map<Character, Node> next;
    
    public Node(Character chr, boolean isWord) {
        this.chr = chr;
        this.isWord = isWord;
        this.next = new HashMap<Character, Node>();
    }
}

class WordDictionary {
    private Node trie;

    public WordDictionary() {
        this.trie = new Node(null, false);
    }
    
    public void addWord(String word) {
        Node node = this.trie;
        for (int i = 0; i < word.length(); i++) {
            char chr = word.charAt(i);
            
            if (!node.next.containsKey(chr)) node.next.put(chr, new Node(chr, false)); 
            node = node.next.get(chr);
        }
        node.isWord = true;
    }
    
    public boolean search(String word) {
        Node node = this.trie;
        return dfs(word, 0, node);
    }
    
    private boolean dfs(String word, int i, Node node) {
        if (i >= word.length()) return node.isWord;
        
        char chr = word.charAt(i);
        if (chr == '.') {
            for (Node nextNode: node.next.values()) {
                if (dfs(word, i+1, nextNode)) return true;
            }
        }
        return node.next.containsKey(chr) && dfs(word, i+1, node.next.get(chr));
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
