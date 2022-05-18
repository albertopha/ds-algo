/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return node;
        return cloneGraph(node, new HashMap<Integer, Node>());
    }
    
    public Node cloneGraph(Node node, Map<Integer, Node> map) {
        if (node == null) return null; 
        if (map.containsKey(node.val)) return map.get(node.val);
        
        Node cloned = new Node(node.val);
        map.put(cloned.val, cloned);
        
        ArrayList<Node> clonedAdjacentList = new ArrayList<>();
        for (Node neighbor : node.neighbors) {
            Node clonedneighbor = cloneGraph(neighbor, map);
            clonedAdjacentList.add(clonedneighbor);
        }
        cloned.neighbors = clonedAdjacentList;
        return cloned;
    }
}
