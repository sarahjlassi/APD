odoo.define('website_inherit.rating_script', function (require) {
    'use strict';

    var ajax = require('web.ajax');




      $(document).keydown(function(e) {
            if (e.ctrlKey && e.altKey && e.key === 'h') {
                window.location.href = '/';
            }

            else if (e.ctrlKey && e.altKey && e.key === 'b') {
                window.location.href = '/my/home';
            }

//             else if (e.ctrlKey && e.shiftKey && e.key === 's') {
//                // Scroll to the bottom of the page
//               window.scrollBy(0, window.innerHeight);
//            }
        });

const choiceRadios = document.querySelectorAll('.choice');
  const radioGroups = document.querySelectorAll('.radio-group');

  choiceRadios.forEach((radio) => {
    radio.addEventListener('change', () => {
      radioGroups.forEach((group) => {
        group.style.display = 'none';
      });

      const selectedRadioGroup = document.querySelector(`#radio-group-${radio.id}`);
      selectedRadioGroup.style.display = 'block';
    });
  });

    const radioOther = document.querySelector('#radio5');
  const commentContainer_yes = document.querySelector('#comment-container_yes');

  radioOther.addEventListener('change', () => {
    if (radioOther.checked) {
      commentContainer_yes.style.display = 'block';
    } else {
      commentContainer_yes.style.display = 'none';
    }
  });


    const radioOtherno = document.querySelector('#radio10');
  const commentContainer_no = document.querySelector('#comment-container_no');

  radioOtherno.addEventListener('change', () => {
    if (radioOtherno.checked) {
      commentContainer_no.style.display = 'block';
    } else {
      commentContainer_no.style.display = 'none';
    }
  });

/*
$(document).on('keyup', function(e) {
 *//* if (e.which == 77) {
    alert("M key was pressed");

  }*//*



   // it goes to the /home if we press alt+B
    if (e.ctrlKey && e.which == 66) {
    window.location.href = '/';
  }
   // it goes to the /my/home if we press alt+C
    else if (e.ctrlKey && e.which == 67) {
    window.location.href = '/my/home';
  }


     else if (e.ctrlKey && e.which == 81) {
     console.log("change language")
        var currentUrl = window.location.href;
            var newLanguageCode = "";

            if (currentUrl.includes("/en/")) {
                newLanguageCode = "ar";
                var newUrl = currentUrl.replace(/\/[a-z]{2}\//, "/" + newLanguageCode + "/");
                window.location.href = newUrl;
            }
            else{
                // If language code is not present, default to English
                newLanguageCode = "en";
                var urlParts = currentUrl.split("/");
                urlParts.splice(1, 0, newLanguageCode); // Insert language code after third "/"
                newUrl = urlParts.join("/");
            }


  }


*/
/*   else if (e.ctrlKey && e.altKey && e.which == 89) {
    alert("Ctrl + Alt + Y shortcut combination was pressed");
  } else if (e.ctrlKey && e.altKey && e.shiftKey && e.which == 85) {
    alert("Ctrl + Alt + Shift + U shortcut combination was pressed");
  }*//*
});*/

     /*   $(document).ready(function() {
        $(".advanced-search-link").click(function(event) {
            event.preventDefault(); // Prevent the link from performing its default action (going to href="#").
            var currentUrl = window.location.href;
            var separator = currentUrl.indexOf('?') !== -1 ? '&' : '?';
            var newUrl = currentUrl + separator + 'adv=1';
            window.location.href = newUrl;
        });
    });*/


    function toggleSearchElements() {
                var advancedForm = $('.advanced-search-form');
                var searchDiv = $('[role="search"]');

                var linkadv = $('.advanced-search-link');

                if (advancedForm.length && searchDiv.length) {
                    if (advancedForm.is(':visible')) {
                    linkadv.text('بحث متقدم');
                        advancedForm.hide();
                        searchDiv.show();
                    } else {

                     linkadv.text('بحث بسيط');
                        advancedForm.show();
                        searchDiv.hide();
                    }
                }
            }
        // Function to toggle the visibility of the search elements
           $(document).ready(function() {
            // Function to toggle the visibility of the search elements


            // Event listener for the "Advanced Search" link
            var advancedSearchLink = $('.advanced-search-link');
            if (advancedSearchLink.length) {
                advancedSearchLink.on('click', function(event) {
                    event.preventDefault();
                    toggleSearchElements();
                });
            }

            // Event listener for the search form submit
            var searchForm = $('.form_advanced');
            if (searchForm.length) {
                searchForm.on('submit', function(event) {
                    // Prevent the default form submission

                    // You can add additional logic here to handle form submission if needed

                    // Toggle the visibility after form submission

                });
                advancedForm.show();
                        searchDiv.hide();
            }
        });



    $(document).ready(function () {
        // JavaScript to get the number of stars selected
        const stars = document.querySelectorAll('input[name="rating"]');
        const path=document.getElementById("path").value;
        console.log('path',path)
        let selectedStars = 0;

        stars.forEach(star => {
            star.addEventListener('change', (event) => {
                selectedStars = parseInt(event.target.value);
                console.log("Selected stars: " + selectedStars);

                // Show the form after a rating is selected
                const formContainer = document.querySelector('.form-container');
                formContainer.style.display = 'block';
            });
        });

        // AJAX function to send the rating value to the controller
        $('form_rating').on('submit', function (event) {
            event.preventDefault();
            ajax.jsonRpc('/rating/rate', 'call', {
                'rating': selectedStars,
                // Include any other form data you want to send to the controller
                // For example: name: $('#name').val(), email: $('#email').val(), etc.
            }).then(function (result) {
                // Handle the response from the controller if needed
                console.log('Rating submitted successfully');
                // You can redirect or show a success message here
            });
        });

    ajax.jsonRpc('/rating/calculate_length', 'call', {'path': path})
            .then(function(result) {



              var lengthElement = $('<span>').text("(  التقييم"+" " +result+")").css({
                'font-size': '18px',
                'margin-left': '5px',
            });

            // Append the lengthElement inside the <h3> element
            $('.rate_page').append(lengthElement);
            })
            .catch(function(error) {
                console.error('Error fetching data:', error);
            });



       ajax.jsonRpc('/rating/calculate_nb_comment', 'call', {'path': path})
            .then(function(result) {



              var cmtElement = $('<span>').text(" ("+ result +" زائر علق على المحتوى"+") ").css({
                'font-size': '12px',
                'margin-left': '5px',
            });

            // Append the lengthElement inside the <h3> element
            $('.cmt').append(cmtElement);
            })
            .catch(function(error) {
                console.error('Error fetching data:', error);
            });





    });

});
