const title = document.getElementById("title")

function sizing(){
    console.log(window.innerWidth)
    if (window.innerWidth > 1200){
        console.log("desktop")
        title.innerText = "Select a college from the list to the right"
    }else{
        console.log("mobile")
        title.innerText = "Select a college from the list below"
    }
}

window.onload = sizing()
window.addEventListener('resize', sizing)