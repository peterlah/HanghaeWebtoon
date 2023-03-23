function login() {
    let user = $('#user').val()
    let pw = $('#password').val()

    let formData = new FormData();

    formData.append("user_give", user);
    formData.append("pw_give", pw);

    fetch('/login', {method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        console.log(data);
        alert(data['msg'])
        window.location.reload()
    })
}