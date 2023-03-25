function mypageListing() {
    fetch('/mypage/list').then(res => res.json()).then(data => {
        let rows = data['result']
        $('#cards-box').empty()
        rows.forEach((a) => {
            let comment = a['comment']
            let title = a['title']
            let image = a['image']
            let desc = a['desc']
            let star = a['star']
            let star_repeate = '⭐'.repeat(star)
            let id = a['id']

            let temp_html = `<div class="col">
                                    <div class="card h-100">
                                        <img src="${image}" class="card-img-top">
                                    <div class="card-body">
                                        <p id="hide-id" style="display: none;">${id}</p>
                                        <h5 class="card-title">${title}</h5>
                                        <p class="card-text">${desc}</p>
                                        <p>${star_repeate}</p>                                                    
                                        <p class="mycomment">${comment}</p>
                                        <button onclick="deleting('${id}')" type="button" class="btn btn-outline-success btn-sm">삭제</button>
                                    </div>
                                </div>
                            </div>`

            $('#cards-box').append(temp_html)
        })
    })
}