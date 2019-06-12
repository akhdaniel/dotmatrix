odoo.define('dotmatrix.print_button', function(require){
"use strict";

var FormController = require('web.FormController');

FormController.include({
    _onButtonClicked: function(event){
        console.log(event);

        if(event.data.attrs.custom == "print"){
            var printer_data = event.data.record.data.printer_data;
            if (!printer_data){
                alert('No printer data! Please click the Refresh Printer Data button');
                return;
            }
            console.log(printer_data);

            var url = "http://localhost:8000/dotmatrix/print";
            $.ajax({
                type:"POST",
                url: url,
                data: {
                    printer_data: printer_data
                },
                success: function(data){
                    alert('Print successfull!');
                },
                error: function(data){
                    alert('Dotmatrix print failed! Is Proxy Running ?')
                    console.log(data);
                }
            });
        }

        this._super(event);
    }
});
});