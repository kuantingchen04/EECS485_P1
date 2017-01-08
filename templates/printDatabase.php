<?php
ignore_user_abort(true);
set_time_limit(0);
$interval = 10;
$dbname='example.db';
$mytable = 'filenames';
//$mytable2 = 'trash';

do{
    $base=new SQLiteDatabase($dbname, 0666, $err);
	if ($err) exit($err);
	$query = "SELECT * from $mytable";
	$results = $base->queryExec($query);
	while($row = sqlite_fetch_array($result)){
		$handle = fopen('file_record.txt','w');
		fwrite($handle, $row);
	}
    sleep($interval);
}while(true);
?>