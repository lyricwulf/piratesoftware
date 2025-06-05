import { FusedPromise } from "$lib/util/fused-promise";

type Awaitable<T = void> = T | Promise<T>;

// instanceof Promise does not work. This is a workaround.
function isPromise<T>(v: any): v is Promise<T> {
  return typeof v?.then === "function";
}

export default function promiseOnce<T, Args extends unknown[]>(
  fn: (...args: Args) => Promise<T>
) {
  const promise = new FusedPromise<T>();
  let call: Awaitable<T>;
  return Object.assign(
    (...args: Args) => {
      call ||= fn(...args);
      if (isPromise(call)) {
        call.then(promise.resolve, promise.reject);
      } else {
        promise.resolve(call);
      }
      return promise;
    },
    {
      passive: promise,
    }
  );
}
