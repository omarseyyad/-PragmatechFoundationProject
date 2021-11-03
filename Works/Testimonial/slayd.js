

let reyler=[
    {
        basliq:'Mehdi Cefer',
        detal:'"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam quis ipsum et ante tempor imperdiet. Sed eleifend metus et nisl scelerisque, ut convallis sapien facilisis."'
    },
    {
        basliq:'Murad Qafarli',
        detal:'"Morbi et vulputate orci. Nullam in venenatis risus. Aliquam nec orci elit. Sed dapibus eleifend enim, sed imperdiet lacus eleifend quis. Nullam mollis, quam ac convallis semper."'
    }
    ,
    {
        basliq:'Murad Ceferli',
        detal:'"Cras blandit rutrum justo tincidunt iaculis. Ut purus sem, facilisis eget urna quis, commodo tempus ligula. Morbi sagittis, erat sed imperdiet mattis, libero libero sodales."'
    }
]


for(let i=0;i<reyler.length;i++){
    let btn=`<div onclick='reyYarat(reyler[${i}].basliq,reyler[${i}].detal)'></div>`
    document.querySelector('.buttons').innerHTML+=btn
}
let basliqElementi=document.querySelector('.rey-container h3')
let detalElementi=document.querySelector('.rey-container p')

let i=0;
function reyYarat(_basliq,_detal){
    basliqElementi.innerHTML=_basliq;
    detalElementi.innerHTML=_detal;
    clearInterval(reyInterval)
}

let reyInterval=setInterval(function(){


    if(i>3){
        i=0
        reyYarat(reyler[i].basliq,reyler[i].detal)
    }else{
        i++
        reyYarat(reyler[i].basliq,reyler[i].detal)
    }
},2000) 