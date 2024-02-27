document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementsByClassName(".message-input");

    textarea.oninvalid = function (event) {
        event.target.setCustomValidity(
            "Please fill out the message before sending"
        );
    };

    textarea.oninput = function (event) {
        // Clear the custom validity message once the user starts typing
        event.target.setCustomValidity("");
    };
});
