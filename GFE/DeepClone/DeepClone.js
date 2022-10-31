/**
 * @param {*} value
 * @return {*}
 */
export default function deepClone(value) {
  if (
    typeof value === 'boolean' ||
    typeof value === 'number' ||
    typeof value === 'string' ||
    !value
  ) return value;

  if (Array.isArray(value)) {
    return value.map(deepClone);
  }

  return Object.entries(value).reduce((newObject, [key, val]) => {
    newObject[key] = deepClone(val);
    return newObject;
  }, {});
}
