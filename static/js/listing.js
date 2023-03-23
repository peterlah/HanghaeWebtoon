function listing() {
    fetch('/webtoon').then((res) => res.json()).then((data) => {
        $('#cards-box').empty();
        let webtoon_list = JSON.parse(data['result']);
        webtoon_list.forEach((web) => {
            let webtoon_id = web['_id']['$oid'];
            let title = web['title'];
            let img = web['image_source'];
            let descript = web['description'];

            let comment_count = web['comment_count'];
            let acc_star = web['acc_star'];

            let ave_star = 0
            if (ave_star) {
                ave_star = acc_star / comment_count;

            }
            let star = '⭐'
            let total_star = star.repeat(ave_star);
            let webtoon_card = `<div class="col">
                                    <div class="card h-100" onclick="webtoon_detail('${webtoon_id}')">
                                        <!-- <a href='/detail/${webtoon_id}' style='text-decoration:none; color:black'> -->
                                            <img src="${img}" class="card-img-top">
                                            <div class="card-body">
                                                <h5 class="card-title">${title}</h5>
                                                <p> 평점 : ${ave_star} 리뷰: ${comment_count}</p>
                                            </div>
                                        <!-- </a> -->
                                    </div>
                                </div>`
            $('#cards-box').append(webtoon_card)
        })

    })
}