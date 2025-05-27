// https://leetcode.com/problems/cache-with-time-limit/description/

class TimeLimitedCache {
  private cache: Map<number, Array<number>>;

  constructor() {
    this.cache = new Map<number, Array<number>>();
  }

  set(key: number, value: number, duration: number): boolean {
    const exists = this.cache.has(key);
    this.cache.set(key, [value, new Date().getTime() + duration]);
    return exists;
  }

  get(key: number): number {
    if (!this.cache.has(key)) {
      return -1;
    }

    const currTime = new Date().getTime();
    const [value, expireTime] = this.cache.get(key) as Array<number>;
    if (currTime > expireTime) {
      this.cache.delete(key);
      return -1;
    }

    return value;
  }

  count(): number {
    const currTime = new Date().getTime();
    let cnt = 0;

    for (const [key, item] of this.cache.entries()) {
      if (currTime <= item[1]) {
        cnt += 1;
      } else {
        this.cache.delete(key);
      }
    }

    return cnt;
  }
}
