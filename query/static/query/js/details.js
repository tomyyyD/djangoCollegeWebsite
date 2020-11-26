const tl = gsap.timeline({defaults:{ease:'power1.out'}})

tl.to('.text', {y:'0%', duration:1, stagger:0.1})
tl.to(".intro", {y:'-100%', duration:0.8})

