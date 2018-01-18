function check_element() {
    herw = location.href;
    window.alert(herw);
}

function get_year() {
    var year, text, inn;
    inn = document.getElementById("NNN").valueOf();
    year = inn.value;
    if (isNaN(year) || year < 1960 || year > 2017) {
        text = "U bustard";
        inn.style.backgroundColor = "#FF7F50";
    } else {
        text = "Everything is okay";
        inn.style.backgroundColor = "#FFF";
    }
    document.getElementById("demo").innerHTML = text;
}


function get_year_of_prod2() {
    var year, text, inn;
    inn = document.getElementById("inp_year_of_prod2").valueOf();
    year = inn.value;
    if (isNaN(year) || year < 1960 || year > 2017) {
        text = "U bustard again mate";
        inn.style.backgroundColor = "#FF7F50";
    } else {
        inn.style.backgroundColor = "#FFF";
    }
    document.getElementById("demo2").innerHTML = text;
}

function reg_password_check1() {
    var pass_in, pass_value, help_text;
    pass_in = document.getElementById("password1").valueOf();
    help_text = document.getElementById("password_error1").valueOf();
    pass_value = pass_in.value;
    if (pass_value.length < 8 || pass_value.length > 20) {
        // noinspection JSAnnotator
        help_text.style.display = "block";

    } else {
        // noinspection JSAnnotator
        help_text.style.display = "none";
    }
}

function reg_password_check2() {
    var pass1, pass2, help_text;
    pass1 = document.getElementById("password1").valueOf().value;
    pass2 = document.getElementById("password2").valueOf().value;
    help_text = document.getElementById("password_error2").valueOf();
    if (pass1 === pass2) {
        help_text.style.display = "none";
    } else {
        help_text.style.display = "block";
    }
}

function reg_selector() {
    var selector, deleteit;
    selector = document.getElementById("reg_user_selector").valueOf().value;
    // window.alert(selector);
    deleteit = document.querySelectorAll('.user_tag input');
    deleteit.valueOf().value = '';
    if (selector === "----") {
        $(".user_tag").css("display", "none");
        document.getElementsByClassName("user_tag").valueOf = null;
        $(".company_tag").css("display", "none");
        $("#moderator_tag").css("display", "none");
        $("#phone_tag").css("display", "none");
        $("#reg_submit_tag").css("display", "none");
    }
    if (selector === "Пользователь") {
        $(".user_tag").css("display", "table-row");
        $(".company_tag").css("display", "none");
        $("#moderator_tag").css("display", "none");
        $("#phone_tag").css("display", "table-row");
        $("#reg_submit_tag").css("display", "table-row");
    }
    if (selector === "Компания") {
        $(".user_tag").css("display", "none");
        $(".company_tag").css("display", "table-row");
        $("#moderator_tag").css("display", "none");
        $("#phone_tag").css("display", "table-row");
        $("#reg_submit_tag").css("display", "table-row");
    }
    if (selector === "Модератор") {
        $(".user_tag").css("display", "none");
        $(".company_tag").css("display", "none");
        $("#moderator_tag").css("display", "table-row");
        $("#phone_tag").css("display", "none");
        $("#reg_submit_tag").css("display", "table-row");
    }
}

function del_del() {
    var del_list, i, selector;
    selector = document.getElementById("reg_user_selector").valueOf().value;
    if (selector === "----") {
    }
    if (selector === "Пользователь") {
        del_list = document.getElementsByClassName("company_tag_input");
        for (i = 0; i < del_list.length; i++) {
            del_list.item(i).valueOf().value = "";
        }
        document.getElementById("moderator_tag_input").valueOf().value = "";
    }
    if (selector === "Компания") {
        del_list = document.getElementsByClassName("user_tag_input");
        for (i = 0; i < del_list.length; i++) {
            del_list.item(i).valueOf().value = "";
        }
        document.getElementById("reg_sel_gender").valueOf().value = "----";
        document.getElementById("moderator_tag_input").valueOf().value = "";
    }
    if (selector === "Модератор") {
        del_list = document.getElementsByClassName("user_tag_input");
        for (i = 0; i < del_list.length; i++) {
            del_list.item(i).valueOf().value = "";
        }
        document.getElementById("reg_sel_gender").valueOf().value = "----";
        del_list = document.getElementsByClassName("company_tag_input");
        for (i = 0; i < del_list.length; i++) {
            del_list.item(i).valueOf().value = "";
        }
        document.getElementById("reg_phone_input").valueOf().value = "";
    }
}

function add_freight_address1() {
    var address;
    address = document.getElementById("freight_input_address1").valueOf().value;
    // window.alert(address);
    document.getElementById("freight_ya_address1").innerHTML = address;
}

function add_freight_address2() {
    var address;
    address = document.getElementById("freight_input_address2").valueOf().value;
    document.getElementById("freight_ya_address2").innerHTML = address;
}

function add_post_inp_img1() {
    document.getElementById("add_post_img_inp1").style.display = "table-row";
    document.getElementById("add_post_img_btn1").style.display = "none";
    document.getElementById("add_post_img_btn2").style.display = "table-row";
}

function add_post_inp_img2() {
    document.getElementById("add_post_img_inp2").style.display = "table-row";
    document.getElementById("add_post_img_btn2").style.display = "none";
    document.getElementById("add_post_img_btn3").style.display = "table-row";
}

function add_post_inp_img3() {
    document.getElementById("add_post_img_inp3").style.display = "table-row";
    document.getElementById("add_post_img_btn3").style.display = "none";
    document.getElementById("add_post_img_btn4").style.display = "table-row";
}

function add_post_inp_img4() {
    document.getElementById("add_post_img_inp4").style.display = "table-row";
    document.getElementById("add_post_img_btn4").style.display = "none";
    document.getElementById("add_post_img_btn5").style.display = "table-row";
}

function add_post_inp_img5() {
    document.getElementById("add_post_img_inp5").style.display = "table-row";
    document.getElementById("add_post_img_btn5").style.display = "none";
}

function freight_info_map1(){
    document.getElementById("freight_info_map").style.display = "table-row";
    document.getElementById("freight_info_btn2").style.display = "table-row";
    document.getElementById("freight_info_btn1").style.display = "none";
}
function freight_info_map2(){
    document.getElementById("freight_info_map").style.display = "none";
    document.getElementById("freight_info_btn2").style.display = "none";
    document.getElementById("freight_info_btn1").style.display = "table-row";
}