import { useEffect, useMemo, useState } from 'react';

export function useSWR<T = any, E = any>(
  _key: string,
  fetcher: () => T | Promise<T>
): {
  data?: T
  error?: E
} {
  const fetchedResponse = useMemo(() => fetcher(), []);
  const isPromise = fetchedResponse instanceof Promise;
  const [data, setData] = useState<T | undefined>(isPromise ? undefined : fetchedResponse);
  const [error, setError] = useState<E | undefined>();

  useEffect(() => {
    if (fetchedResponse instanceof Promise) {
      fetchedResponse
        .then((d) => setData(d))
        .catch((error) => setError(error));
    }
  }, [fetchedResponse]);
  
  return { data, error };
}

// if you want to try your code on the right panel
// remember to export App() component like below

// export function App() {
//   return <div>your app</div>
// }


