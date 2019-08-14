<?php 

    $input = $_GET['search-box'];
    // Execute the python script with the JSON data
    $yiha = shell_exec('C:\Users\Shoumei\Documents\ALGEN\tgsalgen\bb.py ');
    $output= json_decode($yiha);
    ?>
            <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Algoritma Genetika</title>
            <link rel="stylesheet" href="bootstrap.min.css">
            <link rel="stylesheet" href="styles.min.css">
            <style type="text/css">
                .jumbotron{
                      background: url(aa.jpg) no-repeat center center;
                      background-position: 0% 53%;
                      background-size: cover ;
                      background-repeat: no-repeat;
                      text-align: center;
                      border-radius: 0%;
        /*  height: 350px;*/
        }
            </style>
        </head>


        <body>
            
            <!-- jumbotron -->
            <div class="jumbotron text-center">
              <img src="123.jpg"  style= "width: 10%; height: 10%" class="img-circle">
              <div id=papan style="width: inherit; height: 20%;  background: rgba(0,0,0,0.5);  ">
                  <h2 style="color: white;" >Welcome!</h2>
                  <h1 style="color: white;">Website Algoritma Genetika</h1>
              </div>
            </div>
            <!-- akhir jumbotron -->
    <div class="container">
    <h2 align="center">DAFTAR 10 Pura Di Bali</h2>
        <br>
        <div class="row">
          <div class="col-sm-12">
            <table class="table-striped" border="1" style="width: 100%">
                <tr>
                    <th>Index</th>
                    <th>Nama Tempat</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Pura Agung Jagatnatha</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Pura Besakih</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Pura Lempuyang Luhur</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Pura Goa Lawah</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Pura Tanah Lot</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Pura Tirta Empul</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>Pura Uluwatu</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td>Pura Taman Ayun</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td>Pura Ulun Danu</td>
                </tr>
                <tr>
                    <td>10</td>
                    <td>Pura Goa Gajah</td>
                </tr>
            </table>
          </div>
        </div>
        <br>
        <br>
    <h2 align="center">Perbandingan Variasi Algoritma Gapta,dkk dan Variasi Crosover Order, Mutasi Thrors, dan Seleksi Truncation</h2>
    <table border="1" style="width: 100%; margin-right:5%;">
    <?php
    echo '<br>';
    echo '<h3 align="center">Cromosom : </h3>';
    for($x=0;$x<5;$x++){
        echo "<tr >";
        echo "<td align='center'>";
        foreach($output->cromosoma[$x] as $list){
            echo $list.', ';
        }

    }
    echo "<tr>";
    ?>
    </table>
    <table border="1" style="width: 100%; margin-right:5%;">
                 <tr>
                <td style="font-weight: bold; font-size: 16px" align="center" colspan="4">Variasi Algoritma Genetika Order Crossover, Thrors Mutation, dan Truncation Mutation</td>
                 <td style="font-weight: bold; font-size: 16px" align="center" colspan="4">Variasi Gupta, dkk</td>
                 
                 </tr>'; 
                 <tr>
                 <td  align="center" style="font-weight: bold; font-size: 16px">RUTE</td>
                 <td  align="center" style="font-weight: bold; font-size: 16px">JARAK (km) </td>
                 <td  align="center" style="font-weight: bold; font-size: 16px">WAKTU</td>
                 <td  align="center" style="font-weight: bold; font-size: 16px">ITERASI</td>
                 <td  align="center" style="font-weight: bold; font-size: 16px">RUTE</td>
                 <td  align="center" style="font-weight: bold; font-size: 16px">JARAK (km) </td>
                 <td  align="center" style="font-weight: bold; font-size: 16px">WAKTU</td>
                 <td  align="center" style="font-weight: bold; font-size: 16px">ITERASI</td>    
                 </tr>
                 
    <?php
    
        echo "<tr>";
        echo "<td align='center'>";
        foreach($output->rute_mycode[0] as $list){
            echo $list.'-> ';
        }
        echo "</td>";
        echo "<td align='center'>";
        echo $output->tot_jalur_mycode[0];
        echo "</td>";
        echo "<td align='center'>";
        echo $output->waktu_mycode;
        echo "</td>";
        echo "<td align='center'>";
        echo $output->iterasi_mycode;
        echo "</td>";
        
        echo "<td  align='center' >";
        foreach($output->rute_gupta[0] as $list){
            echo $list.'->';
        }
        echo "</td>";
        echo "<td align='center'>";
        echo $output->tot_jalur_gupta[0];
        echo "</td>";
        echo "<td align='center'>";
        echo $output->waktu_gupta;
        echo "</td>";
        echo "<td align='center'>";
        echo $output->iterasi_gupta;
        echo "</td>";
        echo "</tr>";
    
    echo '</table>';
    
    echo '<br>';
  
?>
   <!--  <h2 align="center">HASIL PROSES PENCARIAN RUTE TERPENDEK DENGAN 2-POINT CROSSOVER, INTERCHANGE MUTATION, DAN TRUNCATION SELECTION</h2>
    <table border="1" style="width: 100%; margin-right:5%;">
    <?php
    echo '<br>';
    echo '<h3 align="center">Cromosom : </h3>';
    for($x=0;$x<5;$x++){
        echo "<tr>";
        echo "<td align='center'>";
        foreach($output->cromosoma[$x] as $list){
            echo $list.', ';
        }

    }
    echo "<tr>";
    ?>
    </table>
    <table border="1" style="width: 100%; margin-right:5%;">
                 <tr>
                 <th style=" backround-color:"red;"">RUTE</th>
                 <th style=" backround-color:"red;"">JARAK (km) </th>
                 <th style=" backround-color:"red;"">Pemakaian BBM Blade (liter)</th>
                 <th style=" backround-color:"red;"">Pemakaian BBM Vario (liter)</th>
                 <th style=" backround-color:"red;"">Pemakaian BBM CBR (liter)</th>
                 <th style=" backround-color:"red;"">Pemakaian BBM Beat (liter)</th>
                 </tr>'; 
    <?php
    echo '<br>';
    for($x=0;$x<5;$x++){
        echo "<tr>";
        echo "<td>";
        foreach($output->rute_gupta[$x] as $list){
            echo $list.', ';
        }
        echo "</td>";
        echo "<td>";
        echo $output->tot_jalur_gupta[$x];
        echo "</td>";
        echo "<td>";
        echo $output->konblade_gupta[$x];
        echo "</td>";
        echo "<td>";
        echo $output->konvario_gupta[$x];
        echo "</td>";
        echo "<td>";
        echo $output->koncbr_gupta[$x];
        echo "</td>";
        echo "<td>";
        echo $output->konbeat_gupta[$x];
        echo "</td>";

        echo "</tr>";
    }
    echo '</table>';
    echo '<br>';
    echo '<h5>Jumlah Iterasi : </h5>';
    echo $output->iterasi_gupta ;
    echo '<h5>Waktu Proses (detik): </h5>';
    echo $output->waktu_gupta ;
    echo '<br>';

    
?> -->
<?php
    echo '<br>';
    echo '<a href="Testing_form.php" class="btn btn-primary" style="width:inherit;">KEMBALI<a>';
    echo '<br>';
    echo '<br>';
    echo '<br>';
    echo '<br>';
    echo '<br>';
?>
</div>
<script src="assets/js/jquery.min.js"></script>
<script src="assets/bootstrap/js/bootstrap.min.js"></script>
</body>

</html>