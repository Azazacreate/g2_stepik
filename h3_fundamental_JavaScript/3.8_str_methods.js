str = 'Hello world'
str.__proto__
console.log(
    str.toLowerCase()
    +'\n'
    +str.toUpperCase()
    +'\n'
    +str.includes('wor')    // 
    +'\n'
    +str.indexOf('wor')
    +'\n'
    +str.slice(0, 5)        // срез от-0 до-5
    +'\n'
    +str.split(' ')         // создать массив с-разделителем ' '
)
