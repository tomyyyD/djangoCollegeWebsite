const title = document.getElementById("title")

function sizing(){
    console.log(window.innerWidth)
    if (window.innerWidth > 1200){
        console.log("desktop")
        //title.innerText = title.innerText + " on the right."
    }else{
        console.log("mobile")
        //title.innerText = title.innerText + " below."
    }
}

window.onload = sizing()
window.addEventListener('resize', sizing) 