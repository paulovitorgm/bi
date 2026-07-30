document.addEventListener("DOMContentLoaded", function () {

    document.querySelectorAll(".tomselect").forEach(function (element) {

        new TomSelect(element, {
            create: false,
            sortField: {
                field: "text",
                direction: "asc"
            }
        });

    });

});