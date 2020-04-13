class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(value) {
    if (!this.head) {
      this.head = value;
      this.tail = value;
    } else {
      this.tail.next = value;
      this.tail = value;
    }
    this.length++;
  }
}

const myLinkedList = new LinkedList();

myLinkedList.push(new Node(52));
myLinkedList.push(new Node("hi there"));
myLinkedList.push(new Node([1, 2]));
myLinkedList.push(new Node(895.58));

console.log(myLinkedList);
