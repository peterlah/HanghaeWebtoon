function register() {
    let user = $('#user').val()
    let mail = $('#email').val()
    let pw = $('#password').val()
    let pw_check = $('#re_password').val()

    let formData = new FormData();

    formData.append("user_give", user);
    formData.append("email_give", mail);
    formData.append("pw_give", pw);
    formData.append("pw_check_give", pw_check);

    // fetch('/register').then((res) => res.json()).then((data) => {
    //     alert(data['msg'])
    // })
    fetch('/register', {method: 'POST', body: formData}).then((res) => {
        return res.json()
      }).then((data) => {
        alert(data['msg'])
      })
}