// https://leetcode.com/problems/event-emitter/description/

type Callback = (...args: any[]) => any;
type Subscription = {
  unsubscribe: () => void;
};

class EventEmitter {
  private subscriptions: Map<string, Callback[]>;
  constructor() {
    this.subscriptions = new Map();
  }

  subscribe(eventName: string, callback: Callback): Subscription {
    this.subscriptions.set(eventName, [
      ...(this.subscriptions.get(eventName) || []),
      callback,
    ]);

    return {
      unsubscribe: () => {
        const subscriptions = this.subscriptions.get(eventName);
        if (!subscriptions) {
          return;
        }

        const i = subscriptions!.findIndex((item) => item === callback);
        this.subscriptions.set(
          eventName,
          subscriptions.slice(0, i).concat(subscriptions.slice(i + 1))
        );
      },
    };
  }

  emit(eventName: string, args: any[] = []): any[] {
    const subscriptions = this.subscriptions.get(eventName);
    if (!subscriptions) {
      return [];
    }

    return subscriptions.map((callback) => callback(...args));
  }
}
