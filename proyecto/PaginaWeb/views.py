from django.shortcuts import render
from django.http import HttpResponse

#Nombre de la vista
def nombreVista(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Nombre Titulo</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
        </head>
        <body>
            <h1 class="text-center">Desde aqui puede ir el contenido!!</h1>    
        </body>
        </html>
    ''')

#CREADO POR: Mauricio Lozano
def PaginaPrincipal(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Página Principal</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            <style>
                *{ margin: 0; padding: 0; box-sizing: border-box; }
                .row {
                    margin-right: auto;
                    margin-left: auto;
                }
            </style>
            <script src="https://kit.fontawesome.com/638f505c64.js" crossorigin="anonymous"></script>
        </head>
        <body style="background-color: #fef7f7;">
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
            <div class="row">
                <div class="col-6 mt-2">
                    <div class="container-fluid" style="width: 80%;">            
                        <h2 class="text-center">Últimas Noticias</h2>
                        <div id="carouselExampleFade" class="carousel slide carousel-fade mt-3" data-bs-ride="carousel">
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/clans/41005067/8fa043dc9fcf4cb1fa04aa99ce71cb8aae072c67.png" class="d-block w-100 img-fluid" alt="Elder Ring">
                                    <div class="carousel-caption d-none d-md-block">
                                        <br><h5>Titulo Noticia</h5>
                                        <p>Descripción corta</p>
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img src="https://www.cosmocover.com/wp-content/uploads/2022/02/EN_SIFU_Standard_Edition_Key_Art_16x9-scaled.jpg" class="d-block w-100 img-fluid" alt="Sifu">
                                    <div class="carousel-caption d-none d-md-block">
                                        <h5 class="mt-5">Titulo Noticia</h5>
                                        <p>Descripción corta</p> 
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img src="https://as01.epimg.net/meristation/imagenes/2021/04/22/analisis/1619092845_591663_1619164855_noticia_normal.jpg" class="d-block w-100 img-fluid" alt="Nier">
                                    <div class="carousel-caption d-none d-md-block">
                                        <br><h5>Titulo Noticia</h5>
                                        <p>Descripción corta</p>
                                    </div>
                                </div>                
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="col-6 mt-2">
                    <h2 class="text-center">Publicaciones Destacadas</h2>
                    <div class="container-fluid d-flex justify-content-start mt-3">
                        <img src="https://www.enter.co/wp-content/uploads/2017/03/Persona-5-Protagonist-Introduction.jpg" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Persona 5">                
                        <div class="container-fluid d-flex flex-column">
                            <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p>
                        </div>
                    </div>
                    <div class="container-fluid d-flex justify-content-start mt-3">
                        <img src="https://as01.epimg.net/meristation/imagenes/2019/12/13/noticias/1576212548_456802_1576212636_noticia_normal.jpg" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Sekiro">                
                        <div class="container-fluid d-flex flex-column">
                            <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p>
                        </div>
                    </div>
                    <div class="container-fluid d-flex justify-content-start mt-3">
                        <img src="https://i.blogs.es/e6560e/f4c4882841adfdc7503b5a4d7a496829/1366_2000.jpg" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Zelda">                
                        <div class="container-fluid d-flex flex-column">
                            <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row mt-4">
                <div class="container-fluid" style="background-color: #191A19;">
                    <footer class="d-flex flex-wrap justify-content-between align-items-center">
                    <div class="col-md-4 d-flex align-items-center ms-5">
                        <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                            <i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-bootstrap"></i>
                        </a>
                        <span style="font-size: 1.5rem;" class="mb-3 mb-md-0 text-muted"><p style="color: aliceblue;" class="mt-3">&copy; 2022 Nombre Página, Inc</p></span>
                    </div>      
                    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex me-5">
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-twitter"></i></a></li>
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-instagram"></i></a></li>
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-facebook-f"></i></a></li>
                    </ul>
                    </footer>
                </div>
            </div>
        </body>
        </html>
    ''')























