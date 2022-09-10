

// This is a JavaScript coding problem from BFE.dev 

/**
 * @param {HTMLElement} root
 * @param {HTMLElement} target
 * @return {string}
 */
function generateSelector(root, target) {
  if (root === null || root === target) {
    return getTagName(root);
  }

  if (target.hasAttribute("id")) return `#${target.getAttribute("id")}`;
  
  const selector = [];
  while (target !== null && target !== root) {
    selector.push(getTagName(target));
    target = target.parentElement;
  }
  return selector.reverse().join(" > ");
}

function getTagName(node) {
  if (node === null) return "";
  return node.tagName.toLowerCase();
}
