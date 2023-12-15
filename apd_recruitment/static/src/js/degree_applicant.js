odoo.define('apd_recruitment.degree_applicant', function (require) {

    "use strict";
    console.log("Degree APliacanttttt")
    // Odoo class to calling an url with JSONRPC
    var ajax = require('web.ajax');

    $('#degree_id_c').change(function(){
            console.log("Is Degree Chnge");
            ajax.jsonRpc("/is_collage_degree", 'call', {'degree_id_c': $(this).val()})
            .then(function (data) { // success
                  // Action after update
                  if(data){
                    $('#spcecial_div').show();
                    document.getElementById("special_c").required = true;

                    $('#gpa_div').show();
                    document.getElementById("gpa").required = true;
                  }
                  else{
                    $('#spcecial_div').hide();
                    document.getElementById("special_c").required = false;

                     $('#gpa_div').hide();
                    document.getElementById("gpa").required = false;
                  }
            });
    });

    });

