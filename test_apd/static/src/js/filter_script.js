odoo.define('test_apd.filter_script', function (require) {
    'use strict';

    var ajax = require('web.ajax');

                       filterSelection("all")
          function filterSelection(c) {
            var x, i;
            x = document.getElementsByClassName("filterDiv");
            if (c == "all") c = "";
            for (i = 0; i &lt; x.length; i++) {
              RemoveClass(x[i], "show");
              if (x[i].className.indexOf(c) > -1) AddClass(x[i], "show");
            }
          }

          function AddClass(element, name) {
            var i, arr1, arr2;
            arr1 = element.className.split(" ");
            arr2 = name.split(" ");
            for (i = 0; i &lt; arr2.length; i++) {
              if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
            }
          }

          function RemoveClass(element, name) {
            var i, arr1, arr2;
            arr1 = element.className.split(" ");
            arr2 = name.split(" ");
            for (i = 0; i &lt; arr2.length; i++) {
              while (arr1.indexOf(arr2[i]) > -1) {
                arr1.splice(arr1.indexOf(arr2[i]), 1);
              }
            }
            element.className = arr1.join(" ");
          }








        // Function to toggle the visibility of the search elements
           $(document).ready(function() {

   var btnContainer = document.getElementById("myBtnContainer");
          var btns = btnContainer.getElementsByClassName("btn");
          for (var i = 0; i &lt; btns.length; i++) {
            btns[i].addEventListener("click", function(){
              var current = document.getElementsByClassName("active");
              current[0].className = current[0].className.replace(" active", "");
              this.className += " active";
            });
          }
   $('#categorySelector').change(function(){
            $('.c1').hide();
            $('#' + $(this).val()).show();
        });
        });

         });