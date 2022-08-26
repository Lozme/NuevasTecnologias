from django.shortcuts import render
from django.http import HttpResponse


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
                    background-color: red;
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
                                <a class="nav-link" href="Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
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
                    <div class="cards d-flex flex-wrap justify-content-center">
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
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-35%</strong></span></div> 
                                <img src="https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/hc_167x260/public/media/image/2018/01/celeste-portada.jpg?itok=zaHBO9eM" class="img-fluid" style="width: 115px;height: 130px;" alt="Hollow Knight">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-35%</strong></span></div> 
                                <img src="https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/1200/public/media/image/2018/01/sfv-arcade-edition-portada.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Hollow Knight">
                            </div>                
                        </div>
                        <div class="card-container mt-2 ms-3">
                            <div class="container d-flex justify-content-center align-items-center" style="background-color: #008A27;width: 120px;height: 150px;">
                                <div class="discount-label red" style="position: absolute;"><span style="font-size: 0.5rem;"><strong>-35%</strong></span></div> 
                                <img src="https://cdn.alfabetajuega.com/alfabetajuega/abj_public_files/multimedia/imagenes/201212/28054.cover7.jpg" class="img-fluid" style="width: 115px;height: 130px;" alt="Hollow Knight">
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

#########################################################################################
#########################################################################################

