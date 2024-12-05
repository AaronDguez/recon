const table = document.getElementById('trackTable');
const modal = document.getElementById('editOrderModal');
const inputs = document.querySelectorAll('.editOrderInput');
let count = 0;
let data = [];

table.addEventListener('click', (e) => {
    e.stopPropagation();
    data = e.target.parentElement.parentElement.children;
    fillData(data);
    modal.classList.toggle('show');
});

const fillData = (data) => {
    for(let index of inputs){
        console.log(index);
        console.log(data);
        // index.value = data[index.name].textContent;
    }
};