function posting() {
    let url = $('#url').val()
    let comment = $('#comment').val()
    let star = $('#star').val()

    let formData = new FormData()
    formData.append("url_give", url)
    formData.append("comment_give", comment)
    formData.append("star_give", star)

    fetch('/mypage', { method: "POST", body: formData }).then(res => res.json()).then(data => {
        alert(data['msg'])
        window.location.reload()
    })
}