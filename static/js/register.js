function register() {
    let registerUser = $('#registeruser').val()
    let registerEmail = $('#registeremail').val()
    let registerPassword = $('#registerpassword').val()
    let pw_check = $('#re_password').val()

    let formData = new FormData();

    formData.append("registeruser", registerUser);
    formData.append("registeremail", registerEmail);
    formData.append("registerpassword", registerPassword);
    formData.append("re_password", pw_check);

    fetch('/register', { method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        let status = data['status'];
        let message = data['msg'];

        alert(message)

        if (status) {
            location.href = '/login';
        } else {
            location.href = '/register';
        }
    })
}