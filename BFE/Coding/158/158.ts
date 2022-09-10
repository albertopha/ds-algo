

function previousLeftSibling (root: Element, target: Element): Element | null {
  if (!root || !target || root === target) return null;
  if (target.previousElementSibling) return target.previousElementSibling;
  
  let depth = 0;
  let node: HTMLElement | Element | null = target;
  while (node && node !== root) {
    depth++;
    node = node.parentElement;
  }

  let queue = [root];
  while (depth-- > 0) {
    const size = queue.length;
    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      if (node) queue.push(...node.children);
    }
  }

  const targetIndex = queue.findIndex((node) => node === target);
  return (targetIndex > 0) ? queue[targetIndex-1] : null;
}

