<!DOCTYPE html>
<html lang="zxx">

<head>
    <meta charset="UTF-8">
    <meta name="description" content="Sales Predictor">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Sales Predictor</title>

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css?family=Quantico:400,700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600,700&display=swap" rel="stylesheet">

    <!-- Css Styles -->
    <link rel="stylesheet" href="css/bootstrap.min.css" type="text/css">
    <link rel="stylesheet" href="css/font-awesome.min.css" type="text/css">
    <link rel="stylesheet" href="css/elegant-icons.css" type="text/css">
    <link rel="stylesheet" href="css/owl.carousel.min.css" type="text/css">
    <link rel="stylesheet" href="css/magnific-popup.css" type="text/css">
    <link rel="stylesheet" href="css/slicknav.min.css" type="text/css">
    <link rel="stylesheet" href="css/style.css" type="text/css">
</head>

<body>
    <!-- Page Preloder -->
    <div id="preloder">
        <div class="loader"></div>
    </div>

    <!-- Header Section Begin -->
    <header class="header-section header-normal">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <div class="logo">
                        <a href="./index.html">
                            <img src="img/logo.jpg" alt="" height="30" width = "75">
                        </a>
                    </div>
                    <nav class="nav-menu mobile-menu">
                        <ul>
                            <li><a href="./index.html">Home</a></li>
                            <li ><a href="./visualize.html">Visualize</a></li>
                            <li ><a href="./predict.html">Predict</a></li>
                            <li ><a href="./generate_v.php">Generate Visualizations</a></li>
                            <li class="active"><a href="./generate_p.php">Generate Predictions</a></li>
                            <li><a href="./analyze.php">Analyze</a></li>
                        </ul>
                    </nav>
                    <div id="mobile-menu-wrap"></div>
                </div>
            </div>
        </div>
    </header>
    <!-- Header End -->

    <!-- Breadcrumb Begin -->
    <div class="breadcrumb-option spad">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="bo-links">
                        <a href="./index.html"><i class="fa fa-home"></i> Home</a>
                        <span>Generate Predictions</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Breadcrumb End -->
    <section class="about-section">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-6 p-0">
                    <div class="about-text">
                        <div class="section-title">
                          <h2>Generating Predictions</h2>
                        <p>Please click on the following button to create prediction results!</p>
                        <button onclick = "window.location.href = 'predictions.php';"> Generate </button>
                        <p> Please be patient while the prediction results are being generated. It might take 10-15 minutes.</p>
                        </div>

                    </div>
                        </div>
                    </div>
                </div>
            </div>
    </section>
    <!-- Visualize Section End -->

    <!-- Js Plugins -->
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/jquery.magnific-popup.min.js"></script>
    <script src="js/isotope.pkgd.min.js"></script>
    <script src="js/masonry.pkgd.min.js"></script>
    <script src="js/jquery.slicknav.js"></script>
    <script src="js/owl.carousel.min.js"></script>
    <script src="js/main.js"></script>
</body>

</html>
<?php
set_time_limit(2000);
$pyscript = "C:\\wamp64\\www\\SalesForecastProject\\Sales_forecast_predict.py";
$python = "C:\\Users\sony\\AppData\\Local\\Programs\\Python\\Python38\\python.exe";

$cmd = "$python $pyscript";

exec("$cmd");
echo "ALL PREDICTION RESULTS GENERATED!!", PHP_EOL;
echo "\n YOU CAN SEE THE RESULTS DIAGRAMS UNDER PREDICT TAB! ", PHP_EOL;
echo "\n YOU CAN SEE THE RESULT STATISTICS UNDER ANALYZE TAB!";
?>
