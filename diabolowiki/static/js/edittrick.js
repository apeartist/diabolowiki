var instructions = document.getElementById("instruction-container");

function instructions_addinput() {
    var input = document.createElement("input");
    console.log(instructions.childElementCount);
    input.setAttribute("type", "text");
    input.setAttribute("name", "instruction"+instructions.childElementCount);
    input.setAttribute("class", "instruction");

    instructions.appendChild(input);
}

function instructions_removeinput() {
    var input = instructions.lastElementChild;
    if (!input.getAttribute('value')) {
        input.remove();
    } else {
        alert("Please clear the field before you delete it!");
    }
}