const $Nombre=document.getElementById('txt');
const $provForm=document.getElementById('provForm');

(function() {

    $provForm.addEventListener('submit', function(e){
        let nombre = String($Nombre.value).trim();
        if (nombre.length === 0){
            alert("el nombre está vacío")
            e.preventDefault();
        }
        
    });


})();