function login() {
    let loginUser = $('#loginuser').val()
    let loginPassword= $('#loginpassword').val()

    let formData = new FormData();

    formData.append("loginuser", loginUser);
    formData.append("loginpassword", loginPassword);

    fetch('/login', {method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        let status = data['status'];
        let message = data['msg'];

        alert(message)

        if (status) {
            location.href = '/mypage';
        } else {
            location.href = '/login';
        }
    })
}