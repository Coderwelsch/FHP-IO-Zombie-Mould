// global vars
var requiredScripts = [
		'jquery/jquery-2.1.3.min'
	],
	
	$loadingOverlay,
	$nav,
	$pagePosHeadline,
	$muteBtn,
	$soundMainTheme,
	$teaserView;


// main functions
function fadeOutLoadingOverlay () {
	$loadingOverlay.addClass( 'loaded' );
}

function showTeaserView () {
	$teaserView.addClass( 'active' );

	setTimeout( function () { $loadingOverlay.removeClass( 'active' ) }, 2000 );
}

function navClicked ( event ) {
	if ( $( event.target ).hasClass( 'mute-btn' ) ) {
		return;
	}

	$( this ).find( 'ul' ).toggleClass( 'active' );
}

function resizeBrowser () {
	var scrollTop = $( window.location.hash.toLowerCase() ).offset().top;
	$( 'html, body' ).scrollTop( scrollTop );
}

function anchorItemClicked () {
	var targetViewSelector = $( this ).attr( 'href' ),
		$this = $( this ),
		$targetView = $( targetViewSelector );

	if ( $targetView.length === 1 ) {
		$( 'body > div.view' ).removeClass( 'start-animation' );
		$targetView.addClass( 'start-animation' );

		$('html, body').animate({
        	scrollTop: $targetView.offset().top
    	}, 1000);

    	setTimeout( function () {
    		$pagePosHeadline.text( $this.text() );

    		window.location.hash = targetViewSelector.toUpperCase();
    	}, 1000 );
	}

	$nav.find( 'ul' ).removeClass( 'active' );

	return false;
}

function scrollToTop () {
	$( 'html, body' ).scrollTop( 0 );
}

function muteBtnClicked () {
	$( this ).toggleClass( 'active' );

	if ( $( this ).hasClass( 'active' ) ) {
		$soundMainTheme[ 0 ].pause();
	}else {
		$soundMainTheme[ 0 ].play();
	}
}


// init functions
function initVariables () {
	$nav = $( '.navigation' );
	$pagePosHeadline = $nav.find( '.page-pos-headline' );
	$muteBtn = $nav.find( '.mute-btn' );
	$loadingOverlay = $( '.main-loading-overlay-view' );
	$teaserView = $( '.teaser-view' );
	$soundMainTheme = $( '.sound-main-theme' );
}

function bindEvents () {
	$( window ).on( 'resize', resizeBrowser );

	$nav.on( 'click', navClicked );
	$nav.on( 'click', 'a', anchorItemClicked );
	$muteBtn.on( 'click', muteBtnClicked );
}

function main () {
	scrollToTop();
	fadeOutLoadingOverlay();
	showTeaserView();
}

function init () {
	initVariables();
	bindEvents();
	main();
}

function error ( errorMessage ) {
	console.error( errorMessage );
}

require( requiredScripts, init, error );