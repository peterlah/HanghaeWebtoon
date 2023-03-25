function login_page() {
    $('#cards-box').empty();
    let login_box = `<div class="card" style="margin-top: 100px; width: 400px; height: 350px; margin-left: auto; margin-right: auto;">
                        <div class="card-body">
                    
                            <div class="row mt-5">
                                <h1 style="text-align: center;">로그인</h1>
                            </div>
                    
                            <div class="col-12">
                                <form method="POST" action="/login">
                                    <div class="form-group" style="margin-top: 10px;">
                                        <label for="user" style="margin-left: 3px;">아이디</label>
                                        <input type="text" class="form-control" id="loginuser" placeholder="아이디" name="loginuser" />
                                    </div>
                                    <div class="form-group" style="margin-top: 10px;">
                                        <label for="password" style="margin-left: 3px;">비밀번호</label>
                                        <input type="password" class="form-control" id="loginpassword" placeholder="비밀번호" name="loginpassword" />
                                    </div>
                                    <div style="display: flex;">
                                        <button onclick="login()" type="submit" class="btn btn-primary" style="margin-top: 10px; margin-left: auto;">로그인</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>`
    $('#cards-box').append(login_box)
}