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











def Foro(response):
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
        <body style=" background: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ02qYYeqeXEnbgAN_I4-AaDzDx0btqxvzW7g&usqp=CAU);">
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Foros </h1>
                <p class="text-center" style="font-size: 1.5rem;">Categoria: juegos</p>
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
                                <a class="nav-link active" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
        
            <div class="col-8  row d-flex justify-content-center"style="background-color: #fef7f7;">

                <div class="row">
                    <div class="col-6 mt-2">
                        <h4 class="text-right"style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">videojuegos</p></h4>
 
                    </div>
                    <div class="col-6 mt-2" >
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">ultimos posts</p></h4>

                    </div>
                </div>




                <div class="row">
                    <div class="col-6 mt-2">

                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/8286/8286658.png" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                 <h6><a href="/" style="color: #000000; text-decoration: none;" >Videojuegos en general</a></h6><p>Temas sobre juegos en general. Lanzamientos, actualidad, gustos, preguntas...</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                                                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >9 minutos - Cyber_Turbo_R</a></h6>
                                <p>[Post oficial V.4] CAPTURAS DE JUEGOS</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/189/189533.png" class="img-fluid" style="width: 15%;border-radius: 20px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6> <a href="/" style="color: #000000; text-decoration: none;" >Videojuegos específicos</a></h6><p>Encuentra el foro de tu juego preferido y relaciónate con su comunidad.</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                                                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >un momento - edurance</a></h6><p> Noticia: PlayStation se enfrenta a una demanda millonaria por una presunta 'estafa' al consumidor </p>
                            </div>
                        </div>
                    </div>

                </div>


                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/2005/2005003.png" class="img-fluid" style="width: 15%;border-radius: 2px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >Noticias y actualidad</a></h6><p>Tribuna abierta para comentar las noticias del mundo del videojuego.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >13 minutos - LordDagak</a></h6><p>● Sonic  Post oficial ●  Sonic Frontiers estas Navidades</p>
                            </div>               

                        </div>
                    </div>
                </div>



                <div class="row">
                    <div class="col-6 mt-2">
                        <h4 class="text-right"style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">MÁS QUE VIDEOJUEGOS</p></h4>
 
                    </div>
                    <div class="col-6 mt-2" >
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">ultimos posts</p></h4>

                    </div>
                </div>







                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/7509/7509773.png" class="img-fluid" style="width: 15%;border-radius: 2px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >Off Topic y humor</a></h6><p>Hablemos de todo menos de juegos o temas de otros foros.</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >4 horas - Jocs_204</a></h6><p> GRAN TURISMO 7  Encuentra tu trazada</p>
                            </div>                  
 
                        </div>
                    </div>

                </div>

                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/3959/3959335.png" class="img-fluid" style="width: 15%;border-radius: 2px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >Desarrollo de videojuegos</a></h6><p>Comparte proyectos y conocimientos.</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >13/06/2022 17:03 - Alendi93</a></h6><p>Discord para aprender Unity y desarrollo de juegos en general [Proyecto serio]</p>
                            </div>                  
 
                        </div>
                    </div>

                </div>









                <div class="row">
                    <div class="col-6 mt-2">
                        <h4 class="text-right"style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">SISTEMAS</p></h4>
 
                    </div>
                    <div class="col-6 mt-2" >
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">ultimos posts</p></h4>

                    </div>
                </div>





                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/2331/2331858.png" class="img-fluid" style="width: 15%;border-radius: 40px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >	PC / Hardware y presupuestos</a></h6><p>Jugadores de PC, Steam, juegos digitales y expertos en configurar equipos y presupuestos.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >19/08/2022 10:39 - Guthwulf</a></h6><p>Monster boy and the cursed kingdom: posible bug</p>
                            </div>             

                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/1724/1724566.png" class="img-fluid" style="width: 15%;border-radius: 2px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >	PlayStation 5 / PlayStation 4 / PlayStation 3</a></h6><p>Videojuegos, PSN, PSPlus, PlayStation VR y más para los seguidores de consolas Sony</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >45 minutos - Safenix</a></h6><p>[Xenohilo Oficial] Saga Xenoblade Chronicles: Monolith does what Retrodont</p>
                            </div>                 
 
                        </div>
                    </div>

                </div>
                <div class="row">
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <img src="https://cdn-icons-png.flaticon.com/128/588/588298.png" style="width: 15%;border-radius: 20px;" alt="Sekiro">                
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" > Xbox Series X / Xbox One / Xbox 360</a></h6><p>Juegos, Xbox Live, Arcade, retrocompatibilidad y todo sobre las consolas Xbox de Microsoft.</p>
                            </div>
                        </div>  
                    </div>
                    <div class="col-6 mt-2">
                        <div class="container-fluid d-flex justify-content-start mt-3">
                            <div class="container-fluid d-flex flex-column">
                                <h6><a href="/" style="color: #000000; text-decoration: none;" >21/06/2021 16:51 - Xilos</a></h6><p>P.O THE LEGEND OF SAGA [Every game has a story, Only one is a legend]b</p>
                            </div>                 
 
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
            </div>
        </body>
        </html>
    ''')