function register_page() {
    $('#cards-box').empty();
    let register_box = `<div class="card" style="margin-top: 100px; width: 400px; height: 500px; margin-left: auto; margin-right: auto;">
                            <div class="card-body" >
                                <div class="row mt-5">
                                    <h1 style="text-align: center;">회원가입</h1>
                                </div>

                                <div class="col-12" >
                                    <!-- Form 테그 https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=heartflow89&logNo=221159929166 -->
                                    <form method="POST" action="/register">
                                        <div class="form-group" style="margin-top: 10px;">
                                            <label for="user" style="margin-left: 3px;">아이디</label>
                                            <input type="text" class="form-control" id="registeruser" placeholder="아이디" name="registeruser" />
                                        </div>
                                        <div class="form-group" style="margin-top: 10px;">
                                            <label for="email" style="margin-left: 3px;">이메일</label>
                                            <input type="email" class="form-control" id="registeremail" placeholder="이메일" name="registeremail" />
                                        </div>
                                        <div class="form-group" style="margin-top: 10px;">
                                            <label for="password" style="margin-left: 3px;">비밀번호</label>
                                            <input type="password" class="form-control" id="registerpassword" placeholder="비밀번호" name="registerpassword" />
                                        </div>
                                        <div class="form-group" style="margin-top: 10px;">
                                            <label for="re_password" style="margin-left: 3px;">비밀번호 확인</label>
                                            <input type="password" class="form-control" id="re_password" placeholder="비밀번호 확인"
                                                name="re_password" />
                                        </div>
                                        <div style="display: flex;">
                                            <button onclick="register()" type="submit" class="btn btn-primary" style="margin-top: 10px; margin-left: auto;">회원가입</button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>`
    $('#cards-box').append(register_box)
}