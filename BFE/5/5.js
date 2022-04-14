/**
 * @param {Function} func
 * @param {number} wait
 * @param {boolean} option.leading
 * @param {boolean} option.trailing
 */
function throttle(func, wait, option = {leading: true, trailing: true}) {
  let timer = null;
  let prevArgs = null;
  let prevContext = this;
  const {
    leading,
    trailing
  } = option;

  return (...args) => {
    if (timer) {
      prevArgs = args;
      prevContext = this;
      return;
    }

    if (leading) {
      func.apply(this, args);
    } else {
      prevArgs = args;
      prevContext = this;
    }

    const timerHandler = () => {
      if (prevArgs && trailing) {
        func.apply(prevContext, prevArgs);
        prevArgs = null;
        prevContext = null;
        timer = setTimeout(timerHandler, wait);
      } else {
        timer = null;
      }
    };
    
    timer = setTimeout(timerHandler, wait);
  };
}
