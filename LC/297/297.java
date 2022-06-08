/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return null;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        String delim = "";
        StringBuilder serialized = new StringBuilder();
        
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            serialized.append(delim);
            delim = "_";
            if (node == null) {
                serialized.append("null");
                continue;
            }
            
            serialized.append(String.valueOf(node.val));
            queue.offer(node.left);
            queue.offer(node.right);
        }
        return serialized.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == null) return null;
        String[] nodeValues = data.split("_");
        TreeNode root = new TreeNode(Integer.parseInt(nodeValues[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        int i = 1;
        while (!queue.isEmpty() && i < nodeValues.length) {
            TreeNode node = queue.poll();
            TreeNode leftChild = "null".equals(nodeValues[i])
                ? null : new TreeNode(Integer.parseInt(nodeValues[i]));
            i++;
            TreeNode rightChild = (i >= nodeValues.length) || "null".equals(nodeValues[i])
                ? null : new TreeNode(Integer.parseInt(nodeValues[i]));
            i++;
            
            node.left = leftChild;
            node.right = rightChild;
            
            if (leftChild != null) queue.offer(leftChild);
            if (rightChild != null) queue.offer(rightChild);
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
