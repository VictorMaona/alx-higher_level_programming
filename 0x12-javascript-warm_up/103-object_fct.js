#!/usr/bin/node

// Makes object called 'myObject' and set its "type" to "object" and "value" to 12.
const myObject = {
  type: 'object',
  value: 12
};

// Show 'myObject' in its initial condition.
console.log(myObject);

// Provide'myObject' with 'incr' function that increases the 'value' attribute.
myObject.incr = function () {
  this.value++;
};

// Upon initializing 'incr' function, present the modified'myObject'.
myObject.incr();
console.log(myObject);

// After making second call to 'incr' method, show the updated'myObject'
myObject.incr();
console.log(myObject);

// After third call to 'incr' method, the updated'myObject' should be shown.
myObject.incr();
console.log(myObject);
