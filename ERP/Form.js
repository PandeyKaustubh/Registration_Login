function Myfunc() {

    var fname, lname, add, city, st, zip, scb, hq, phno, email, gen, user, pass;

    fname = document.getElementById("Fname").value;
    lname = document.getElementById("Lname").value;
    add = document.getElementById("Add").value;
    city = document.getElementById("City").value;
    st = document.getElementById("State").value;
    zip = document.getElementById("Pin").value;
    scb = document.getElementById("School").value;
    hq = document.getElementById("HighestQualification").value;
    phno = document.getElementById("Mobile_no").value;
    email = document.getElementById("Email").value;
    user = document.getElementById("User").value;
    pass = document.getElementById("Pass").value;
    gen = document.querySelector('input[name="RDB"]:checked').value;




    var j = {
        "Fname": fname,
        "Lname": lname,
        "Address": add,
        "City": city,
        "State": st,
        "PinCode": zip,
        "School": scb,
        "HighestQualification": hq,
        "Mobile_no": phno,
        "Email": email,
        "Username": user,
        "Password": pass,
        "Gender": gen


    };


    var s = JSON.stringify(j);


    request(s);


}

function request(a) {
    var xmlhttp = new XMLHttpRequest();
    var data;


    xmlhttp.onreadystatechange = function () {

        document.write(" ");


        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            data = JSON.parse(xmlhttp.response);
        
            if (data.Status == "OK")
             {
                alert('RECORD INSERTED');
                window.location.href = "/home/kp_d_best/Desktop/ERP/Login/Login.html";
            }
             else if (data.Status == "Wrongpass")
              {
                alert("Username already exist ! Please choose again");
                window.location.href = "/home/kp_d_best/Desktop/ERP/Form.html";
              }
            else if (data[0].link__Fname)
             {
                alert("User already exists!! Please Login");
                window.location.href = "/home/kp_d_best/Desktop/ERP/Login/Login.html";
            }
            

        }

    }


    xmlhttp.open("POST", "http://127.0.0.1:8000/data/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send(a);


}
This is the code for form validation
