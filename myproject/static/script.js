btn1 = document.getElementById('btn1')
btn1.addEventListener("click", fn1)
btn2 = document.getElementById('btn2')
btn2.addEventListener("click", myFunction)
login_form = document.getElementById('login_form')
registration = document.getElementById('registration')

function bodyload() {
    login_form.style.display = "none";
    btn1.classList.add("active");
};

function myFunction(){
    registration.style.display = "none";
    login_form.style.removeProperty('display');
    btn2.classList.add("active");
    btn1.classList.remove("active");
}

function fn1(){
    login_form.style.display = "none";
    registration.style.removeProperty('display');
    btn1.classList.add("active");
    btn2.classList.remove("active");
}