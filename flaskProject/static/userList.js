fetch('https://reqres.in/api/users?page=2')
.then(response => response.json())
.then (responseJSON => creatUsersList (responseJSON.data))
.catch(err => console.log(err));


function creatUsersList (users){
    const user = users[0];
    const curr_main = document.querySelector("main");
    for (let user of users){
        const section = document.createElement('section');
        section.innerHTML=`
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
                <span>${user.first_name} ${user.last_name} </span>
                <br>
               
            </div>`;
        curr_main.appendChild(section);

    }
}