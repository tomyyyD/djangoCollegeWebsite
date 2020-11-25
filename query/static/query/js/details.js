const tl = gsap.timeline({defaults:{ease:'power1.out'}})

tl.to('.text', {y:'0%', duration:1, stagger:0.25})
tl.to(".intro", {y:'-100%', duration:1})
