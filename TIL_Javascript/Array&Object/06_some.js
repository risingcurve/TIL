const arr = [1, 2, 3, 4, 5]


const result = arr.find(function (elem) {
    return elem % 2 === 0
})


const result = arr.find((elem) => {
    return elem % 2 === 0
})


const result = arr.some((elem) => % 2 === 0)

console.log(result)