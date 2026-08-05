document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".tomselect").forEach(function (element) {
        element.tomselect || new TomSelect(element, {
            create: false,
            sortField: {
                field: "text",
                direction: "asc"
            }
        });
    });

    const modalElement = document.getElementById("crudModal");
    const modalContent = document.getElementById("crudModalContent");
    const modal = modalElement ? new bootstrap.Modal(modalElement) : null;
    let selectTarget = null;

    document.addEventListener("click", async function (event) {
        const button = event.target.closest(".js-create-related");
        if (!button) return;
        selectTarget = document.getElementById(button.dataset.target);
        const response = await fetch(button.dataset.modalUrl, {
            headers: {"X-Requested-With": "XMLHttpRequest"}
        });
        modalContent.innerHTML = await response.text();
        modal.show();
    });

    modalContent.addEventListener("submit", async function (event) {
        const form = event.target.closest(".js-modal-form");
        if (!form) return;
        event.preventDefault();
        const response = await fetch(form.action || window.location.href, {
            method: "POST",
            body: new FormData(form),
            headers: {"X-Requested-With": "XMLHttpRequest"}
        });
        const type = response.headers.get("content-type") || "";
        if (!type.includes("application/json")) {
            modalContent.innerHTML = await response.text();
            return;
        }
        const option = await response.json();
        if (selectTarget.tomselect) {
            selectTarget.tomselect.addOption(option);
            selectTarget.tomselect.addItem(String(option.id));
        } else {
            selectTarget.add(new Option(option.text, option.id, true, true));
        }
        modal.hide();
    });
});
