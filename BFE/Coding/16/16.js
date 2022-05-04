
// please complete the implementation
class EventEmitter {
  constructor() {
    this.eventMap = new Map();
  }

  subscribe(eventName, callback) {
  	if (!this.eventMap.has(eventName)) {
      this.eventMap.set(eventName, new Set());
    }
    const cloneCallback = { callback };
    this.eventMap.get(eventName).add(cloneCallback);
    return {
      release: () => {
        this.eventMap.get(eventName).delete(cloneCallback);
        if (this.eventMap.get(eventName).size === 0) {
          this.eventMap.delete(eventName);
        }
      }
    };
  }
  
  emit(eventName, ...args) {
  	if (!this.eventMap.has(eventName)) return;
    this.eventMap.get(eventName).forEach(({ callback }) =>
      callback.apply(null, args));
  }
}
