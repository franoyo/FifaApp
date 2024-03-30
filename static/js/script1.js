const loginAlerta=document.getElementById("see")
const logButton=document.getElementById("log-button")
let clickCount = 0;
function desplegar(event) {
    event.preventDefault()
    clickCount++;
    if (clickCount%2==0){
        loginAlerta.classList.remove("ver");
    }else{
        loginAlerta.classList.add("ver");
    }
   
}
