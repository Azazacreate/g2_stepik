// хранение по-ссылке
const Petr = {
    age: 23,
    hobby: 'fishing'
};
const Ivan = Petr;
Ivan.skills = ['gaming on-PC']

console.log(Petr)
console.log(Ivan)
// беда. у Петра появился:тоже ключ:новый
