function webtoon_detail(id) {
    fetch(`/detail/${id}`).then((res) => res.json()).then((data) => {
        let one_webtoon = JSON.parse(data['result']);
        let select_title = one_webtoon['title'];
        let select_des = one_webtoon['description'];
        let select_img = one_webtoon['image_source'];

        let scroll = document.documentElement.scrollTop;
        let window = `
                    <div class="modal_window">
                        <div class='modal_innerimg' style = "background-image : url('${select_img}')"";>
                        </div>
                        <h5> ${select_title} </h5>
                        <p> ${select_des} <p>
                    </div>`
        console.log(scroll)
        $('#modal_frame').append(window)
        let modal = document.querySelector('#modal_frame')
        modal.style.display = "flex";

        modal.addEventListener("click", e => {
            modal.style.display = 'none';
            $('#modal_frame').empty();
        })
    })
}