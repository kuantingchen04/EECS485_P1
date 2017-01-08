<?php
function createThumbs( $pathToImages, $pathToThumbs, $thumbWidth ,$thumbHeight ) 
{
  // open the directory
  $dir = opendir( $pathToImages );

  // loop through it, looking for any/all JPG files:
  while (false !== ($fname = readdir( $dir ))) {
    // parse path for the extension
    $info = pathinfo($pathToImages . $fname);
    // continue only if this is a JPEG image
    if ( strtolower($info['extension']) == 'jpg' ) 
    {
      //echo "Creating thumbnail for {$fname} <br />";

      // load image and get image size
      $img = imagecreatefromjpeg( "{$pathToImages}{$fname}" );
      echo $img;
      $width = imagesx( $img );
      $height = imagesy( $img );

      // calculate thumbnail size
      if ($width>$height)
      {
        $new_width = $thumbWidth;
        $new_height = floor( $height * ( $thumbWidth / $width ) );
      }
      else
      {
        $new_height = $thumbHeight;
        $new_width = floor( $width * ( $thumbHeight / $height ) );
      }

      // create a new temporary image
      $tmp_img = imagecreatetruecolor( $new_width, $new_height );

      // copy and resize old image into new image 
      imagecopyresized( $tmp_img, $img, 0, 0, 0, 0, $new_width, $new_height, $width, $height );

      // save thumbnail into a file
      imagejpeg( $tmp_img, "{$pathToThumbs}{$fname}" );
    }
    else if ( strtolower($info['extension']) == 'txt' ) 
    {
      //$img = 'reference_picture/'
    }
  }
  // close the directory
  closedir( $dir );
}
// call createThumb function and pass to it as parameters the path 
// to the directory that contains images, the path to the directory
// in which thumbnails will be placed and the thumbnail's width. 
// We are assuming that the path will be a relative path working 
// both in the filesystem, and through the web for links
//createThumbs("upload/","upload/thumbs/",100);
?>
<?php
function createGallery( $pathToImages, $pathToThumbs ) 
{
date_default_timezone_set('Asia/Taipei');
  //echo "Creating gallery.html <br />";

  //$output = "<html>";
  //$output .= "<head><title>Thumbnails</title></head>";
  //$output .= "<body>";
  //$output .= "<table cellspacing=\"0\" cellpadding=\"2\" width=\"500\">";
  //$output .= "<tr>";

  // open the directory
  $dir = opendir( $pathToImages );

  $counter = 0;
  // loop through the directory
  while (false !== ($fname = readdir($dir)))
  {
    #echo $fname;
    // strip the . and .. entries out
    $info = pathinfo($pathToImages . $fname);
    // continue only if this is a JPEG image

      if ($fname != '.' && $fname != '..' && $fname!= '.DS_Store') 
      {
         // echo "<a href=\"#\" class=\"thumbnail\">"
        if ( strtolower($info['extension']) == 'jpg' or strtolower($info['extension']) == 'png' ) 
        {
          $thumbnail_name='_'.$fname;
          $thumb_source = "{$pathToThumbs}{$thumbnail_name}";
        }
        if (!file_exists($thumb_source)) 
          $thumb_source = "reference_picture/picture_thumbnail.jpg";
        else if( strtolower($info['extension']) == 'txt' ) 
          $thumb_source = "reference_picture/text_thumbnail.png";
        else 
           $thumb_source = "reference_picture/file_thumbnail.png";
        /*$output .= "<td valign=\"middle\" align=\"center\"><a href=\"{$pathToImages}{$fname}\">";
        if ( strtolower($info['extension']) == 'jpg' ) 
          $output .= "<img src=\"{$pathToThumbs}{$fname}\" border=\"0\" />";
        else if( strtolower($info['extension']) == 'txt' ) 
          $output .= "<img src=\"reference_picture/text_thumbnail.png\" border=\"0\" />";
        else 
           $output .= "<img src=\"reference_picture/file_thumbnail.png\" border=\"0\" />";
        $output .= "</a></td>";*/
          // echo "<div class=\"row\">";
           #echo "<div class=\"span3\">";
     echo "<div class=\"col-sm-6 col-md-3\">";
   
      
      echo"        <div class=\"thumbnail\">
          <img src=\"$thumb_source\" max-width:\"200\" max-height:\"150\"
         alt=\"Generic placeholder thumbnail\"></div>";
     echo" <div class=\"caption\">
               <h3>".$fname."</h3>";
    echo"<p> Size: ". formatSizeUnits(filesize($pathToImages.$fname))." </p>"; 
    echo "<p>Last modified: " . date ("F d Y H:i:s.", filemtime($pathToImages.$fname))."</p>";
    echo"<p>
         <a href=\"{$pathToImages}{$fname} \"class=\"btn btn-primary\" role=\"button\">
               Download
            </a> 

         </p>
     
    </div>";//  
   echo "</div>";//col sm 6
  // echo "</li>";
   #echo "</div>";//span3
   //echo "</div>";//row
    $counter += 1;
     //if ( $counter % 4 == 0 ) { echo "</tr><tr>"; }
      }
    
  }
  // close the directory
  closedir( $dir );

  //$output .= "</tr>";
  //$output .= "</table>";
  //$output .= "</body>";
  //$output .= "</html>";

  // open the file
  //$fhandle = fopen( "gallery.html", "w" );
  // write the contents of the $output variable to the file
  //fwrite( $fhandle, $output ); 
  // close the file
  //fclose( $fhandle );
  return $output;
}
// call createGallery function and pass to it as parameters the path 
// to the directory that contains images and the path to the directory
// in which thumbnails will be placed. We are assuming that 
// the path will be a relative path working 
// both in the filesystem, and through the web for links
 function formatSizeUnits($bytes)
    {
        if ($bytes >= 1073741824)
        {
            $bytes = number_format($bytes / 1073741824, 2) . ' GB';
        }
        elseif ($bytes >= 1048576)
        {
            $bytes = number_format($bytes / 1048576, 2) . ' MB';
        }
        elseif ($bytes >= 1024)
        {
            $bytes = number_format($bytes / 1024, 2) . ' KB';
        }
        elseif ($bytes > 1)
        {
            $bytes = $bytes . ' bytes';
        }
        elseif ($bytes == 1)
        {
            $bytes = $bytes . ' byte';
        }
        else
        {
            $bytes = '0 bytes';
        }

        return $bytes;
}
?>