

const tl = gsap.timeline({defaults:{ease:'power1.out'}})

tl.to('.text', {y:'0%', duration:1, stagger:0.1})
tl.to(".intro", {y:'-100%', duration:0.8})

$(window).on('load', function(){
    if (window.innerWidth > 1200){
        $('.dataGroup').each(function(){
            $('.dataGroup').hover(
                function() {
                    //console.log($(this).next())
                    //$(this).next().css('display', "flex")
                    $(this).children('.summary').css({'opacity': "1", 'background-color':'#b7c9c9'})
                },
                function(){
                    //$(this).next().css('display', "none")
                    $(this).children('.summary').css({'opacity': "0", 'background-color':'transparent'})
                }
            )            
        })
    }else{
        $('.summary').css({'opacity': "1", 'background-color':'#b7c9c9'})
    }
})