 Sual 1:let, const və var arasındakı fərqləri izah edin


var: Funksiya içərisindəki dəyişkən 


let: Block içərisindəki dəyişkən


const: Block içərisindəki dəyişkən (sabit dəyişkən)

function funk(){

  for (var i=0; i<5 ; i++){
  
    console.log(i);
    
  }
  
  console.log(i);
  
}
 
funk();

Əgər burada var -ı let ilə əvəzləsək kodumuz error verəcək. (ReferenceError: i is not defined) Bunun səbəbi isə let dəyişkən tipi yalnız bəzəkli mötərizə {} daxilində elan olunur.

Əsas düşünməli olduğumuz “qanunlar”lar :

1.var istifadə etməyin, let və ya const daha çox spesifikdir

2.default olaraq const istifadə edin, çünki yenidən düzəliş edilə bilməz

3.əgər bir dəyişkəni yenidən düzəliş etmək istəyirsinizsə let istifadə edin

4.unutmayınki hər zaman let , var – dan daha rahatdır və const, let -dən daha rahatdır
