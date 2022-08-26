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
                .discount-label {
                    background-color: #950101;
                    padding:8px; 
                    position:absolute;
                    float:left;
                    margin-top:-120px;
                    margin-left:60px;
                    width:30px;
                    border-radius: 50%;
                    transform: rotate(30deg);
                }
                .discount-label span {
                    color:#ffffff;
                    text-align:center;
                    font-family:"Raleway",Helvetica;
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
                <div class="col-12 mt-3">
                    <h2 class="text-center">Ofertas Steam</h2>
                    <div class="cards d-flex flex-wrap">
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-50%</strong></span></div> 
                                <img src="https://uvejuegos.com/img/caratulas/60296/pc.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Dark Souls">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-77%</strong></span></div>    
                                <img src="https://media.redadn.es/imagenes/tomb-raider-pc_153837.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Tomb Raider">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-33%</strong></span></div> 
                                <img src="https://i.pinimg.com/236x/f0/0f/aa/f00faa9d57c931debbf589a82cb06d6e.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Uncharted">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-20%</strong></span></div> 
                                <img src="https://i.blogs.es/55a00e/gris/450_1000.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Gris">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-80%</strong></span></div> 
                                <img src="https://uvejuegos.com/img/caratulas/53456/pc.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Mass Effect Andromeda">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-10%</strong></span></div> 
                                <img src="https://cdn.tutsplus.com/cdn-cgi/image/width=640/psd/uploads/legacy/psdtutsarticles/linkb_60vgamecovers/19.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Half life 2">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-60%</strong></span></div> 
                                <img src="https://sm.ign.com/ign_es/screenshot/default/781-2_4na5.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Mafia">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-70%</strong></span></div> 
                                <img src="https://i.3djuegos.com/juegos/5635/darksiders_ii/fotos/ficha/darksiders_ii-1960314.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Darksiders">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-35%</strong></span></div> 
                                <img src="https://cl.buscafs.com/www.levelup.com/public/uploads/images/478984_256x320.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Hollow Knight">
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
        </body>
        </html>
    ''')

#CREADO POR ESTIVEN
def GuiaGOW(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>GUIA</title>
        </head>
        <body>
            <div>
                <h2>Guía God of War (PC, PS4 y PS5): Trucos, consejos y secretos</h2>
                <h4>Enseña a Kratos a ser padre y a Atreus a ser un dios con la guía más completa de God of War en español.</h4>
            </div>
            <div>
                <img src="https://media.vandal.net/m/3-2020/20203218232519_1.jpg" alt="" srcset="">
            </div>
                <div>
                    <p>
                        Bienvenidos a la guía más completa de God of War para PS4, PC y PS5. Descubre todos los secretos del juego, complétalo al 100%, consigue todos los trofeos y descúbrelo todo sobre la nueva aventura del dios de la guerra. Como es sabido, Kratos acabó con todo aquello que se interponía en su camino en la antigua Grecia. Sin embargo, ahora, cansado y muy cambiado, vive en los lejanos reinos del norte acompañado de su hijo Atreus. No te dejes nada en God of War PS4 con nuestra guía completa del juego.
                    </p>
                </div>
                <div>
                    <h4>Preguntas frecuentes</h4>
                    <p>
                        <ul> <li> <b>Cómo mejorar las armaduras:</b> Tendrás que esperar a haber avanzado lo suficiente en la historia para desbloquear la tienda. Puedes mejorar tu equipo en cualquiera de las tiendas del juego.</li>
                        </ul>
                        <ul> <li> <b>Cómo conseguir los materiales para mejorar las armas:</b> Se trata de materiales que el juego nos da automáticamente al derrotar a los jefes. Para la última mejora de las armas principales debes completar los Reinos opcionales.</li>
                        </ul>
                        <ul> <li> <b>Cómo conseguir mejores armaduras:</b> Las mejores armaduras se consiguen en Niflheim. En los cofres el equipo es la mayoría de veces aleatorio.</li>
                        </ul>
                        <ul> <li> <b>Cómo conseguir XP y Plata rápidamente;</b> No hay un sistema rápido, el juego está perfectamente equilibrado en este sentido.</li>
                        </ul>
                        <ul> <li> <b>¿Hace falta haber jugado a los God of War anteriores para entender la historia?</b> No. Siempre que sepas quién es Kratos y a quiénes mató en Grecia, podrás comprender la historia perfectamente.</li>
                        </ul>
                    </p>
                </div>
                <div>
                    <h4>Historia</h4>
                    <p>
                        Te contamos cómo superar todas las misiones de historia de God of War, sin spoilers e indicando una buena parte de los coleccionables que encontrarás en tu camino. Si quieres exprimir tu partida al máximo, no te pierdas nuestra guía completa de la historia de God of War.
                    </p>
                </div>
                <div>
                    <h4>Favores</h4>
                    <p>
                        God of War nos ofrece unas cuantas misiones secundarias, que en este caso llevan el nombre de Favores. Desde las criaturas más pequeñas hasta los monstruos más grandes, todos tienen algo que pedirte y nosotros te contamos cómo cumplir con todo. Todos los favores.
                    </p>
                </div>
                <div>
                    <h4>Valquirias</h4>
                    <p>
                        Las valquirias están de nuevo sobre la tierra. Sin embargo, parece que no lo están precisamente por voluntad propia. Kratos tendrá que enfrentarse a ellas y averiguar qué ha sucedido si quiere arreglar esta situación. Derrotar a todas las valquirias no será fácil, pero nosotros te ayudaremos a salir con vida de los enfrentamientos.
                    </p>
                </div>
                <div>
                    <h4>Mapas del tesoro</h4>
                    <p>
                        Un sitio tan antiguo como Midgard no puede tener todo a simple vista. Repartidas por las distintas regiones del Reino de los hombres, encontrarás una serie de ubicaciones que tienen un tesoro oculto. Estos tesoros contienen Recursos especiales, enfocados a poder mejorar nuestros accesorios y, cómo no, conseguir una buena cantidad de Plata.
                        <br><br>
                        No vayas demasiado rápido, porque tendrás que encontrar los mapas para poder coger los tesoros. Lo primero es fácil, para lo segundo puede que tengas problemas, ya que sólo te dan una imagen y una pista de dónde buscar.
                    </p>
                </div>
                <div>
                    <h4>Cámaras Ocultas de Odín</h4>
                    <p>
                        El padre de los dioses del norte tiene una serie de escondrijos para sus tesoros repartidos por los Reinos. ¿Qué es lo que realmente ha ocultado en estos lugares y por qué? Sólo hay una manera de averiguarlo: abriendo las Cámaras. Todas las cámaras ocultas de Odín.
                    </p>
                </div>
        </body>
        </html>
    ''')