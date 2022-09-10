/**
 * @param {any[]} args
 * @returns {string}
 */
function classNames(...args) {
  return helper(args).join(" ");
}

function helper(args) {
  return args.reduce((acc, arg) => {
    if (Array.isArray(arg)) {
      acc.push(...helper(arg));
    } else if (
      typeof arg === "string" ||
      typeof arg === "number"
    ) {
      acc.push(arg);
    } else if (typeof arg === "object" && !isFalsy(arg)) {
      acc.push(
        ...Object.keys(arg)
        .filter((key) => Boolean(arg[key]))
      );
    }
    return acc;
  }, []);
}

function isFalsy(arg) {
  return !Boolean(arg) || arg instanceof Symbol;
}

const obj = new Map([['foo', 'bar']])
obj.cool = '!'
obj.not = false
obj[Symbol()] = 'symbol'
Object.defineProperty(obj, 'hidden', {value: true})
console.log(classNames({BFE: [], dev: true, is: 3}, obj))