#CREADO POR: Victor Rios
def Noticias(response):
    return HttpResponse('''
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Noticias</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
        <style>
            *{ margin: 0; padding: 0; box-sizing: border-box; }
            .row {
                margin-right: auto;
                margin-left: auto;
            }
            #jumbo{
                margin-bottom: 0; 
                color: white;
                background-image: url(https://www.nitro-pc.es/blog/wp-content/uploads/2020/08/Portada-juegos-baratos.png);
                background-color: #cccccc;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
                position: relative;
                height: 100%;
        
            }
            a{
                text-decoration: none!important;
                color: black;
            }
            #frase{
                background-color: rgba(61,0,0,0.5);
            }
            #upi{
                color: #E04646;
            }
            #upi:hover{
                color: white!important;
            }
            .active{
                color: #E04646!important
            }
            .nav-link:hover,.bi:hover{
                color: #E04646!important
            }
            .abs-center {
                display: flex;
                align-items: center;
                justify-content: center;
            }
            #card:hover{
                box-shadow: 5px 0px 40px rgba(224, 70, 70, 0.596);
                -webkit-transform: scale(1.1);
                transform: scale(1.1);
                color: #212529!important; 
            }
            
        </style>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
        
    </head>
    <body style="background-color: #fef7f7;">
        <div class="row">
            <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
            <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
            <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
            <hr style="margin: 0;">
            <nav class="navbar navbar-expand-lg">
                <div class="container-fluid">
                    <a class="navbar-brand" href="/" style="color: aliceblue;font-size: 2rem;">Logo</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                            <a class="nav-link" href="Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            </div>
        </div> 
        <br><br>
        <section>        
            <div class="row">
                <div class="col ">
                    <div class="row text-center"  style="background-color: #212529;">
                        <strong><h2 style="color: black;">ÚLTIMAS NOTICIAS DE VIDEOJUEGOS</h2></strong>
                    </div>
                    <br><br><br>
                    <div class="row">
                        <p style="color: black;"">Aquí encontrarás todas las noticias y las últimas novedades en videojuegos. Recopilamos cada día y minuto a minuto toda la actualidad del mundo de los videojuegos y sus diferentes plataformas para que siempre estés al corriente de la última actualización o contenido relacionado con tus títulos preferidos, de las fechas de lanzamiento de los juegos más esperados, los anuncios más importantes, reportajes, entrevistas, declaraciones, nuevas imágenes o tráileres y todas las curiosidades del mundillo para mantenerte informado y a la vez entretenido.</p>
                    </div>
                
                </div>
                <div class="col">
                    <div class="ratio ratio-16x9" >
                        <iframe src="https://www.youtube.com/embed/ezKQ-FE4UEQ" title="YouTube video" allowfullscreen></iframe>
                    </div>
                </div>
            </div>
            <br><br>
        </section>
        <section style="background-color: #FEF7F7;">
            <br>
            <div class="row text-center">
                <strong><h1>Noticias</h1></strong>
            </div>
            <hr>
        </section>
        <br>
        <section style="background-color: #FEF7F7;">
            <br><br>
            <div class="row ">
                <div class="col abs-center">
                    <a href="https://vandal.elespanol.com/noticia/1350755903/kena-bridge-of-spirits-llega-a-steam-en-septiembre-con-nuevos-modos-y-opciones/">
                        <div class="card mb-3" id="card" style="max-width: 540px;">
                            <div class="row g-0">
                            <div class="col-md-4">
                                <img src="https://3y3seo1md7o8303qa48ddzzb-wpengine.netdna-ssl.com/wp-content/uploads/2022/06/gamer.png" class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                <h5 class="card-title">Titulo</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel maiores ipsa perspiciatis labore? Ea delectus est suscipit fugit nostrum sapiente quas exercitationem? Accusantium minima qui fugiat ipsam, pariatur quis blanditiis.</p>
                                <p class="card-text">
                                    <small class="text-muted"><i class="bi bi-clock-fill"></i> Last updated 3 mins ago</small>
                                    <small class="text-muted"><i class="bi bi-person-fill"></i> Kevin Mier</small>
                                </p>
                                
                                </div>
                            </div>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col abs-center">
                    <a href="https://vandal.elespanol.com/noticia/1350755903/kena-bridge-of-spirits-llega-a-steam-en-septiembre-con-nuevos-modos-y-opciones/">
                        <div class="card mb-3" id="card" style="max-width: 540px;">
                            <div class="row g-0">
                            <div class="col-md-4">
                                <img src="https://3y3seo1md7o8303qa48ddzzb-wpengine.netdna-ssl.com/wp-content/uploads/2022/06/gamer.png" class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                <h5 class="card-title">Titulo</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel maiores ipsa perspiciatis labore? Ea delectus est suscipit fugit nostrum sapiente quas exercitationem? Accusantium minima qui fugiat ipsam, pariatur quis blanditiis.</p>
                                <p class="card-text">
                                    <small class="text-muted"><i class="bi bi-clock-fill"></i> Last updated 3 mins ago</small>
                                    <small class="text-muted"><i class="bi bi-person-fill"></i> Kevin Mier</small>
                                </p>
                                
                                </div>
                            </div>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
            <br>
            <div class="row ">
                <div class="col abs-center">
                    <a href="https://vandal.elespanol.com/noticia/1350755903/kena-bridge-of-spirits-llega-a-steam-en-septiembre-con-nuevos-modos-y-opciones/">
                        <div class="card mb-3" id="card" style="max-width: 540px;">
                            <div class="row g-0">
                            <div class="col-md-4">
                                <img src="https://3y3seo1md7o8303qa48ddzzb-wpengine.netdna-ssl.com/wp-content/uploads/2022/06/gamer.png" class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                <h5 class="card-title">Titulo</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel maiores ipsa perspiciatis labore? Ea delectus est suscipit fugit nostrum sapiente quas exercitationem? Accusantium minima qui fugiat ipsam, pariatur quis blanditiis.</p>
                                <p class="card-text">
                                    <small class="text-muted"><i class="bi bi-clock-fill"></i> Last updated 3 mins ago</small>
                                    <small class="text-muted"><i class="bi bi-person-fill"></i> Kevin Mier</small>
                                </p>
                                
                                </div>
                            </div>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col abs-center">
                    <a href="https://vandal.elespanol.com/noticia/1350755903/kena-bridge-of-spirits-llega-a-steam-en-septiembre-con-nuevos-modos-y-opciones/">
                        <div class="card mb-3" id="card" style="max-width: 540px;">
                            <div class="row g-0">
                            <div class="col-md-4">
                                <img src="https://3y3seo1md7o8303qa48ddzzb-wpengine.netdna-ssl.com/wp-content/uploads/2022/06/gamer.png" class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                <h5 class="card-title">Titulo</h5>
                                <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel maiores ipsa perspiciatis labore? Ea delectus est suscipit fugit nostrum sapiente quas exercitationem? Accusantium minima qui fugiat ipsam, pariatur quis blanditiis.</p>
                                <p class="card-text">
                                    <small class="text-muted"><i class="bi bi-clock-fill"></i> Last updated 3 mins ago</small>
                                    <small class="text-muted"><i class="bi bi-person-fill"></i> Kevin Mier</small>
                                </p>
                                
                                </div>
                            </div>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </section>
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

#########################################################################################
#########################################################################################

#CREADO POR: Juan Camilo Cano
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
                                <a class="nav-link" href="Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link active" href="Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
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
