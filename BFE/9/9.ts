function decode(message: string[][]): string {
  if (message.length === 0 || message[0].length === 0) return '';
  const m = message.length;
  const n = message[0].length;
  const res: string[] = [];
  let row: number  = -1;
  let downwards: boolean = true;
  for (let col = 0; col < n; col++) {
    row = (downwards) ? row+1 : row-1;
    res.push(message[row][col]);
    if (row === m-1 && downwards) downwards = false;
    else if (row === 0 && !downwards) downwards = true;
  }

  return res.join("");
}


