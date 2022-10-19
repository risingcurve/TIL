// function add(num1, num2) {
//   return num1 + num2
// }

// console.log(add(2, 7))



// const sub = function (num1, num2) {
// 	return num1 - num2
// }

// console.log(sub(2, 7))



const greeting = function (name = 'Anonymous') {
	return 'Hi ${name}'
}

console.log(greeting())



// 단계별로 줄이기(화살 함수)
const greeting = function (name) {
	return 'Hi ${name}'
}

// 1단계
const greeting = (name) => {
	return 'Hi ${name}'
}

// 2단계
const greeting = name => {
	return 'Hi ${name}'
}

// 3단계
const greeting = name => 'Hi ${name}'





