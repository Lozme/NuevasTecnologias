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
                                <a class="nav-link" href="Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
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
                        <h2 class="text-center" style="background-color:black;color:aliceblue;">Últimas Noticias</h2>
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
                    <h2 class="text-center" style="background-color:black;color:aliceblue;">Publicaciones Destacadas</h2>
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
                    <h2 class="text-center" style="background-color:black;color:aliceblue;">Ofertas Steam</h2>
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
                    <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                            <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="../Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="../Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                            </li>
                            <li class="nav-item">
                            <a class="nav-link" href="../Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
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
                    <div class="row text-center"  style="background-color: black;">
                        <strong><h2 style="color:aliceblue;">NUESTRO CONTENIDO</h2></strong>
                    </div>
                    <br><br><br>
                    <div class="row">
                        <p style="color: black;text-align:justify;">Aquí encontrarás todas las noticias y las últimas novedades en videojuegos. Recopilamos cada día y minuto a minuto toda la actualidad del mundo de los videojuegos y sus diferentes plataformas para que siempre estés al corriente de la última actualización o contenido relacionado con tus títulos preferidos, de las fechas de lanzamiento de los juegos más esperados, los anuncios más importantes, reportajes, entrevistas, declaraciones, nuevas imágenes o tráileres y todas las curiosidades del mundillo para mantenerte informado y a la vez entretenido.</p>
                    </div>
                
                </div>
                <div class="col">
                    <div class="row text-center"  style="background-color: black;">
                        <strong><h2 style="color:aliceblue;">ÚLTIMO VIDEO</h2></strong>
                    </div><br><br>
                    <div class="ratio ratio-16x9" >
                        <iframe src="https://www.youtube.com/embed/ezKQ-FE4UEQ" title="YouTube video" allowfullscreen></iframe>
                    </div>
                </div>
            </div>
            <br><br>
        </section>
        <section style="background-color: #FEF7F7;">
            <br>
            <div class="row text-center"  style="background-color: black;">
                <strong><h2 style="color:aliceblue;">ÚLTIMAS NOTICIAS</h2></strong>
            </div>
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
            <title>Foro</title>
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
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="../Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="../Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="../Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
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
        
            <div class="col-10  row d-flex justify-content-center"style="background-color: #fef7f7;">
                <div class="row">
                    <div class="col-6 mt-2">
                        <h4 class="text-right"style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">VIDEOJUEGOS</p></h4>
 
                    </div>
                    <div class="col-6 mt-2" >
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">Últimos Posts</p></h4>
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
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">Últimos Posts</p></h4>
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
                        <h4 class="text-right" style="background-color: #000000;border-radius: 20px;color: aliceblue;"><p class="titxex1" style="margin-left: 5%">Últimos Posts</p></h4>
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
            <div class="row">
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

#########################################################################################
#########################################################################################

