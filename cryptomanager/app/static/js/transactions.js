document.addEventListener('DOMContentLoaded', function (event) {

    $('#table').DataTable({
        "searching": false,
        "order": [["0", "desc"]],
        "aLengthMenu": [2, 5, 10, 25],
        "iDisplayLength": 5,
        "pagingType": "numbers",
        "info": false,
    });
})