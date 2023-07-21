/*global $*/
$(document).ready(function () {

    "use strict";

    $(".color-gray").on("click", function () {
       $("body").toggleClass("site-gray");
    });

    // Add Alt Attribute
    function addAltHome() {
        $(".section-post-media").each(function() {
            var eventName = $(this).parent().find(".sct_blog_name").text();
            $(this).attr('alt',eventName);
        })
    }
    function addAltNews() {
        $(".o_wblog_post .o_record_cover_image").each(function() {
            var eventName = $(this).parents(".o_wblog_post").find(".o_blog_post_title").text();
            $(this).attr('alt',eventName);
        })
    }
    function addAltEvents() {
        $(".o_wevent_events_list .o_record_cover_image").each(function() {
            var eventName = $(this).parents("article.card").find(".card-title span").text();
            $(this).attr('alt',eventName);
        })
    }
    function addAltSingleNews() {
        $("#o_wblog_post_top .o_record_cover_image").each(function() {
            var eventName = $(this).parents("#o_wblog_post_top").find("#o_wblog_post_name").text();
            $(this).attr('alt',eventName);
        })
    }
    function addAltSingleEvents() {
        $(".o_wevent_event .o_record_cover_image").each(function() {
            var eventName = $(this).parents(".o_record_cover_container").find(".o_wevent_event_name").text();
            $(this).attr('alt',eventName);
        })
    }
    setTimeout(() => {
        addAltHome();
        addAltNews();
        addAltEvents();
        addAltSingleNews();
        addAltSingleEvents();
    },1000);

    // Control Font Size
    if ($('#fontLarge').length > 0) {
        var resizabletxt = 'body';
        $.creaseFont({
            content: resizabletxt,
            unit: 'px',
            defaultSize: 16,
            maxSize: 20,
            minSize: 12,
            bFontLarge: '#fontLarge',
            bFontDefault: '#fontDefault',
            bFontSmall: '#fontSmall',
            animate: false,
            cookieLifetime: 0,
            stepSize: 1
        });
    }

    $("html body #wrapwrap.homepage .our-rules-page .item").hover( function () {
        $(this).find("p").slideDown();
    }, function () {
        $(this).find("p").slideUp();
    });

    $(".sustainability .options .option").click(function () {
        $(this).addClass("active").siblings().removeClass("active");
    });
    $(".sustainability .options .option").hover(function () {
        $(this).addClass("active").siblings().removeClass("active");
    });

    // Search Validation
    var validateSearch = function(){
        var query = $("#txtSearchTerm").val();
        var mobilequery = $("#mobile-txtSearchTerm").val();
        if(query && query !=''){
            document.location.href = '/search-results?q='+query;
        }else{
            console.log("ERROR");
        }
        if(mobilequery && mobilequery !=''){
            document.location.href = '/search-results?q='+mobilequery;
        }else{
            console.log("ERROR");
        }
    }
    $('#btnSearch').click(function(){
        validateSearch();
    });
    $('#txtSearchTerm').keyup(function(e){
        if(e.keyCode == 13){
            validateSearch();
        }
    });
    $("#btnSearchIconHead").click(()=>{
        $('#txtSearchTerm').focus();
    });
});

// On page load set the theme.
(function() {
  let onpageLoad = localStorage.getItem("theme") || "light";
  let element = document.body;
  if(element && onpageLoad){
     element.classList.toggle(onpageLoad);
     document.getElementById("theme").textContent = localStorage.getItem("theme") || "light";
     let mic = document.getElementById('responsiveMic')
     if (!mic) {
        mic = document.getElementById('fontLarge')
     }
     mic.addEventListener('click', () => {
         if (responsiveVoice.isPlaying()) {
            responsiveVoice.cancel()
        }
     })
  }

})();

function themeToggle() {
  let element = document.body;
  element.classList.toggle("site-dark");

  let theme = localStorage.getItem("theme");
  if (theme && theme === "site-dark") {
    localStorage.setItem("theme", "light");
  } else {
    localStorage.setItem("theme", "site-dark");
  }

  document.getElementById("theme").textContent = localStorage.getItem("theme");
}

function getYTvideos(link, event) {
	event.preventDefault();
    var href = link.getAttribute("href");
    console.log(link);
    document.getElementById('sign_lang_YT_videos').src = href;
    jQuery('#signlanguage').modal();
    return false;
}

