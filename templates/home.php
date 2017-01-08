<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Home</title>

    <!-- Bootstrap core CSS -->
    <link href="dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap theme -->
    <link href="dist/css/bootstrap-theme.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="theme.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="../../assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
   <style>
  body {
    background-image: url("http://i.imgur.com/dICOJo8.jpg");
  background-size:100%;
  background-repeat: no-repeat;
    background-attachment: fixed;

}
.jumbotron 
    {
      background: rgba(255,255,255, 0.7); 
    width:100%;
    padding: 10%;
  }
  .thumbnail {
    background: rgba(255,255,255, 0);
    padding:4px;
    overflow: auto;
    height:100%; 
    width: 100%;
    max-width: :200px;
}
  #footer {
    background-color:black;
    color:white;
    clear:both;
    text-align:center;
    padding:5px;   
  background: rgba(0,0,0, 0.7);    
  }

</style>


  <body role="document">

    <!-- Fixed navbar -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="home.php">Your Cloud</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
          <li class="active"><a href="home.php">Home</a></li> 
            <li><a href="files.php">File</a></li>
            <li><a href="Mobile.php">Mobile</a></li>
            <li><a href="RecycleBin.php">Recycle Bin</a></li>
            
            
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container theme-showcase" role="main">

      <!-- Main jumbotron for a primary marketing message or call to action -->
      <div class="jumbotron">
        <h1>Home</h1>
        <p>Welcome to this website.</p>
     <!--  <p><a href="search_the_folder.html" class="btn btn-primary btn-lg" role="button">Search the folder &raquo;</a></p> -->
      </div>
     
  <div id="footer">
Copyright ESLAB 2014 autumn
</div>    

</div>
   </body>

   </html>





