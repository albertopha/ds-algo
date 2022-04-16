



type IsBad = (version: number) => boolean

function firstBadVersion(isBad: IsBad) {
	// firstBadVersion receive a check function isBad
  // and should return a closure which accepts a version number(integer)
  let firstBadVersion: number = -1;
  return (version: number): number => {
    // write your code to return the first bad version
    // if none found, return -1
    if (!isBad(version)) return -1;
    if (firstBadVersion > -1) return firstBadVersion;
    return findFirstBadVersion(isBad, version);
  }
}

function findFirstBadVersion(isBad: IsBad, version: number): number {
  let l: number = 0,
      r: number = version;
  while (l <= r) {
    let m = Math.floor((l+r)/2);
    if (isBad(m)) r = m-1;
    else l = m+1;
  }
  return l;
}

