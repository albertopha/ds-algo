


import React, { useEffect, useState, useRef, Ref } from 'react'

export function useFocus<T extends HTMLElement>(): [Ref<T>, boolean] {
  const ref = useRef<T>(null);
  const [isFocused, setIsFocused] = useState<boolean>(false);

  useEffect(() => {
    if (!ref.current) return;
    
    const targetElem = ref.current;
    const onFocus = () => setIsFocused(true);
    const onBlur = () => setIsFocused(false);
    
    targetElem.addEventListener('focus', onFocus);
    targetElem.addEventListener('blur', onBlur);

    return () => {
      targetElem.removeEventListener('focus', onFocus);
      targetElem.removeEventListener('blur', onBlur);
    };
  });

  return [ref, isFocused];
}

// if you want to try your code on the right panel
// remember to export App() component like below

export function App() {
  const [ref, isFocused] = useFocus();
  return <div>
    <input ref={ref}/>
    {isFocused && <p>focused</p>}
    {!isFocused && <p>not focused</p>}
  </div>
}


