$(document).ready(function () {
    $('#doctors').DataTable({
        "ajax": "/doctor/page"
        , "processing": true
        , "serverSide": true
        , "fnDrawCallback": function (settings) {
            console.log();
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
});