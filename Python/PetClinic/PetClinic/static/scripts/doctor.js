$(document).ready(function () {
    $('#doctors').DataTable({
        "ajax": "/doctor/page"
        , "processing": true
        , "serverSide": true
    });
});