$(document).ready(function () {
    $('#pets').DataTable({
        "ajax": "/pet/page"
        , "columns": [
            { "data": "name" }
            , { "data": "birthDate" }
            , { "data": "type" }
            , { "data": "client" }
        ]
        , "processing": true
        , "serverSide": true
        , "fnDrawCallback": function (settings) {
            var pager = $(settings.nTableWrapper).find(".dataTables_paginate")
            if (settings._iDisplayLength == -1
                || settings._iDisplayLength > settings.fnRecordsDisplay()
                || settings._iDisplayLength > settings.aoData.length) {
                pager.hide();
            } else {
                pager.show()
            }
        }
    });

    $("#birthDate").datepicker({
        format: "dd MM yyyy",
        autoclose: true,
        todayBtn: true,
        minuteStep: 10
    });
});
