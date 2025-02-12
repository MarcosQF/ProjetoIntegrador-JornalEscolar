$(document).ready(function () {
    var table = $('#example').DataTable({
        responsive: true,
        language: {
            url: 'https://cdn.datatables.net/plug-ins/1.10.19/i18n/Portuguese-Brasil.json'
        }
    })
    .columns.adjust()
    .responsive.recalc();
});