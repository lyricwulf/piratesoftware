// inspired by Rust's FusedFuture, a FusedPromise is a promise that can be
// resolved externally
export class FusedPromise<T = void> extends Promise<T> {
  resolve: (value: T | PromiseLike<T>) => void;
  reject: (reason?: any) => void;
  resolved = false;
  rejected = false;
  complete = false;
  pending = true;
  constructor(
    executor?: (
      resolve: (value: T | PromiseLike<T>) => void,
      reject: (reason?: any) => void
    ) => void
  ) {
    let res: (value: T | PromiseLike<T>) => void;
    let rej: (reason?: any) => void;
    super((resolve, reject) => {
      res = (v) => {
        this.resolved = true;
        this.complete = true;
        this.pending = false;
        resolve(v);
      };
      rej = (r) => {
        this.rejected = true;
        this.complete = true;
        this.pending = false;
        reject(r);
      };
      executor?.(resolve, reject);
    });
    this.resolve = res!;
    this.reject = rej!;
  }
  // version of contructor that returns the resolve function
  internal() {
    let resolve: (value: T | PromiseLike<T>) => void;
    let reject: (reason?: any) => void;
    const promise = new FusedPromise<T>((res, rej) => {
      resolve = res;
      reject = rej;
    });
    promise.resolve = resolveTrap;
    promise.reject = resolveTrap;
    return [promise, resolve!, reject!] as const;
  }
}

function resolveTrap() {
  throw new Error("Cannot resolve or reject an internal promise externally");
}
