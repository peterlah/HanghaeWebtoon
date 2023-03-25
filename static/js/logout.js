function logout() {
    fetch('/logout', {method: "POST", body: formData }).then((res) => res.json()).then((data) => {
        let status = data['status'];
        let message = data['msg'];

        alert(message)

        if (status) {
            location.href = '/login'
        }
    })
}