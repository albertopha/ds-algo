
import React, { useState } from 'react'
export function PhoneNumberInput() {
  const [numberInput, setNumberInput] = useState<string>('');
  const onChange = (evt: React.FormEvent<HTMLInputElement>) => {
    if (!evt || !evt.target || typeof (evt.target as HTMLInputElement).value !== 'string') return;
    const value = (evt.target as HTMLInputElement).value;
    if (value.length === 0) {
      setNumberInput('');
      return;
    }

    const lastValue = value[value.length-1];
    if (
      value.length > 13 ||
      lastValue === ' ' ||
      (
        ![')', '-'].includes(lastValue) && 
        Number.isNaN(Number(value[value.length-1]))
      )
    ) {
      return;
    }

    if (value[value.length-1] === ')') {
      setNumberInput(numberInput.substring(1, value.length-1));
      return;
    }

    if (value[value.length-1] === '-') {
      setNumberInput(numberInput.substring(0, value.length-1));
      return;
    }

    setNumberInput(value);
  };

  const displayValue = (numberInputValue: string) => {
    if (!numberInputValue) return '';

    const lastDigit = numberInputValue[numberInputValue.length-1];
    if (numberInputValue.length === 4) {
      return `(${numberInputValue.substring(0,3)})${lastDigit}`;
    }

    if (numberInputValue.length === 9) {
      return `${numberInputValue.substring(0,8)}-${lastDigit}`;
    }

    return numberInputValue;
  };
  return <input data-testid="phone-number-input" onChange={onChange} value={displayValue(numberInput)}/>
}

// if you want to try your code on the right panel
// remember to export App() component like below

// export function App() {
//   return <div>your app</div>
// }
