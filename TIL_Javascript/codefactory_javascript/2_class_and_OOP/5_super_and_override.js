/**
 * Super and Override
 */


class IdolModel{
  name;
  year;
  
  sayHello(){
    return `안녕하세요. ${this.name}입니다.`
  };

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}

class FemaleIdolModel extends IdolModel {
  // 노래 / 춤
  part;

  constructor(name, year, part) {
    super(name, year);
    this.part = part;
  }

  sayHello() {
    // return `안녕하세요. ${this.name}입니다. ${this.part}를 맡고 있습니다.`;
    // 다른 OOP 언어에서는 ${super.name}
    // javascript에서는 변수값을 불러올 때 super를 사용하면 안 된다.
    return `${super.sayHello()} ${this.part}를 맡고 있습니다.`
  }

}

const yuJin = new FemaleIdolModel('안유진', 2003, '보컬');
console.log(yuJin.part);

const wonYoung = new IdolModel('장원영', 2004);
console.log(wonYoung);
console.log(wonYoung.sayHello());
console.log(yuJin.sayHello());
