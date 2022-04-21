

/**
 * @param {any} data
 * @param {Object} command
 */
function update(data, command) {
  if (!data || !command) return;
  run(data, command);
  return data;
}

function run(data, command) {
  if (!data || !command) return;
  const isArray = Array.isArray(data);

  if (!isRunnable(command)) {
    const [key, cmd] = Object.entries(command)[0];
    run(data[key], cmd);
    return;
  }

  if ('$push' in command) {
    if (!isArray) throw new Error('not an array');
    data.push(...command.$push);
    return;
  }

  const [key, cmd] = Object.entries(command)[0];
  if ('$set' in cmd) {
    if (isArray) {
      data.splice(key, 0, cmd.$set);
    } else {
      data[key] = cmd.$set;
    }
    return;
  }

  if ('$merge' in cmd) {
    if (
      !data[key] ||
      typeof data[key] !== 'object'
    ) throw new Error('not an object');
    data[key] = {
      ...data[key],
      ...cmd.$merge
    };
    return;
  }

  if ('$apply' in cmd) {
    data[key] = cmd.$apply(data[key]);
  }
}

function isRunnable(command) {
  if (!command) return false;
  if ('$push' in command) return true;

  const cmd = Object.values(command)[0];
  return (
    '$set' in cmd ||
    '$merge' in cmd ||
    '$apply' in cmd
  );
}

const state = {
  a: {
    b: {
      c: 1
    }
  },
  d: 2
}

const newState = update(
  state, 
  {a: {b: { c: {$set: 3}}}}
)
console.log(newState);