def PaginaGuias(response):
        return HttpResponse('''
       <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Página Principal</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            <style>
body{
    background-image: url("https://p4.wallpaperbetter.com/wallpaper/926/325/306/video-game-crossover-collage-mario-wallpaper-preview.jpg");
}
a{
    text-decoration: none;
}
.carousel-caption.d-none.d-md-block {
display: block!important;
margin-bottom: -7%;
}
img.d-block.w-100.img-fluid:hover {
    filter: sepia(60%);
    transition-duration: 2s, 3s, 2s, 3s;

}
div#carouselExampleFade {
    margin-top: 8rem!important;
}

*{ margin: 0; padding: 0; box-sizing: border-box;}
 h2.text-center {
    margin-top: -53.8px;
    margin-bottom: 5%;
}
h3.text-titulo2 {
    font-size: 38px;
}
.row {
margin-right: auto;
margin-left: auto;
}
.row-seccion-guias {
background: wheat;
border: 0;
margin-left: 13vw;
margin-right: 14vw;
margin-top: 10%;
}
.col-12-sec1 {
flex: 0 0 auto;
width: 100%;
height: 100%;
}
p.textoEnlace {
    margin-left: -12%;
    margin-bottom: -11%;
}
p.texto1guias {
    margin-top: 89px !important;
    margin-bottom: -5rem !important;
    margin-left: -8% !important;
}
                
.tarjeta{
background: black;
display:flex;
flex-direction:column;
justify-content:space-between;
width:420px;
border: 1px solid rgb(32, 15, 15);
box-shadow: 2px 2px 8px 4px #a03131d1;
border-radius:15px;
font-family: sans-serif;
margin-left: 3%;
}
.tarjeta-2{
    background: black;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 420px;
    border: 1px solid rgb(32, 15, 15);
    box-shadow: 2px 2px 8px 4px #a03131d1;
    border-radius: 15px;
    font-family: sans-serif;
    margin-left: 53%;
    margin-top: -30%;
}
.tarjeta-3{
background: black;
display:flex;
flex-direction:column;
justify-content:space-between;
width:420px;
border: 1px solid rgb(32, 15, 15);
box-shadow: 2px 2px 8px 4px #a03131d1;
border-radius:15px;
font-family: sans-serif; 
margin-top: 5%;
margin-left: 3%;
}
.tarjeta-4{
    background: black;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 420px;
    border: 1px solid rgb(32, 15, 15);
    box-shadow: 2px 2px 8px 4px #a03131d1;
    border-radius: 15px;
    font-family: sans-serif;
    margin-left: 53%;
    margin-top: -30.7%;
}
h4.textimg-sec2 {
    color: white;
    position: absolute;
    margin-left: 9%;
    margin-top: -3%;
}
h4.textimg1-sec2 {
    color: white;
    position: absolute;
    margin-left: 9%;
    margin-top: -3%;
}
h4.textimg2-sec2 {
    color: white;
    position: absolute;
    margin-left: 9%;
    margin-top: -3%;
}
h4.textimg3-sec2 {
    color: white;
    position: absolute;
    margin-left: 9%;
    margin-top: -3%;
}
/* tarjetas seccion tres */
.tarjeta-sec2{
display:flex;
flex-direction:column;
justify-content:space-between;
width:420px;
border: 1px solid rgb(32, 15, 15);
box-shadow: 2px 2px 8px 4px #a03131d1;
border-radius:15px;
font-family: sans-serif;
margin-left: 3%;
}
.tarjeta-2-sec2{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 420px;
    border: 1px solid rgb(32, 15, 15);
    box-shadow: 2px 2px 8px 4px #a03131d1;
    border-radius: 15px;
    font-family: sans-serif;
    margin-left: 53%;
    margin-top: -59%;
}
.tarjeta-3-sec2{
display:flex;
flex-direction:column;
justify-content:space-between;
width:420px;
border: 1px solid rgb(32, 15, 15);
box-shadow: 2px 2px 8px 4px #a03131d1;
border-radius:15px;
font-family: sans-serif; 
margin-top:5% ;
margin-left: 3%;
}
.tarjeta-4-sec2{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 420px;
    border: 1px solid rgb(32, 15, 15);
    box-shadow: 2px 2px 8px 4px #a03131d1;
    border-radius: 15px;
    font-family: sans-serif;
    margin-left: 53%;
    margin-top: -59%;
}
/*seccion 4*/
/*fin seccion 4*/
.titulo{
font-size: 24px;
padding: 10px 10px 0 10px;
}
.cuerpo{
    padding: 7px;
    background-color: #890000;
    border-radius: 43px;
}
.pie{
background: #442929;
border-radius:0 0 15px 15px;
padding: 10px;
text-align:center;
color: white;
}
.pie a{
text-decoration: none;

}
.pie a:after {
position: absolute;
top: 0;
right: 0;
bottom: 0;
left: 0;
z-index: 1;
color: white;
}
.pie:hover{
    background:radial-gradient( circle, black, #1162ac);
    transition-duration: 2s, 3s, 2s, 3s;

}
img.img-sec2-1 {
    width: 100% !important;
    
}
img.img-sec2-1:hover {
    filter: blur(4px);
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    transition-duration: 2s, 3s, 2s, 3s;
}
img.img-sec2-2 {
   
   width: 100% !important;
   border-radius: 20px;
   height: 17vw;
}
img.img-sec2-2:hover {
    filter: blur(4px);
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    transition-duration: 2s, 3s, 2s, 3s;
}

img.img-sec2-3 {
    width: 100% !important;
    height: 17vw;
}
img.img-sec2-3:hover {
    filter: blur(4px);
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    transition-duration: 2s, 3s, 2s, 3s;
}
img.img-sec2-4 {
    width: 100% !important;
    height: 17vw;
}
img.img-sec2-4:hover {
    filter: blur(4px);
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    transition-duration: 2s, 3s, 2s, 3s;
}

            </style>
            <script src="https://kit.fontawesome.com/638f505c64.js" crossorigin="anonymous"></script>
        </head>
        <body>
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="texto1" style="font-size: 1.5rem;     margin-top: 0;
                margin-bottom: 1rem;
                margin-left: -1%; ">Seccion De Guias</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
            <!--seccion 1 con carusel-->
            <div class="row-seccion-guias" >
                <div class="col-12-sec1">
                    <div class="container-fluid" style="width: 80%;">  
                        
                        <a href="" class="enlaceInico"><p class="textoEnlace">nombreProy</p></a>
                        <h3 class="text-titulo2"><p class="texto1guias" style="    margin-top: 0;
                            margin-bottom: 1rem;
                            margin-left: -8%;">GUÍAS DE VIDEOJUEGOS</p></h3>
                        
                        <div id="carouselExampleFade" class="carousel slide carousel-fade mt-3" data-bs-ride="carousel">
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                   <a href="">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/clans/41005067/8fa043dc9fcf4cb1fa04aa99ce71cb8aae072c67.png" class="d-block w-100 img-fluid" alt="Elder Ring">
                                    <div class="carousel-caption d-none d-md-block">
                                        <br><h5>GUIA DE ELDEN RING</h5>
                                        <p>Esto es todo lo que necesitas saber para completar Elden Ring al 100%. ¿Serás tú el Sinluz que restaure el Círculo de Elden, o perecerás en el intento?</p>
                                    </div>
                                   </a>
                                </div>
                                <div class="carousel-item">
                                    <img src="https://www.cosmocover.com/wp-content/uploads/2022/02/EN_SIFU_Standard_Edition_Key_Art_16x9-scaled.jpg" class="d-block w-100 img-fluid" alt="Sifu">
                                    <div class="carousel-caption d-none d-md-block">
                                        <h5 class="mt-5">Titulo Noticia</h5>
                                        <p>Descripción corta</p> 
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img src="https://as01.epimg.net/meristation/imagenes/2021/04/22/analisis/1619092845_591663_1619164855_noticia_normal.jpg" class="d-block w-100 img-fluid" alt="Nier">
                                    <div class="carousel-caption d-none d-md-block">
                                        <br><h5>Titulo Noticia</h5>
                                        <p>Descripción corta</p>
                                    </div>
                                </div>                
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    </div>
                </div>
                



                    
                    <div class="container-fluid ">
                        <div class="col-12">
                            <div class="tarjeta">
                                <div class="cuerpo"> 
                                <img src="https://medialazy.vandalimg.com/m/2-2022/202222411331812_1.jpg"  class="img-sec2-1" style="width: 15%;border-radius: 20px;" alt="muestra"><h4 class="textimg-sec2">Titulo Articulo</h4>              
                                </div>
                        
                        <a href="#"><div class="pie">Más información</div></a>
   
                        </div>
                    </div>
                    
                        <div class="tarjeta-2">
                        <div class="cuerpo"> 
                            <img src="https://medialazy.vandalimg.com/i/323x139/9-2020/202092917111858_1.jpg"  class="img-sec2-2" style="width: 15%;border-radius: 20px;" alt="muestra"><h4 class="textimg1-sec2">Titulo Articulo</h4>                            
                        </div>
                        
                        <a href="#"><div class="pie">Más información</div></a>
   
                        </div>


                        <div class="tarjeta-3">
                            <div class="cuerpo"> 
                                <img src="https://medialazy.vandalimg.com/i/323x139/3-2021/2021329101281_1.jpg"  class="img-sec2-3" style="width: 15%;border-radius: 20px;" alt="muestra"><h4 class="textimg2-sec2">Titulo Articulo</h4>                            
                            </div>
                           
                            <a href="#"><div class="pie">Más información</div></a>
       
                            </div>

                            <div class="tarjeta-4">
                                <div class="cuerpo"> 
                                    <img src="https://media.vandal.net/i/300x160/7-2022/202272815195974_1.jpg"  class="img-sec2-4" style="width: 15%;border-radius: 20px;" alt="muestra"><h4 class="textimg3-sec2">  Titulo Articulo</h4>                 
                                </div>
                                
                                <a href="#"><div class="pie">Más información</div></a>
           
                                </div>
                    
                             </div>
                        </div>

                        <!--seccion 2-->
                        <section class="section2">
                            <div class="row-seccion-guias" >
                                <div class="col">
                                    <div class="container-fluid" style="width: 80%;">  
                                        
                                        <a href="" class="enlaceInico"><p class="textoEnlace">nombreProy</p></a>
                                        <h3 class="text-titulo2"><p class="texto1guias2">Últimas Noticias</p></h3>
                                        
                                        
                                    </div>
                                </div>
                                
                
                
                
                                    
                                    <div class="container-fluid ">
                                        <div class="col-12">
                                            <div class="tarjeta-sec2">
                                                <div class="cuerpo"> 
                                                <img src="https://www.enter.co/wp-content/uploads/2017/03/Persona-5-Protagonist-Introduction.jpg"  class="img-sec2-1" style="width: 15%;border-radius: 20px;" alt="muestra">                
                                                </div>
                                        <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p><p>descripcion: Lorem ipsum dolor, sit amet consectetur adipisicing elit. Omnis, quos veniam! Obcaecati cupiditate nihil nulla reiciendis magnam perspiciatis laudantium mollitia molestias dignissimos ducimus, cumque unde odio exercitationem atque ipsum dolores!</p>
                                        <a href="#"></a><div class="pie">Más información</div></a>
                   
                                        </div>
                                    </div>
                                    
                                        <div class="tarjeta-2-sec2">
                                        <div class="cuerpo"> 
                                            <img src="https://www.enter.co/wp-content/uploads/2017/03/Persona-5-Protagonist-Introduction.jpg"  class="img-sec2-1" style="width: 15%;border-radius: 20px;" alt="muestra">                
                                        </div>
                                        <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p><p>descripcion: Lorem ipsum dolor, sit amet consectetur adipisicing elit. Omnis, quos veniam! Obcaecati cupiditate nihil nulla reiciendis magnam perspiciatis laudantium mollitia molestias dignissimos ducimus, cumque unde odio exercitationem atque ipsum dolores!</p>
                                        <a href="#"></a><div class="pie">Más información</div></a>
                   
                                        </div>
                
                
                                        <div class="tarjeta-3-sec2">
                                            <div class="cuerpo"> 
                                                <img src="https://www.enter.co/wp-content/uploads/2017/03/Persona-5-Protagonist-Introduction.jpg"  class="img-sec2-1" style="width: 15%;border-radius: 20px;" alt="muestra">                
                                            </div>
                                            <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p><p>descripcion: Lorem ipsum dolor, sit amet consectetur adipisicing elit. Omnis, quos veniam! Obcaecati cupiditate nihil nulla reiciendis magnam perspiciatis laudantium mollitia molestias dignissimos ducimus, cumque unde odio exercitationem atque ipsum dolores!</p>
                                            <a href="#"></a><div class="pie">Más información</div></a>
                       
                                            </div>
                
                                            <div class="tarjeta-4-sec2">
                                                <div class="cuerpo"> 
                                                    <img src="https://www.enter.co/wp-content/uploads/2017/03/Persona-5-Protagonist-Introduction.jpg"  class="img-sec2-1" style="width: 15%;border-radius: 20px;" alt="muestra">                
                                                </div>
                                                <h6>Titulo Articulo</h6><p>Autor: Nombre Persona</p><p>descripcion: Lorem ipsum dolor, sit amet consectetur adipisicing elit. Omnis, quos veniam! Obcaecati cupiditate nihil nulla reiciendis magnam perspiciatis laudantium mollitia molestias dignissimos ducimus, cumque unde odio exercitationem atque ipsum dolores!</p>
                                                <a href="#"></a><div class="pie">Más información</div></a>
                           
                                                </div>
                                    
                                             </div>
                                        </div>
                        </section>
                        <!--seccion 3-->

                    </div>                   
                </div>
            </div>
            <div class="row mt-4">
                <div class="container-fluid" style="background-color: #191A19;">
                    <footer class="d-flex flex-wrap justify-content-between align-items-center">
                    <div class="col-md-4 d-flex align-items-center ms-5">
                        <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                            <i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-bootstrap"></i>
                        </a>
                        <span style="font-size: 1.5rem;" class="mb-3 mb-md-0 text-muted"><p style="color: aliceblue;" class="mt-3">&copy; 2022 Nombre Página, Inc</p></span>
                    </div>      
                    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex me-5">
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-twitter"></i></a></li>
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-instagram"></i></a></li>
                        <li class="ms-3"><a class="text-muted" href="#"><i style="color: aliceblue; font-size: 2.5rem;" class="fa-brands fa-facebook-f"></i></a></li>
                    </ul>
                    </footer>
                </div>
            </div>
        </body>
        </html>    ''')

