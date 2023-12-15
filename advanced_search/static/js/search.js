odoo.define('advanceed_search.search_script', function (require) {
    'use strict';

    var ajax = require('web.ajax');


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
           var language=$(".current_lang_s").value ;
           console.log('languuuue',language)

           var advancedForm = $('.advanced-search-form');
                var searchDiv = $('[role="search"]');

                var linkadv = $('.advanced-search-link');

if (advancedForm.is(':visible')) {

                        searchDiv.hide();
}

else {
 searchDiv.show();
}


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


        });