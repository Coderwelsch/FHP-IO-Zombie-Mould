<?php
	if ( isset( $_POST[ 'json' ] ) ) {
		$file = fopen( '../json/cachedURLs.json', 'w+' );
		fwrite( $file, $_POST[ 'json' ] );
		fclose( $file );

		echo 'success';
	} else {
		echo 'error';
	}
?>