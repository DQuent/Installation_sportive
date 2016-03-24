
<!DOCTYPE html>
<html>
	<head>
		<title>Sport / Ville - Pays de la Loire</title>
		<!-- <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
		<!-- Bootstrap -->
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<script src="http://code.jquery.com/jquery.js"></script>
		<script src="static/bootstrap/js/bootstrap.min.js"></script>
		<link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet">
		<link href="static/perso.css" rel="stylesheet">
		<script src="static/perso.js"></script>
		  <script src="http://maps.google.com/maps/api/js?sensor=false" 
          type="text/javascript"></script>

	</head>
	<body style="padding-top:70px">

		<nav class="navbar navbar-inverse navbar-fixed-top">
	      <div class="container">
	        <div class="navbar-header">
	          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
	            <span class="sr-only">Navigation</span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	          </button>
	          <a class="navbar-brand" href="/">Sport / Ville - PDL</a>
	        </div>
	        <div id="navbar" class="navbar-collapse collapse">
	          <ul class="nav navbar-nav">
	            <li><a  href="/">Chercher</a></li>
	            <li><a href="#">Resultat</a></li>
	            <li><a href="#">Carte</a></li>
	            <li><a data-toggle="modal" data-target="#myModal">A propos</a></li>
	          </ul>
	        </div><!--/.nav-collapse -->
	      </div>
	    </nav>

	    <div class="container">
	    	<h1>Cherche les installations d'une ville</h1>
	    	<div class="row">
	    		<div class="col-md-6">
			    	<form class="form-horizontal" action='/map2' method='POST'>
			    		<label for="ville" class="col-sm-1 control-label">Ville</label>
			    			<div class="col-sm-6">
			    				<input type="text" class="form-control" id="ville" placeholder="Ville" name="ville">
			    				<br>
			     			</div>
			     			<div class="col-sm-2">
			     				<button type="submit" class="btn btn-primary">Chercher</button>
			     				<br>
			     			</div>	
			    	</form>
			    </div>
			</div>    	
				



		    	<div class="row">
		    		<div class="col-md-1">
		    		</div>
		    		<div class="col-md-10">
		    			<div id="map" style="width: 1000px; height: 500px;"></div>
		    		</div>
		    		<div class="col-md-1">
		    		</div>
					  <script type="text/javascript">
					    var locations = [
					    ];

					    var map = new google.maps.Map(document.getElementById('map'), {
					      zoom: 10,
					      center: new google.maps.LatLng(-33.92, 151.25),
					      mapTypeId: google.maps.MapTypeId.ROADMAP
					    });

					    var infowindow = new google.maps.InfoWindow();

					    var marker, i;

					    for (i = 0; i < locations.length; i++) {  
					      marker = new google.maps.Marker({
					        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
					        map: map
					      });

					      google.maps.event.addListener(marker, 'click', (function(marker, i) {
					        return function() {
					          infowindow.setContent(locations[i][0]);
					          infowindow.open(map, marker);
					        }
					      })(marker, i));
					    }
					  </script>
				</div>




		<!-- About modal content -->
		<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		  <div class="modal-dialog">
		    <div class="modal-content">
		      <div class="modal-header">
		        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		        <h4 class="modal-title" id="myModalLabel">A propos du projet</h4>
		      </div>
		      <div class="modal-body">
		        Les données sont issues du site disponible <a href="http://data.paysdelaloire.fr/" target="_blank"> ici </a>.
		        <br><br>
		        L'énoncé du problème auquel ce projet répond est disponible sur le <a HREF="https://github.com/sebprunier/installations-sportives-pdl" target="_blank">GitHub de Sébastien Prunier</a>
		      </div>
		      <div class="modal-footer">
		        <button type="button" class="btn btn-default" data-dismiss="modal">Fermer</button>
		      </div>
		    </div>
		  </div>
		</div>


		<!-- Footer -->
		<nav class="navbar-fixed-bottom">
		    <h5 class="text-center">Delanou Quentin</h5>
		</nav>
	</body>
</html>

