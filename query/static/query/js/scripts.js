const title = document.getElementById("title")

function sizing(){
    console.log(window.innerWidth)
    if (window.innerWidth > 1200){
        title.style.backgroundColor = "red";
    }else{
        console.log("mobile")
    }
}


window.onload = sizing()
window.addEventListener('resize', sizing)