#CREADO POR: Estiven Zapata
def GuiaGOW(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Guías</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            <style>
                *{ margin: 0; padding: 0; box-sizing: border-box; }
                .row {
                    margin-right: auto;
                    margin-left: auto;
                }
            </style>
        </head>
        <body>
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="../Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="../Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link active" href="../Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
            <div class="row d-flex justify-content-center">
                <div class="container-fluid w-75">
                    <div>
                        <h2 class="mt-5 text-center" style="background-color:black;color:aliceblue;">Guía God of War (PC, PS4 y PS5): Trucos, consejos y secretos</h2>
                        <h5 class="mt-3 text-center">Enseña a Kratos a ser padre y a Atreus a ser un dios con la guía más completa de God of War en español.</h5>
                    </div>
                    <div class="mt-3 text-center">
                        <img style="width:70%" src="https://media.vandal.net/m/3-2020/20203218232519_1.jpg" alt="" srcset="">
                    </div>
                    <div class="mt-3">
                        <p style="text-align:justify;">
                            Bienvenidos a la guía más completa de God of War para PS4, PC y PS5. Descubre todos los secretos del juego, complétalo al 100%, consigue todos los trofeos y descúbrelo todo sobre la nueva aventura del dios de la guerra. Como es sabido, Kratos acabó con todo aquello que se interponía en su camino en la antigua Grecia. Sin embargo, ahora, cansado y muy cambiado, vive en los lejanos reinos del norte acompañado de su hijo Atreus. No te dejes nada en God of War PS4 con nuestra guía completa del juego.
                        </p>
                    </div>
                    <div>
                        <h4>Preguntas frecuentes</h4>
                        <p>
                            <ul> <li style="text-align:justify;"> <b>Cómo mejorar las armaduras:</b> Tendrás que esperar a haber avanzado lo suficiente en la historia para desbloquear la tienda. Puedes mejorar tu equipo en cualquiera de las tiendas del juego.</li>
                            </ul>
                            <ul> <li style="text-align:justify;"> <b>Cómo conseguir los materiales para mejorar las armas:</b> Se trata de materiales que el juego nos da automáticamente al derrotar a los jefes. Para la última mejora de las armas principales debes completar los Reinos opcionales.</li>
                            </ul>
                            <ul> <li style="text-align:justify;"> <b>Cómo conseguir mejores armaduras:</b> Las mejores armaduras se consiguen en Niflheim. En los cofres el equipo es la mayoría de veces aleatorio.</li>
                            </ul>
                            <ul> <li style="text-align:justify;"> <b>Cómo conseguir XP y Plata rápidamente;</b> No hay un sistema rápido, el juego está perfectamente equilibrado en este sentido.</li>
                            </ul>
                            <ul> <li style="text-align:justify;"> <b>¿Hace falta haber jugado a los God of War anteriores para entender la historia?</b> No. Siempre que sepas quién es Kratos y a quiénes mató en Grecia, podrás comprender la historia perfectamente.</li>
                            </ul>
                        </p>
                    </div>
                    <div>
                        <h4>Historia</h4>
                        <p style="text-align:justify;">
                            Te contamos cómo superar todas las misiones de historia de God of War, sin spoilers e indicando una buena parte de los coleccionables que encontrarás en tu camino. Si quieres exprimir tu partida al máximo, no te pierdas nuestra guía completa de la historia de God of War.
                        </p>
                    </div>
                    <div>
                        <h4>Favores</h4>
                        <p style="text-align:justify;">
                            God of War nos ofrece unas cuantas misiones secundarias, que en este caso llevan el nombre de Favores. Desde las criaturas más pequeñas hasta los monstruos más grandes, todos tienen algo que pedirte y nosotros te contamos cómo cumplir con todo. Todos los favores.
                        </p>
                    </div>
                    <div>
                        <h4>Valquirias</h4>
                        <p style="text-align:justify;">
                            Las valquirias están de nuevo sobre la tierra. Sin embargo, parece que no lo están precisamente por voluntad propia. Kratos tendrá que enfrentarse a ellas y averiguar qué ha sucedido si quiere arreglar esta situación. Derrotar a todas las valquirias no será fácil, pero nosotros te ayudaremos a salir con vida de los enfrentamientos.
                        </p>
                    </div>
                    <div>
                        <h4>Mapas del tesoro</h4>
                        <p style="text-align:justify;">
                            Un sitio tan antiguo como Midgard no puede tener todo a simple vista. Repartidas por las distintas regiones del Reino de los hombres, encontrarás una serie de ubicaciones que tienen un tesoro oculto. Estos tesoros contienen Recursos especiales, enfocados a poder mejorar nuestros accesorios y, cómo no, conseguir una buena cantidad de Plata.
                            <br><br>
                            No vayas demasiado rápido, porque tendrás que encontrar los mapas para poder coger los tesoros. Lo primero es fácil, para lo segundo puede que tengas problemas, ya que sólo te dan una imagen y una pista de dónde buscar.
                        </p>
                    </div>
                    <div>
                        <h4>Cámaras Ocultas de Odín</h4>
                        <p style="text-align:justify;">
                            El padre de los dioses del norte tiene una serie de escondrijos para sus tesoros repartidos por los Reinos. ¿Qué es lo que realmente ha ocultado en estos lugares y por qué? Sólo hay una manera de averiguarlo: abriendo las Cámaras. Todas las cámaras ocultas de Odín.
                        </p>
                    </div>                    
                </div>
            </div>
        </body>
        </html>
    ''')

#########################################################################################
#########################################################################################

#CREADO POR: Andrés Murillo
def GuiaFreeFire(response):
    return HttpResponse('''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Guías</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
            <style>
                *{ margin: 0; padding: 0; box-sizing: border-box; }
                .row {
                    margin-right: auto;
                    margin-left: auto;
                }
            </style>
        </head>
        <body>
            <div class="row">
                <div class="rounded-3" style="background: rgb(0,0,0);background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(61,0,0,1) 35%);;color:aliceblue;font-size: 1.6rem;">
                <h1 class="text-center  mt-2" style="font-size: 2.5rem;">Nombre Página / Logo</h1>
                <p class="text-center" style="font-size: 1.5rem;">Alguna frase</p>
                <hr style="margin: 0;">
                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="../" style="color: aliceblue;font-size: 2rem;">Logo</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                <a class="nav-link" href="../Noticias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Noticias</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="#" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="../Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link active" href="../Foro" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Foro</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                </div>
            </div> 
            <div class="row d-flex justify-content-center">
                <div class="container-fluid w-75">
                    <div>
                        <h2 class="mt-3 text-center" style="background-color:black;color:aliceblue;">Guía Free Fire, trucos, consejos y secretos</h2>
                        <p class="mt-3">En nuestra completa guía de Free Fire, el popular juego de móviles, te enseñamos los mejores consejos para sobrevivir y ganar en sus intensas y divertidas partidas Battle Royale.</p>
                    </div>
                    <div class="d-flex justify-content-center">
                        <iframe class="mt-3" width="75%" height="380" src="https://www.youtube.com/embed/CgqrHG_3i9g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                    <div class="mt-3">
                        <p style="text-align:justify;">
                            Bienvenidos a nuestra guía completa de Free Fire, uno de los juegos móviles que más descargas acumulan en el mercado, tanto en dispositivos Android como en iOS de Apple. Garena nos brinda una experiencia de acción en tercera persona al más puro estilo Battle Royale en la que debemos caer en una isla con 50 jugadores y sobrevivir hasta el final... solo si somos capaces. Para ayudaros a brillar en el campo de batalla os traemos en nuestra guía un montón de consejos, trucos y recomendaciones de todo tipo. Aquí podréis encontrar información acerca del arsenal del juego, cómo conseguir diamantes, desbloquear contenidos y mucho más. ¡Rompan filas, soldados!
                        </p>
                    </div>             
                </div>
            </div>
        </body>
        </html>
    ''')



def Analisiseldenring(response):
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
                                <a class="nav-link" href="Analisis" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Análisis</a>
                                </li>
                                <li class="nav-item">
                                <a class="nav-link" href="Guias" style="color: aliceblue;font-size: 1.5rem;margin-left: 5vw;">Guías</a>
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
            

        <div style="border: 5px solkid black;">
            <img src="Imagenes Analisis 1 y 2/Imagen 1 elden ring.jpeg" alt="" width="100%" height="75%">
            <h1>Elden Ring y este es nuestro análisis definitivo del juego de Fromsoftware</h1>
        </div> 
        <div>
            <h3>
                100 horas ha sido la cifra para completar nuestro viaje por las Tierras Intermedias. Una odisea que se saborea y se recuerda. Para muchos jugadores, Elden Ring será uno de los mejores ejemplos de por qué estamos en esta industria. De por qué nos gustan los videojuegos.
            </h3>
            <p>
                En la Odisea, Ulises (u Odiseo) recibe uno de los máximos castigos de los dioses: vagar diez años en su regreso a Ítaca después de la guerra de Troya. Normalmente, los mitos se ciñen a una sola aventura, pero el héroe griego se enfrenta al cíclope, a las sirenas, a la bruja Circe, a Escila (la hidra) y Caribdis e incluso desciende al Inframundo. Por eso no conocemos su gesta como un viaje, sino como una odisea. Cuando juegas a Elden Ring, sientes que estás viviendo algo similar. No eres solo un sinluz en busca de convertirte en señor del Círculo de Elden; eres un conquistador de las Tierras Intermedias. Tu aventura no es una sola. Son muchas.
            </p>
            <p>
                Después de 100 horas que marca el contador del juego, puedo decir que conozco Elden Ring. Es extraño esto. El juego está hecho conscientemente para que te sientas perdido. Su misticismo radica en lo hermético que es. Algunos de los lugares y misiones más espectaculares y largos del juego se esconden de la misma forma que otro videojuego escondería un coleccionable. Y, una vez que lo has completado todo (o casi todo, las primeras partidas a los juegos de FromSoftware son peculiares) el misterio inevitablemente se pierde y se transforma en otra cosa: en recuerdo de tus gestas. Has vuelto a Ítaca, pero diferente. Ya no eres el mismo.
            </p>
            <p >
                Ahora que ya no puedo jugar a Elden Ring de la forma constante que lo he hecho estos días porque ya lo he terminado, el juego comienza otro viaje: se está haciendo fuerte en el recuerdo. Noto cómo sus mazmorras, sus enemigos y los momentos épicos vividos empiezan5 a transformarse en una suerte de nostalgia temprana. Es casi como una droga. Sigues en esta industria, sigues jugando a videojuegos, buscando ese nuevo juego que te ofrezca las sensaciones que lograron obras como Elden Ring.
            </p>
        </div>
            <h1>La ambición del mundo abierto</h1>
            <img src="Imagenes Analisis 1 y 2/imagen 2 elden ring.jpg" alt="" height="75%" width="75%">
            <div>
            <p>
                Creo que el secreto está en su diseño. Recuerdo jugar a Far Cry 3, hace ya 10 años, y entrar en un búnker para la misión principal donde su mundo abierto se echaba a un lado para, por un momento, convertirse en un juego algo más lineal. Pensé que eso era lo correcto. Los mundos abiertos debían ser lienzos sobre los que pintar aventuras sin perder las bondades del diseño de un nivel cerrado. Porque mundo abierto y mundo cerrado no deben ser antónimos el uno del otro, sino complementarios. Y, sin embargo, desde entonces, he visto cómo los desarrolladores ya sufrían largos desarrollos por entregar juegos en los que todo sucede en ese lienzo. Quizá por ello, el campamento amurallado se ha convertido casi en un símbolo de este tipo de mundos abiertos. Una forma simple de cercar ese entorno inabarcable.
            </p>
            <p>
                Elden Ring hace algo que a todas luces parece demasiado arriesgado. Se niega a dejar de ser ese juego clásico con un diseño de niveles excelso, solo por construirse en un mapa lleno de kilómetros cuadrados que recorrer. Ofrece lo mejor de los dos mundos y lo mezcla con un ritmo marcado por el jugador. Esto de por sí ya sería digno de elogio, no funcionaría si no fuera por la calidad de su contenido. Dentro de esas "actividades" que forman un mundo abierto, las de Elden Ring son todas tan atractivas que quiere hacerlas todas. No sientes que hay contenido principal y secundario, porque mucho del secundario tiene tanta o más calidad que el principal, sino que todo parece obligatorio si quieres tener la experiencia completa en las Tierras Intermedias.
            </p>
            <p>
                Es por eso que no podía ceñirme a la misión principal y acabar este análisis. Tenía que completarlo todo. Cada vez que descubría un secreto o alguien me guiaba a una nueva zona no podía evitar acudir ahí, atraído por el canto de la sirena. Es esa curiosidad que mató al gato, porque vas a morir muchas veces irremediablemente, y a la que no puedes resistirte. El motor de FromSoftware es, y siempre ha sido, la curiosidad del jugador. Ahora que ya tiene cierto renombre, que sabe que sus aficionados van a explorar hasta el último centímetro cuadrado del mapa, pueden permitirse licencias que otros estudios no harían. Por ello, Elden Ring esconde una inmensa cantidad de secretos que dan lugar a los niveles más trabajados que he visto del estudio detrás de una simple pared (hablo simbólica y literalmente). Como probablemente estaréis haciendo, descubrir y compartir estos secretos forma parte de la experiencia; y Elden Ring lleva esa sensación de recompensa a un nuevo nivel.
            </p>
            </div>
            <h1>Arbol de la vida </h1>
            <img src="Imagenes Analisis 1 y 2/imagen 3 elden ring.jpg" alt="" height="100%" width="100%">
            <div>
                <p> 
                    Dice el escritor de fantasía Brandon Sanderson en una de sus clases (aparte de amistosamente envidiar la participación de Martin) que las ideas valen poco; lo importante es cómo las escribas. Para explicarlo, pone un ejemplo que me gusta mucho. El escritor Jim Butcher defendía esto ante unos aficionados en un foro que creían que una buena idea lo era todo. Él se comprometió a hacer un libro con la idea más absurda que le pudieran plantear; y lo que le plantearon fue mezclar Pokémon con la última legión romana. El resultado es una exitosa serie de libros llamada Codex Alera y a mí me sirve para explicar lo ocurrido con George R.R. Martin. Lo importante en una historia no siempre es el qué se cuenta, sino el cómo. Y la forma que tiene From de narrar sus juegos es tan personal que absorbe las ideas de Martin hasta el punto de hacerlas pasar por propias.
                </p>
                <p>
                    De Martin entonces, y como lector suyo, puedes notar algunos conceptos, pero su trabajo ha sido más en la sombra. Es el que los escritores de fantasía realizan antes de ponerse a escribir, cuando elaboran el pasado de sus mundos fantásticos. Es From la encargada de contarlo todo a través de la tradicional descripción de objetos y escasos diálogos de sus habitantes. Y el resultado a mi parecer se asemeja más a Bloodborne, por ejemplo, en la forma de ir tirando de un hilo pasado hasta descubrir lo que ha sucedido en el mundo de las Tierras Intermedias.
                </p>
                <p>
                    Al fin y al cabo, Martin no solo ha escrito Canción de Hielo y Fuego dentro del ámbito fantástico, sino que se ha centrado mucho en la ciencia-ficción y el terror. Por tanto, es difícil analizar sus tropos como lo podríamos hacer de otros autores como Sanderson o Abercrombie. Algunos temas, como las traiciones, la política y los escarceos de las clases altas, son propias del autor, no hay duda; pero también son tropos clásicos de la fantasía épica en general. De hecho, en los nombres de los personajes, que muchos comparten prefijos comunes, es algo en lo que coinciden tanto George R.R. Martin como Hidetaka Miyazaki (Rhaegon, Rhaegar, Rhaenys en Canción de Hielo y Fuego; Gwyn, Gwynevere, Gwyndolin en Dark Souls). Lo mismo sucede en Elden Ring.
                </p>
            </div>
            <div>
                <h1>Un mundo bello y fragmentado</h1>
                <p>
                    A medida que progresaba en mi partida, me ha ocurrido algo que tiene que ver con esa dicotomía tan marcada en los juegos de FromSoftware. El diseño visual se fue comiendo al técnico cada vez más. Necrolimbo es, sin duda, la zona más sufrida, donde más problemas he visto a nivel de popping de hierba, stuttering y caídas de frames. Poco a poco, el juego mantiene la escala pero mejora su suavidad. Las mazmorras se comportan siempre con una tasa de frames estable y los nuevos biomas como el de Liurna dan paso a lugares más escarpados que camuflan mejor los defectos de las vastas praderas del Necrolimbo.


                    No es excusa, claro está: FromSoftware tiene que mejorar asperezas tanto en el rendimiento del juego en PC y consolas como en el propio motor de juego, que no es capaz de representar algunos materiales como deberían. Probablemente el pelo de animales y personas sea uno de los aspectos que más sufren estos. Sin embargo, estoy de acuerdo en que Elden Ring no es el juego que debía liderar ese cambio; es intergeneracional y ha sufrido retrasos; es también un juego tan grande que un cambio de motor habría causado quizá muchos problemas. Pero sí, toca cambio de motor que se adecúe a la próxima generación.
                </p>
                <img src="Imagenes Analisis 1 y 2/Elden ring 4.jpg" alt="" width="75%" height="75%">
                <p>
                    Cuando me puse a jugar a Elden Ring, no imaginaba lo que me esperaba. Es uno de esos raros casos en que las expectativas se quedan cortas. En que ese juego que te has imaginado y has idealizado en tu cabeza después de todo el hype y todos los tráileres, se ve superado a los mandos. Y quiero decir, para que conste, que no me gustaría que todo en el futuro de FromSoftware fuera como Elden Ring a partir de ahora. Me gusta tanto o más su lado más vanguardista de Bloodborne y Sekiro, orientado a las mecánicas nuevas y la acción más que el RPG. A veces pienso que el éxito que Elden Ring está teniendo es tan desmesurado que podría sacar el lado más continuista de FromSoftware o de Bandai Namco. Me gusta la From que abraza distintas editoras para hacer ideas diferentes y espero que siga así.
                </p>
                <h2>Hay que disfrutar de Elden Ring, porque ocasiones así son tan únicas y fugaces como una estrella que cae del cielo</h2>
                <p>
                    Sin embargo creo que, con el paso del tiempo, el recuerdo de Elden Ring no hará más que mejorar más todavía. Lo que ha conseguido el equipo de Hidetaka Miyazaki es tan único y ambicioso que a veces dudo de que logre crear escuela. Porque, ¿qué estudio en su sano juicio crearía tanto contenido para un solo juego y sin DLCs? ¿Quién mimaría cada rincón de su vasto entorno para esconder secretos únicos? ¿Quién estaría dispuesto a reservar algunos de los mejores niveles para que solo lo vean un porcentaje muy reducido de los jugadores? La respuesta, lamentablemente, no es fácil. Pocos en nuestra amada industria tienen ahora mismo la libertad y la autoría de Hidetaka Miyazaki. Su filosofía de "Dirección Total", ahorrando intermediarios y supervisando todas las ramas del diseño, es, en el fondo, la más pareja a la que tienen los reputados directores de cine. Hay que disfrutar de Elden Ring, porque ocasiones así son tan únicas y fugaces como una estrella que cae del cielo. Dice el poema de Kavafis que "Cuando emprendas tu viaje a Itaca, pide que el camino sea largo, lleno de aventuras, lleno de experiencias. […] Ten siempre a Itaca en tu mente. Llegar allí es tu destino. Mas no apresures nunca el viaje. Mejor que dure muchos años y atracar, viejo ya, en la isla, enriquecido de cuanto ganaste en el camino sin aguantar a que Itaca te enriquezca."
                </p>
            </div>
            <h3 style="text-align: left;">Siguenos en</h3>
        

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

