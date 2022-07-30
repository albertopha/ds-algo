
// This is a React problem from BFE.dev

import React, { useCallback, useState } from 'react'

type UseArrayActions<T> = {
  push: (item: T) => void,
  removeByIndex: (index: number) => void
}

export function useArray<T>(initialValue: T[]): { value: T[] } & UseArrayActions<T> {
  const [value, setValue] = useState<T[]>([...initialValue]);
  const push = useCallback((newValue: T): void => setValue([...value, newValue]), []);
  const removeByIndex = useCallback((index: number): void => {
    if (index < 0 || index >= value.length) return;
    setValue([...value.slice(0, index), ...value.slice(index+1)]);
  }, []);
  return { value, push, removeByIndex };
}


// if you want to try your code on the right panel
// remember to export App() component like below

export function App() {
  const { value, push, removeByIndex } = useArray([1, 2, 3]);
  const [pushValue, setPushValue] = useState<number | string>('');
  const [index, setIndex] = useState<number | string>('');
  
  const onPushInputChange = useCallback((evt) => {
    if (!evt || !evt.target) return;
    const newValue = evt.target.value === '' ? '' : Number(evt.target.value);
    setPushValue(newValue);
  }, [pushValue]);

  const onIndexInputChange = useCallback((evt) => {
    if (!evt || !evt.target) return;
    const newValue = evt.target.value === '' ? '' : Number(evt.target.value);
    setIndex(newValue);
  }, [index]);

  return (
    <div>
      <div>Value: {value.join(', ')}</div>
      <form>
        <label>
          Push Value:
          <input
            onChange={onPushInputChange}
            value={pushValue === undefined ? '' : String(pushValue)}
            type="text"
          />
        </label>
        <button onClick={() => {
          if (typeof pushValue === 'number') push(pushValue);
          setPushValue('');
        }}>Push</button>
      </form>
      
      <form>
        <label>
          Remove by index:
          <input
            onChange={onIndexInputChange}
            value={String(index)}
            type="text"
          />
        </label>
        <button onClick={() => {
          if (typeof index === 'number') removeByIndex(index);
          setIndex('');
        }}>Remove</button>
      </form>
    </div>
  );
}



