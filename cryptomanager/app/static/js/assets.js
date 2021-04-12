document.addEventListener('DOMContentLoaded', function (event) {

    $('#table').DataTable({
        "searching": false,
        "order": [["2", "asc"]],
        "aLengthMenu": [2, 5, 10, 25],
        "iDisplayLength": 2,
        "pagingType": "numbers",
        "info": false,
    });
})
