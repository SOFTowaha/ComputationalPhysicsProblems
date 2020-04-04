f rom v i s u a l i m p o rt ∗
i m p o rt random
random . s e e d ( None ) # Seed g e n e r a t o r , None => s y st em c l o c k
jmax = 1000
xx =yy = zz = 0. 0 # S t a r t a t o r i g i n
g r a p h 1 = d i s p l a y ( x =0 , y =0 , wi dt h = 6 0 0 , h e i g h t = 6 0 0 , t i t l e = ’3D Random Walk’ ,
f o r w a r d =( −0.6 , −0.5 , −1) )
# Curve , i t s p a r a m e t e r s and l a b e l s
p t s = c u r v e ( x= l i s t ( r a n g e ( 0 , 1 0 0 ) ) , r a d i u s = 1 0 . 0 , c o l o r = c o l o r . y ell o w )
xax = c u r v e ( x= l i s t ( r a n g e ( 0 , 1 5 0 0 ) ) , c o l o r = c o l o r . re d , p o s = [ ( 0 , 0 , 0 ) , ( 1 5 0 0 , 0 , 0 ) ] , r a d i u s = 1 0 . )
yax = c u r v e ( x= l i s t ( r a n g e ( 0 , 1 5 0 0 ) ) , c o l o r = c o l o r . re d , p o s = [ ( 0 , 0 , 0 ) , ( 0 , 1 5 0 0 , 0 ) ] , r a d i u s = 1 0 . )
za x = c u r v e ( x= l i s t ( r a n g e ( 0 , 1 5 0 0 ) ) , c o l o r = c o l o r . re d , p o s = [ ( 0 , 0 , 0 ) , ( 0 , 0 , 1 5 0 0 ) ] , r a d i u s = 1 0 . )
xname = l a b e l ( t e x t = "X" , p o s = ( 1 0 0 0 , 1 5 0 , 0 ) , box = 0 )
yname = l a b e l ( t e x t = "Y" , p o s = ( −1 0 0 , 1 0 0 0 , 0 ) , box = 0 )
zname = l a b e l ( t e x t = "Z" , p o s = ( 1 0 0 , 0 , 1 0 0 0 ) , box = 0 )
p t s . x [ 0 ] = p t s . y [ 0 ] = p t s . z [ 0 ] =0 # S t a r t i n g p o i n t
f o r i i n r a n g e ( 1 , 1 0 0 ) :
xx += ( random . random ( ) − 0 . 5 ) ∗2. # −1 =< x =< 1
yy += ( random . random ( ) − 0 . 5 ) ∗2. # −1 =< y =< 1
zz += ( random . random ( ) − 0 . 5 ) ∗2. # −1 =< z =< 1
p t s . x [ i ] = 200∗xx − 100
p t s . y [ i ] = 200∗yy − 100
p t s . z [ i ] = 200∗ zz − 100
r a t e ( 1 0 0 )
p r i n t ("This walk’s distance R =" , s q r t ( xx∗xx + yy∗yy+ zz∗zz ) )
