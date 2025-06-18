// https://leetcode.com/problems/design-cancellable-function/description/

function cancellable<T>(
  generator: Generator<Promise<any>, T, unknown>
): [() => void, Promise<T>] {
  let cancelled = false;
  let cancel: () => void;

  // This promise will be in pending state until
  // the cancel function is called, which then turns
  // into rejected state.
  const cancelPromise = new Promise((_, reject) => {
    cancel = () => {
      cancelled = true;
      reject("Cancelled");
    };
  });

  const processPromise = async () => {
    let next = generator.next();
    while (!cancelled && !next.done) {
      try {
        next = generator.next(await Promise.race([next.value, cancelPromise]));
      } catch (err) {
        next = generator.throw(err);
      }
    }

    return next.value;
  };

  return [cancel!, processPromise()];
}
