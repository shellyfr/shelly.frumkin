function switchToAbout(){

    document.getElementById('aboutMe').style.display = 'block';
    document.getElementById('skills').style.display = 'none';
    document.getElementById('education').style.display = 'none';
    document.getElementById('contact').style.display = 'none';

}

function switchToSkills(){
    document.getElementById('aboutMe').style.display = 'none';
    document.getElementById('skills').style.display = 'block';
    document.getElementById('education').style.display = 'none';
    document.getElementById('contact').style.display = 'none';
}


function switchToEducation(){
    document.getElementById('aboutMe').style.display = 'none';
    document.getElementById('skills').style.display = 'none';
    document.getElementById('education').style.display = 'block';
    document.getElementById('contact').style.display = 'none';
}

const name="SHELLY FRUMKIN";
let i =0;
let speed=50;

function loadName(){
    if(i < name.length){
        document.getElementById('nameF').innerHTML += name.charAt(i);
        i++;
        setTimeout(loadName(), speed);
    }
}


function switchToContact(){
    document.getElementById('aboutMe').style.display = 'none';
    document.getElementById('skills').style.display = 'none';
    document.getElementById('education').style.display = 'none';
    document.getElementById('contact').style.display = 'block';
}