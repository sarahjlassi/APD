odoo.define('test_apd.categoryDropdown', function (require) {
    "use strict";

    var core = require('web.core');

    $(document).ready(function () {
        var categoryDropdown = $('#categoryDropdown');

        categoryDropdown.on('change', function () {
            var selectedCategory = categoryDropdown.val();

            $.ajax({
                url: '/landing_page',
                type: 'POST',
                data: {
                    search_name: selectedCategory,
                },
                success: function (response) {
                    console.log('response',response);
                    console.log('search_name',search_name);
                },
                error: function (xhr, textStatus, errorThrown) {
                }
            });
        });
    });
});