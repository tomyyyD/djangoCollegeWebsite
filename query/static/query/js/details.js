

const tl = gsap.timeline({defaults:{ease:'power1.out'}})

tl.to('.text', {y:'0%', duration:1, stagger:0.1})
tl.to(".intro", {y:'-100%', duration:0.8})

$(window).on('load', function(){
    $('.dataGroup').each(function(){
        $('.dataGroup').hover(
            function() {
                //console.log($(this).next())
                //$(this).next().css('display', "flex")
                $(this).children('.summary').css('display', "flex")
            },
            function(){
                //$(this).next().css('display', "none")
                $(this).children('.summary').css('display', "none")
            }
        )
    })
})