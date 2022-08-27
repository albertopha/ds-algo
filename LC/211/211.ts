class Node {
    val: string;
    isWord: boolean;
    next: {[key: string]: Node};
    
    constructor(val: string) {
        this.val = val;
        this.isWord = false;
        this.next = {};
    }
}

class WordDictionary {
    trie: Node;
    
    constructor() {
        this.trie = new Node("");
    }

    addWord(word: string): void {
        let node: Node = this.trie;
        
        for (let i = 0; i < word.length; i++) {
            const char: string = word[i];
            if (!Object.hasOwnProperty.call(node.next, char)) {
                node.next[char] = new Node(char);
            }
            node = node.next[char];
        }
        node.isWord = true;
    }

    search(word: string): boolean {
        return this.searchFromNode(word, 0, this.trie);
    }

    searchFromNode(word: string, start: number, node: Node): boolean {
        for (let i = start; i < word.length; i++) {
            const char: string = word[i];
            if (char === '.') {
                return Object.values(node.next)
                    .some((nextNode) => this.searchFromNode(word, i+1, nextNode));
            }
            
            if (!Object.hasOwnProperty.call(node.next, char)) return false;
            node = node.next[char];
        }
        return node.isWord;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
