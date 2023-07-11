/**
 * Immutable Object
 */

const yuJin = {
  name: '안유진',
  year: 2003,

  get age() {
    return new Date().getFullYear() - this.year;
  },

  set age(age) {
    this.year = new Date().getFullYear() - age;
  }
}

console.log(yuJin);