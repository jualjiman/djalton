/* Begin Of jQuery or JS Custom Scripts - This line of codemust stay intact */
jQuery( document ).ready( function ( $ )
{
    /* Markers */
    var myMarkers = {
        "markers": [
            {
                "latitude": "16.867572",
                "longitude": "-99.898213",
                "icon": "images/marker.png",
                "baloon_text": ''
            }]
    };

    //set up map options
    $( ".map" ).mapmarker(
    {
        zoom: 15,
        center: "Tepic 12, Acapulco, GRO, México",
        markers: myMarkers
    } );

    $( '.select-input select, .light-select-input select, .dark-select-input select' ).chosen(
    {
        disable_search: true,
        width: '100%',
    } );


    /* NAV */
    $( 'ul.sub-menu' ).hide( );
    $( 'ul.main-navigation li' ).hover( function ( )
    {
        $( this ).children( 'ul.sub-menu' ).stop( true, true, true ).slideDown( 300 );
    }, function ( )
    {
        $( this ).children( 'ul.sub-menu' ).stop( true, true, true ).slideUp( 0 );
    } );

    $( 'ul.sub-menu li' ).hover( function ( )
    {
        $( this ).children( 'ul.sub-menu li > ul.sub-menu' ).fadeIn( 300 );
    }, function ( )
    {
        $( this ).children( 'ul.sub-menu li > ul.sub-menu' ).fadeOut( 0 );
    } );


    /** Stay Active Until Sub Nav Active **/
    $( 'ul.main-navigation li ul, ul.sub-nav ' ).hover(
        function ( )
        {
            $( this ).parent( 'li' ).children( 'a' ).addClass( 'active' );
        },
        function ( )
        {
            $( this ).parent( 'li' ).children( 'a' ).removeClass( 'active' );
        } );



    if ( $( 'ul.sub-menu li' ).has( ).children( 'ul' ) )
    {
        $( 'ul.sub-menu li > ul' ).parent( 'li' ).children( 'a' ).append( ' <span style="float:right; display:inline-block; padding-right:15px;">&raquo;</span>' );
    }


    /* RESPONSIVE NAV */

    // Create the dropdown base
    $( "<select />" ).appendTo( ".main-nav" );

    // Create default option "Go to..."
    $( "<option />",
    {
        "selected": "selected",
        "value": "",
        "text": "NAVIGATION..."
    } ).appendTo( ".main-nav select" );
    // Populate dropdown with menu items
    $( ".main-nav ul.main-navigation li a" ).each( function ( )
    {
        var el = $( this );
        $( "<option />",
        {
            "value": el.attr( "href" ),
            "text": el.text( )
        } ).appendTo( ".main-nav select" );
    } );

    $( ".main-nav select" ).change( function ( )
    {
        window.location = $( this ).find( "option:selected" ).val( );
    } );

    /* search */
    $( '.nav-search span.icon-search' ).click( function ( )
    {
        $( '.nav-search span.icon-search' ).toggleClass( 'orange' );
        $( '.nav-search input' ).stop( true, true, true ).toggle( 'slide',
        {
            direction: 'right'
        }, 300 );
    } );




    /* main search toggle */
    $( '.advanced-search-fields' ).hide( );
    $( '.search-right button' ).click( function ( )
        {
            $( '.main-search' ).slideUp( 'fast' );
            $( '.main-search' ).slideDown( 'slow' );
            $( '.advanced-search-fields' ).toggle( ).delay( 1000 );
            $( '.search-right button > span' ).toggleClass( 'icon-plus' ).toggleClass( 'icon-minus' );
            $( '.quick-search-fields' ).toggle( ).delay( 1000 );


        }


    );



    /* revolution slider */
    jQuery( '.banner' ).revolution(
    {
        delay: 9000,
        startwidth: 1170,
        startheight: 500,
        autoHeight: "on",
        fullScreenAlignForce: "off",

        onHoverStop: "on",

        thumbWidth: 100,
        thumbHeight: 50,
        thumbAmount: 3,

        hideThumbsOnMobile: "true",
        hideBulletsOnMobile: "false",
        hideArrowsOnMobile: "true",
        hideThumbsUnderResoluition: 0,

        hideThumbs: 0,
        navigationType: "hide",
        navigationArrows: "solo",
        navigationStyle: "round",

        navigationHAlign: "center",
        navigationVAlign: "top",
        navigationHOffset: 60,
        navigationVOffset: 30,

        soloArrowLeftHalign: "right",
        soloArrowLeftValign: "bottom",
        soloArrowLeftHOffset: 280,
        soloArrowLeftVOffset: 230,

        soloArrowRightHalign: "right",
        soloArrowRightValign: "bottom",
        soloArrowRightHOffset: 220,
        soloArrowRightVOffset: 230,


        touchenabled: "on",

        stopAtSlide: -1,
        stopAfterLoops: -1,
        hideCaptionAtLimit: 0,
        hideAllCaptionAtLilmit: 0,
        hideSliderAtLimit: 0,

        dottedOverlay: "",

        fullWidth: "on",
        forceFullWidth: "off",
        fullScreen: "off",
        fullScreenOffsetContainer: "#topheader-to-offset",

        shadow: 0

    } );

    jQuery( '.banner-single' ).revolution(
    {
        delay: 9000,
        startwidth: 1170,
        startheight: 620,
        autoHeight: "off",
        fullScreenAlignForce: "off",

        onHoverStop: "on",

        thumbWidth: 100,
        thumbHeight: 50,
        thumbAmount: 3,

        hideThumbsOnMobile: "true",
        hideBulletsOnMobile: "true",
        hideArrowsOnMobile: "true",
        hideThumbsUnderResoluition: 0,

        hideThumbs: 0,
        navigationType: "square",
        navigationArrows: "solo",
        navigationStyle: "square",

        navigationHAlign: "center",
        navigationVAlign: "bottom",
        navigationHOffset: 60,
        navigationVOffset: 30,

        soloArrowLeftHalign: "right",
        soloArrowLeftValign: "bottom",
        soloArrowLeftHOffset: 80,
        soloArrowLeftVOffset: 20,

        soloArrowRightHalign: "right",
        soloArrowRightValign: "bottom",
        soloArrowRightHOffset: 20,
        soloArrowRightVOffset: 20,


        touchenabled: "on",

        stopAtSlide: -1,
        stopAfterLoops: -1,
        hideCaptionAtLimit: 0,
        hideAllCaptionAtLilmit: 0,
        hideSliderAtLimit: 0,

        dottedOverlay: "none",

        fullWidth: "on",
        forceFullWidth: "off",
        fullScreen: "off",
        fullScreenOffsetContainer: "#topheader-to-offset",

        shadow: 0

    } );

    $( ".to-top" ).hide( );
    $( function ( )
    {
        $( window ).scroll( function ( )
        {
            if ( $( this ).scrollTop( ) > 500 )
            {
                $( '.to-top' ).fadeIn( );
            }
            else
            {
                $( '.to-top' ).fadeOut( );
            }
        } );

        // scroll body to 0px on click
        $( '.to-top a' ).click( function ( )
        {
            $( 'body,html' ).animate(
            {
                scrollTop: 0
            }, 800 );
            return false;
        } );
    } );

    /* Tabs */
    $( ".h-tab" ).easyResponsiveTabs(
    {
        type: 'default',
    } );

    $( ".accordion" ).easyResponsiveTabs(
    {
        type: 'accordion',
    } );

    $( ".v-tab" ).easyResponsiveTabs(
    {
        type: 'vertical',
    } );

    /* Carell Animate Elements */
    $( "[data-appear-animation]" ).each( function ( )
    {
        var $this = $( this );
        $this.addClass( "carell-animation" );
        if ( !$( "html" ).hasClass( "no-csstransitions" ) && $( window ).width( ) > 767 )
        {
            $this.appear( function ( )
            {
                var delay = ( $this.attr( "data-appear-delay" ) ? $this.attr( "data-appear-delay" ) : 1 );
                if ( delay > 1 ) $this.css( "animation-delay", delay + "ms" );
                $this.addClass( $this.attr( "data-appear-animation" ) ).addClass( "carell-animation-visible" );
                setTimeout( function ( )
                {
                    $this.addClass( "carell-animation-visible" );
                }, delay );
            },
            {
                accX: 0,
                accY: -100
            } );
        }
        else
        {
            $this.addClass( "carell-animation-visible" );
        }
    } );



    /* Carell Knob */

    if ( $( '.knob' ).parent( '.progress-bar' ).hasClass( 'carell-animation' ) )
    {
        $( ".knob" ).each( function ( )
        {

            var $this = $( this );
            var myVal = $this.val( );



            $this.addClass( "carell-animation" );

            $this.knob( );
            $this.appear( function ( )
            {

                var delay = ( $this.attr( "data-appear-delay" ) ? $this.attr( "data-appear-delay" ) : 1 );
                if ( delay > 1 ) $this.css( "animation-delay", delay + "ms" );
                $this.addClass( $this.attr( "data-appear-animation" ) ).addClass( "carell-animation-visible" );
                setTimeout( function ( )
                {

                    $(
                    {
                        value: 0
                    } ).animate(
                    {
                        value: myVal
                    },
                    {
                        duration: 2000,
                        easing: 'swing',
                        step: function ( )
                        {
                            $this.val( Math.ceil( this.value ) ).trigger( 'change' );
                        }
                    } );
                    $this.addClass( "carell-animation-visible" );
                }, delay );
            },
            {
                accX: 0,
                accY: -0
            } );


        } );

    }
    else
    {
        $( '.knob' ).each( function ( )
        {
            var $this = $( this );
            var myVal = $this.val( );
            $this.knob( );
            $(
            {
                value: 0
            } ).animate(
            {
                value: myVal
            },
            {
                duration: 1000,
                easing: 'swing',
                step: function ( )
                {
                    $this.val( Math.ceil( this.value ) ).trigger( 'change' );
                }
            } );
        } );
    }

    /* Lightboxes Modals */

    $( '.popup-modal' ).magnificPopup(
    {
        removalDelay: 500,
        type: 'inline',
        midClick: true,
        callbacks:
        {
            beforeOpen: function ( )
            {
                this.st.mainClass = this.st.el.attr( 'data-effect' );
            }
        },
    } );

    $( '.popup-image' ).magnificPopup(
    {
        removalDelay: 500,
        type: 'image',
        midClick: true,
        callbacks:
        {
            beforeOpen: function ( )
            {
                this.st.mainClass = this.st.el.attr( 'data-effect' );
            }
        },
    } );

    $( '.popup-gallery' ).each( function ( )
    {
        $( this ).magnificPopup(
        {
            removalDelay: 500,
            midClick: true,
            delegate: 'a',
            type: 'image',
            gallery:
            {
                enabled: true
            },
            callbacks:
            {
                beforeOpen: function ( )
                {
                    this.st.mainClass = this.st.el.attr( 'data-effect' );
                }
            },
        } );
    } );

    /* car boxes responsiveness */

    if ( $( window ).width( ) < 769 )
    {
        $( '.car-box' ).removeClass( 'horizontal small' );
        $( '.car-box' ).addClass( 'vertical small' );
    }
    else
    {

    }

    /* Count Down */
    $( '.carell-count-down' ).dsCountDown(
    {

        endDate: new Date( "January 18, 2014 11:13:00" )
    } );

    /* On click hide */
    $( '.on-click-hide' ).css(
    {
        'cursor': 'pointer'
    } );
    $( '.on-click-hide' ).click( function ( )
    {

        $( this ).fadeOut( 300 );
    } );

    /* Z-index */
    $( '.main-search' ).css(
    {
        'position': 'relative',
        'z-index': '999'
    } );
    if ( $( '.row' ).has( '.light-select-input' ) )
    {
        $( '.light-select-input' ).closest( '.row' ).css(
        {
            'position': 'relative',
            'z-index': '998'
        } );
    }

    $(".submitform").click(function(e){
        e.preventDefault();

         var name = $('#id_name').val();
         var email = $('#id_email').val();
         var phonenumber = $('#id_phonenumber').val();
         var message = $('#id_message').val();

         alert($('input[name="csrfmiddlewaretoken"]').val());

        if( name !== "" && email !== "" && message !== ""){
            $.ajax({
                type: "POST",
                url: "/contactoEmail/",  // or just url: "/my-url/path/"
                data: {
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                    name: $('#id_name').val(),
                    email: $('#id_email').val(),
                    phonenumber: $('#id_phonenumber').val(),
                    message: $('#id_message').val()
                },
                success: function(data) {
                    alert("Congratulations! You scored: "+data);
                },
                error: function(xhr, textStatus, errorThrown) {
                    alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
                }
            });
        }
        else{
            alert("noup!");
        }
    });

	/* contact form */
	// $('.submitform').click(function(e){
	// 	e.preventDefault();
        
		
	// 	var name = $('input[name="name"]').val();
	// 	var email = $('input[name="email"]').val();
	// 	var phonenumber = $('input[name="phonenumber"]').val();
	// 	var message = $('textarea[name="message"]').val();
	// 	var email_regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;


	// 	if( name !== "" && email !== "" && phonenumber !== "" && message !== ""){
	// 		if( email_regex.test(email) === true ){
	// 			$.post(
	// 				$('.contactform').attr('action'),
	// 				{
	// 					name:name,
	// 					email:email,
	// 					phonenumber:phonenumber,
	// 					message:message
	// 				},
	// 				function(response){
	// 					if( response.indexOf("[OK]") !== -1 ){
	// 						$('.send_result').text('Mensaje enviado, en breve le atenderemos.').hide().fadeIn();
	// 						$('input[name="name"]').val("");
	// 						$('input[name="email"]').val("");
	// 						$('input[name="phonenumber"]').val("");
	// 						$('textarea[name="message"]').val("");
	// 					}
	// 					else{
	// 						$('.send_result').text('Error al enviar el mensaje.').hide().fadeIn();
	// 					}
	// 				}
	// 			);
	// 		}
	// 		else{
	// 			$('.send_result').text('El formato de email que ingreso es invalido.').hide().fadeIn();
	// 		}
	// 	}
	// 	else{
	// 		$('.send_result').text('Todos los campos son requeridos.').hide().fadeIn();
	// 	}
	// });	
    /*end submitform*/
	
    $(".car-price .clearfix .price").on("click",function( evt ){
        evt.preventDefault();
    });

    $(".car-price .clearfix .icon-arrow-right2").on("click",function( evt ){
        evt.preventDefault();
    });

    $(".car-title h3 a").on("click",function( evt ){
        evt.preventDefault();
    });
    /* End Of jQuery or JS Custom Scripts - This line of code must stay intact */
} );